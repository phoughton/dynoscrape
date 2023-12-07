from bs4 import BeautifulSoup
import requests
import json
from unidecode import unidecode


url_base = "https://www.maryleboneschool.org"
url_index_path = "/parent-newsletter/293.html"


def get_index_data():
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url_base + url_index_path, verify=False)
    index_page = BeautifulSoup(response.text, "html.parser")
    
    all_index = []
    
    for dated_div in index_page.find_all('div', {'class': 'jp-details'}):
        sub_url_name = dated_div.get_text().strip().replace("\n", " ")
        sub_url_path = dated_div.find('a').get('href')
        item_data = {}
        item_data["name"] = sub_url_name
        item_data["path"] = sub_url_path
        all_index.append(item_data)

    return all_index


def get_newsletter_data(full_url):
    requests.packages.urllib3.disable_warnings()
    nl_response = requests.get(full_url, verify=False)
    nl_content = BeautifulSoup(nl_response.text, "html.parser")
    all_text = [unidecode(text) for text in nl_content.stripped_strings]
    return all_text


the_index = get_index_data()
print(json.dumps(the_index, indent=4))
print()
a_page = get_newsletter_data(the_index[0]["path"])
print(a_page)
