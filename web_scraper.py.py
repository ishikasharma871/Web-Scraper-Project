import requests
from bs4 import BeautifulSoup

url = input("Enter URL: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

for h in headings:
      print(h.get_text(strip=True))