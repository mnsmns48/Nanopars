import requests
from bs4 import BeautifulSoup

from main import headers, write_in_db

print('Введите ссылку')
one_url = str(input())
response = requests.get(one_url, headers=headers, timeout=3)
soup_ = BeautifulSoup(response.text, 'lxml')
write_in_db(soup_)
with open('card_list.txt', 'a') as file_:
    file_.write(one_url)
    file_.write('\n')
