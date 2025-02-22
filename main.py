import re
import sys
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def extract_canarytokens_from_ini(file_path):
    """
    Extracts and prints Canarytoken URLs from a .ini file.
    """
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
    """
    Detects occurrences of '.canarytokens.com' in a .reg file.
    """
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
    else:
        print(Fore.RED + "[!] Unsupported file type. Please provide a .ini or .reg file.")
