import requests
from bs4 import BeautifulSoup

from proxy import proxies
import json


# url = 'https://www.skiddle.com/festivals/'

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# req = requests.get(url, headers=headers)

# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(req.text)

# with open('index.html', encoding='utf-8') as file:
#     src = file.read()

# soup = BeautifulSoup(src, 'lxml')

links = []

for i in range(0, 25, 24):
    url = f'https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=29%20Jan%202024&to_date=&maxprice=500&o={
        i}&bannertitle=July'
    req = requests.get(url, headers=headers, proxies=proxies)
    json_data = json.loads(req.text)
    html_response = json_data['html']

    with open(f"data/index_{i}.html", 'w', encoding='utf-8') as file:
        file.write(html_response)

    with open(f"data/index_{i}.html", encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('a', class_='card-details-link')
    for item in cards:
        links.append('https://www.skiddle.com' + item.get('href'))


for url in links:
    req = requests.get(url, headers=headers, proxies=proxies)
    try:
        soup = BeautifulSoup(req.text, 'lxml')
    except Exception as ex:
        print(ex)

    header = soup.find(class_='MuiContainer-root').find('h1',
                                                        class_='MuiTypography-root').text.strip()
