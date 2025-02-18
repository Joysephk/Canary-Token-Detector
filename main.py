import re
import sys

# Function to extract Canarytoken URLs from an .ini file
def extract_canarytokens(file_path):
    # Regex pattern to match the Canarytoken URLs
    pattern = re.compile(r"\\%USERNAME%\.\%COMPUTERNAME%\.\%USERDOMAIN%\.INI\.\w+\.canarytokens\.com\\resource\.dll")
    
    try:
        # Open and read the file
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            
            # Find all matches in the file content
            matches = pattern.findall(content)
            
            if matches:
                print("[+] Detected Canarytokens URLs:")
                for match in matches:
                    print(match)
            else:
                print("[-] No Canarytokens URLs found.")
    except FileNotFoundError:
        print("[!] File not found. Check the file path.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

# Main function to handle command-line arguments
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_ini_file>")
        sys.exit(1)
    
    extract_canarytokens(sys.argv[1])
