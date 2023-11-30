from bs4 import BeautifulSoup
import requests

url = "https://www.maryleboneschool.org/parent-newsletter/293.html"

requests.packages.urllib3.disable_warnings()
response = requests.get(url, verify=False)
index_page = BeautifulSoup(response.text, "html.parser")
for link in index_page.find_all('a'):
    print("Link:", link.get('href'))
    print("Text:", link.get_text())
    

