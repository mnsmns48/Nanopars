import time

import requests
from bs4 import BeautifulSoup

url_ = 'https://nanoreview.net/ru/phone/lg-v20'
with open('card_list.txt', 'r') as file:
    a = file.read().split('\n')
count = 0
for i in a:
    if i != url_:
        count += 1
    if i == url_:
        print(count)


# def check_new():
#     with open('url_list.txt', 'r') as f:
#         file = f.read().split('\n')
#     for url in file:
#         yield url
#
#
# def find_new_items(url):
#     headers = {'User-Agent':
#                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
#                    'Safari/537.36 OPR/98.0.0.0'}
#     response = requests.get(url=url, headers=headers)
#     soup_ = BeautifulSoup(response.text, 'lxml')
#     links = soup_.find_all('a', style='font-weight:500;')
#     for line in links:
#         print(line.get('href'))
#
# for url_ in check_new():
#     find_new_items(url_)
#     time.sleep(100)