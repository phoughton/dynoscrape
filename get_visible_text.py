from bs4 import BeautifulSoup
import requests

url_base = "https://www.maryleboneschool.org"
url_index_path = "/parent-newsletter/293.html"

all_data = {}

requests.packages.urllib3.disable_warnings()
response = requests.get(url_base + url_index_path, verify=False)
index_page = BeautifulSoup(response.text, "html.parser")

print()

for dated_div in index_page.find_all('div', {'class': 'jp-details'}):
    sub_url_name = dated_div.get_text()
    sub_url_path = dated_div.find('a').get('href')
    print()
    all_data[sub_url_name] = {}
    all_data[sub_url_name]["path"] = sub_url_path

    # nl_response = requests.get(url_base + nl_link, verify=False)
    # all_data[nl_link]["content"] = BeautifulSoup(nl_response.text, "html.parser")

print(all_data)
