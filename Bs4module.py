from bs4 import BeautifulSoup
import requests

url = "https://www.google.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Find and print all link tags instead
for link in soup.find_all("a"):
    print(link.get('href'))