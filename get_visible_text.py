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


with open("index.json", "w") as f:
    json.dump(get_index_data(), f, indent=4)

with open("index.json", "r") as f:
    the_index = json.load(f)

with open("newsletters.json", "w") as f:
    all_nl = []
    for newsletter in the_index:
        the_nl = get_newsletter_data(newsletter["path"])
        the_nl = "\n".join(the_nl)
        all_nl.append(the_nl)
        
    json.dump(all_nl, f, indent=4)
