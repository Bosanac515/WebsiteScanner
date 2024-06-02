This is a simple python file to vulnerability scan websites that can run in the terminal on Mac/Windows

**WARNING**
DON'T vulnerability scan websites without EXPRESS PERMISSION.

**To use the program**
PREREQ: 
- Python 3 installed.
- Run this in terminal to install neccessary API's: pip3 install requests beautifulsoup4 pandas fpdf

1. Start by navigating to file for ex: cd path/to/extracted/directory
2. Then call program with: python3 vuln_scanner.py
3. You input a site and it will format it correctly.
4. You confirm its correct.
5. Then the program will run it through 50 common vulnerabilities.
6. It will then finish up and ask to run any other sites.
7. YES option: it will reset you to step 1.
8. NO option: it will output the results of your time scanning.
9. It will then ask to export if you want.
10. YES option: program asks to export to excel or pdf.
11. It will then be in your downloads or desktop folder in the chosen file format.
12. NO option: program ends.

