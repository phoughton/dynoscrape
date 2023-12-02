from bs4 import BeautifulSoup
import requests

url_base = "https://www.maryleboneschool.org"
url_index_path = "/parent-newsletter/293.html"

all_data = {}

requests.packages.urllib3.disable_warnings()
response = requests.get(url_base + url_index_path, verify=False)
index_page = BeautifulSoup(response.text, "html.parser")
for nl_link_a in index_page.find_all('a'):
    nl_link = nl_link_a.get('href')
    all_data[nl_link] = {}
    all_data[nl_link]["link_text"] = nl_link_a.get_text()
    print(url_base + nl_link_a)

    # nl_response = requests.get(url_base + nl_link, verify=False)
    # all_data[nl_link]["content"] = BeautifulSoup(nl_response.text, "html.parser")

print(all_data)
