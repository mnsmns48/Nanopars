import time

with open('card_list.txt', 'r') as file:
    a = file.read().split('\n')
count = 0
for i in a:
    if i != 'https://nanoreview.net/ru/phone/samsung-galaxy-s23-plus':
        count += 1
    if i == 'https://nanoreview.net/ru/phone/samsung-galaxy-s23-plus':
        print(count)