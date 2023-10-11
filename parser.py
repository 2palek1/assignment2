import json
import requests
import bs4
import re


print("Hello! This program is created to parse apartments in Astana, Esil district")
min_r = input("minimum number of rooms: ")
max_r = input("maximum number of rooms: ")
max_p = input("maximum price of apartments: ")


# Creating url address with input data and Sending request
url = f"https://krisha.kz/arenda/kvartiry/astana-esilskij/?das[live.rooms][]={min_r}&das[live.rooms][]={max_r}&das[price][to]={max_p}"
r = requests.get(url)


# Getting html  from url
soup = bs4.BeautifulSoup(r.text, 'lxml')

# Creating lists with parsed data
raw_titles = [re.sub(r'[\n\xa0]', '', title.text) for title in soup.select(".a-card__header-left")]
raw_prices = [re.sub(r'[\n\xa0 ]', '', price.text) for price in soup.select(".a-card__price")]
raw_address = [re.sub(r'[\n\xa0]', '', address.text).strip() for address in soup.select(".a-card__subtitle")]
raw_links = [elem["data-id"] for elem in soup.findAll('div', {"data-id": True})]


offers = []

# Creating list of dictionaries
for i in range(len(raw_titles)):
    offer = {
        "title": raw_titles[i],
        "price": raw_prices[i],
        "address": raw_address[i],
        "id": raw_links[i],
        "link": f"https://krisha.kz/a/show/{raw_links[i]}"
    }
    offers.append(offer)

# Creating JSON file in working directory
with open("offers.json", "w") as out:
    json.dump(offers, out, ensure_ascii=False, indent=4)