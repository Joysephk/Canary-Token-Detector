# Canary Token Detector

## Description
This Python project is designed to detect Canarytoken URLs in various file types, including `.ini` files. It scans files for specific Canarytoken patterns and alerts the user if any are found.

## Features
- Reads and scans files for embedded Canarytoken URLs.
- Uses regex to detect Canarytokens.
- Provides a simple command-line interface for easy usage.

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/canary-token-detector.git
   cd canary-token-detector
   ```
2. Install required dependencies (if any):
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script with the file path as an argument:
```sh
python script.py <path_to_file>
```
Example:
```sh
python script.py sample.inf
```

## Output
- If a Canarytoken is found, the script displays:
  ```
  [+] Detected Canarytokens URLs:
  \\username.computername.userdomain.INI.someid.canarytokens.com\resource.dll
  ```
- If no Canarytoken is found:
  ```
  [-] No Canarytokens URLs found.
  ```

## License
This project is licensed under the MIT License.

## Author
Joseph KANKO

