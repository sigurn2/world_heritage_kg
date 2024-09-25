import time

from bs4 import BeautifulSoup
import requests

selector = '#content > div > div:nth-child(4) > div > div.col-12.col-lg-8.mb-4.mb-lg-0 > div > div:nth-child(4)'


def crawler(nid: int):
    url = f"https://whc.unesco.org/en/list/{nid}"
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')
            content = soup.select(selector)
            return content[0].get_text()
        else:
            time.sleep(10)
            continue
