import time
import requests
from bs4 import BeautifulSoup

with open('card_list.txt', 'r') as card_file:
    result_reading = card_file.read()
    card_url_list_ = result_reading.split('\n')


def url_generator(link):
    counter = 0
    while counter != 20:
        result = link[counter]
        counter += 1
        yield result


def find_final_score_value(soup_):
    try:
        result = soup_.find_all('span', class_='score-bar-result-number-review')[1]
    except IndexError:
        result = soup_.find('span', class_='score-bar-result-square-dark')
    print(result.text)


def get_data(link: str):
    data = list()
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                   'Safari/537.36 OPR/98.0.0.0'}
    result = requests.get(link, headers=headers)
    soup = BeautifulSoup(result.text, 'lxml')
    title = soup.find('h1', class_="title-h1").text
    brand = soup.find_all('span', class_='breadcrumbs-link')[1].find('a').text.split(' ')[1]
    # advantage_ = soup.find('ul', class_='proscons-list two-columns-item').find_all('li')
    # advantage = [i.text for i in advantage_]
    # disadvantage_ = soup.find_all('ul', class_='proscons-list two-columns-item')[1].find_all('li')
    # disadvantage = [i.text for i in disadvantage_]
    final_score = find_final_score_value(soup)
    # print(title)
    # print(brand)
    # print(advantage)
    # print(disadvantage)
    # data.append({'title': title})


for card_url in url_generator(card_url_list_):
    get_data(card_url)
    time.sleep(10)
