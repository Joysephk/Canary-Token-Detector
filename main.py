import re
import sys
import os
import zipfile
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def extract_canarytokens_from_ini(file_path):
    """Extracts and prints Canarytoken URLs from a .ini file."""
    pattern = re.compile(r"\\%USERNAME%\.%COMPUTERNAME%\.%USERDOMAIN%\.INI\.\w+\.canarytokens\.com\\resource\.dll")
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            matches = pattern.findall(content)
            if matches:
                print(Fore.GREEN + "[+] Detected Canarytoken URLs in INI file:")
                for match in matches:
                    print(Fore.YELLOW + match)
            else:
                print(Fore.RED + "[-] No Canarytoken URLs found in INI file.")
    except FileNotFoundError:
        print(Fore.RED + "[!] INI file not found. Check the file path.")
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred while processing INI file: {e}")

def detect_canarytokens_in_reg(file_path):
    """Detects occurrences of '.canarytokens.com' in a .reg file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            if '.canarytokens.com' in content:
                print(Fore.GREEN + f"[+] Detected '.canarytokens.com' in {file_path}")
            else:
                print(Fore.RED + f"[-] No '.canarytokens.com' found in {file_path}")
    except FileNotFoundError:
        print(Fore.RED + "[!] REG file not found. Check the file path.")
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred while processing REG file: {e}")

def extract_canarytokens_from_xlsx(file_path):
    """Extract and detect canary tokens inside the xl/drawings/_rels/ folder in an xlsx file."""
    canary_pattern = re.compile(r'http://canarytokens\.com[^\s]*')

    try:
        with zipfile.ZipFile(file_path, 'r') as xlsx_zip:
            file_list = xlsx_zip.namelist()
            rels_files = [f for f in file_list if f.startswith('xl/drawings/_rels/')]

            concatenated_content = ''
            for rels_file in rels_files:
                with xlsx_zip.open(rels_file) as file:
                    content = file.read().decode('utf-8', errors='ignore')
                    concatenated_content += content

            matches = canary_pattern.findall(concatenated_content)
            if matches:
                print(Fore.GREEN + f"[+] Detected Canarytokens URLs in '{file_path}':")
                for match in matches:
                    print(Fore.YELLOW + f"    {match}")
            else:
                print(Fore.RED + f"[-] No Canarytokens URLs found in '{file_path}'.")

    except zipfile.BadZipFile:
        print(Fore.RED + f"[!] The file '{file_path}' is not a valid .xlsx file or is corrupted.")
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred while processing '{file_path}': {e}")

def extract_canarytokens_from_docx(file_path):
    """Extract and detect canary tokens inside the word/_rels/ folder in a .docx file."""
    canary_pattern = re.compile(r'http://canarytokens\.com[^\s]*')

    try:
        with zipfile.ZipFile(file_path, 'r') as docx_zip:
            file_list = docx_zip.namelist()
            rels_files = [f for f in file_list if f.startswith('word/_rels/')]

            concatenated_content = ''
            for rels_file in rels_files:
                with docx_zip.open(rels_file) as file:
                    content = file.read().decode('utf-8', errors='ignore')
                    concatenated_content += content

            matches = canary_pattern.findall(concatenated_content)
            if matches:
                print(Fore.GREEN + f"[+] Detected Canarytokens URLs in '{file_path}':")
                for match in matches:
                    print(Fore.YELLOW + f"    {match}")
            else:
                print(Fore.RED + f"[-] No Canarytokens URLs found in '{file_path}'.")

    except zipfile.BadZipFile:
        print(Fore.RED + f"[!] The file '{file_path}' is not a valid .docx file or is corrupted.")
    except Exception as e:
        print(Fore.RED + f"[!] An error occurred while processing '{file_path}': {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.CYAN + "Usage: python main.py <path_to_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(Fore.RED + "[!] The specified path is not a file or does not exist.")
        sys.exit(1)

    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() == '.ini':
        extract_canarytokens_from_ini(file_path)
    elif file_extension.lower() == '.reg':
        detect_canarytokens_in_reg(file_path)
    elif file_extension.lower() == '.xlsx':
        extract_canarytokens_from_xlsx(file_path)
    elif file_extension.lower() == '.docx':
        extract_canarytokens_from_docx(file_path)
    else:
        print(Fore.RED + "[!] Unsupported file type. Please provide a .ini, .reg, .xlsx, or .docx file.")
