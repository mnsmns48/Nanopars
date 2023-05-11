import time
import requests
from bs4 import BeautifulSoup

from db_model import engine, \
    indicators, \
    smartphone_main, \
    display_model_dict, \
    display, \
    design_and_body_model_dict


def url_generator(link):
    counter = 552
    while counter != 560:
        result = link[counter]
        counter += 1
        yield result


def total_score_value(soup):
    data = dict()
    total_score_model_title = soup.find_all('div', class_='score-bar-name')
    for index in total_score_model_title:
        value = index.find_next('span', class_='score-bar-result-square') \
                or index.find_next('span', class_='score-bar-result-square-dark') \
                or index.find_next('span', class_='score-bar-result-number')
        if value:
            data.update({str(index.text.strip()): value.text.replace('*', '').strip()})
    total_score_model_value_red = soup.find_all('span', class_='score-bar-result-number-review')
    for value in total_score_model_value_red:
        index = value.find_previous('div', class_='score-bar-name')
        data.update({index.text.strip(): value.text.replace('*', '').strip()})
    result = data.keys() - indicators.keys()
    for key in result:
        data.pop(key)
    return data


def get_smartphone_main_data(soup):
    title = soup.find('h1', class_="title-h1").text
    brand = soup.find_all('span', class_='breadcrumbs-link')[1].find('a').text.split(' ')[1]
    advantage_ = soup.find('ul', class_='proscons-list two-columns-item').find_all('li')
    advantage = [i.text for i in advantage_]
    disadvantage_ = soup.find_all('ul', class_='proscons-list two-columns-item')[1].find_all('li')
    disadvantage = [i.text for i in disadvantage_]
    final_score = total_score_value(soup).get('Итоговая оценка')
    data = [
        {
            'title': title,
            'brand': brand,
            'advantage': advantage,
            'disadvantage': disadvantage,
            'final_score': final_score
        }
    ]
    # for k, v in data[0].items():
    #     print(k, ':', v)
    # print('----------------------------------------------------------------------------------')
    return data
    # def get_display_data(soup):

    # display_model_title = soup.find_all('table', class_='specs-table')[0].find_all('td', class_='cell-h')
    # display_model_value = soup.find_all('table', class_='specs-table')[0].find_all('td', class_='cell-s')
    # for line, line2 in zip(display_model_title, display_model_value):
    #     if display_model_dict.get(line.text):
    #         locals().update({display_model_dict.get(line.text): line2.text})
    # data.append([{
    #     'title': title,
    #     'brand': brand,
    #     'type': locals().get('type_'),
    #     'size': str(locals().get('size')).split(' ')[0],
    #     'resolution': str(locals().get('resolution')).rsplit(' ', maxsplit=1)[0],
    #     'ratio': locals().get('ratio'),
    #     'pixel_density': str(locals().get('pixel_density')).split(' ')[0],
    #     'frequency': str(locals().get('frequency')).split(' ')[0],
    #     'adaptive_refresh_rate': True if locals().get('adaptive_refresh_rate') == 'Да' else False,
    #     'max_brightness': str(locals().get('max_brightness')).split(' ')[0],
    #     'hdr_suport': False if locals().get('hdr_suport') == 'Нет' else True,
    #     'display_protection': locals().get('display_protection'),
    #     'display_total_score': final_score[0]
    # }])
    # design_and_body_model_title = soup.find_all('table', class_='specs-table')[1].find_all('td', class_='cell-h')
    # design_and_body_model_value = soup.find_all('table', class_='specs-table')[1].find_all('td', class_='cell-s')
    # for line, line2 in zip(design_and_body_model_title, design_and_body_model_value):
    #     if design_and_body_model_dict.get(line.text):
    #         locals().update({design_and_body_model_dict.get(line.text): line2.text})
    # screen_to_body_ratio = soup.find_all('div', class_='score-bar-name')
    # data.append([{
    #     'title': title,
    #     'brand': brand,
    #     'height': str(locals().get('height')).split(' ')[0],
    #     'wight': str(locals().get('wight')).split(' ')[0],
    #     'thickness': str(locals().get('thickness')).split(' ')[0],
    #     'weight': str(locals().get('weight')).split(' ')[0],
    #     'waterproof': False if locals().get('waterproof') == 'Нет' else True,
    #     'fingerprint_scanner': locals().get('fingerprint_scanner'),
    #     'backpanel_material': locals().get('backpanel_material'),
    #     'frame_material': locals().get('frame_material'),
    #     'colors': locals().get('colors'),
    #     'screen_to_body_ratio': 'в процессе'
    # }])
    # print(screen_to_body_ratio)
    # return data
    # for k,v in data[0][0].items():
    #     print(k, ':', v)
    # print('-------------')
    # for k,v in data[2][0].items():
    #     print(k, ':', v)
    # concatenated_data_block = soup.find_all('table', class_='specs-table')[1].find_all('td', class_='cell-s')
    # height = concatenated_data_block.text.split(' ')[0]
    # wight = concatenated_data_block[1].text.split(' ')[0]
    # thickness = concatenated_data_block[2].text.split(' ')[0]
    # weight = concatenated_data_block[3].text.split(' ')[0]
    # waterproof = False if concatenated_data_block[4].text.split(' ')[0] == 'Нет' else True
    # fingerprint_scanner = str()
    # data.append([{
    #     'title': title,
    #     'brand': brand,
    #     'height': height,
    #     'wight': wight,
    #     'thickness': thickness,
    #     'weight': weight
    #
    # }])




def start():
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                   'Safari/537.36 OPR/98.0.0.0'}
    with open('card_list.txt', 'r') as card_file:
        result_reading = card_file.read()
        card_url_list_ = result_reading.split('\n')
    for card_url in url_generator(card_url_list_):
        response = requests.get(card_url, headers=headers)
        soup_ = BeautifulSoup(response.text, 'lxml')
        get_smartphone_main_data(soup_)
        with engine.connect() as conn:
            smartphone_main_query = smartphone_main.insert().values(get_smartphone_main_data(soup_))
            conn.execute(smartphone_main_query)
            conn.commit()
        time.sleep(3)


if __name__ == "__main__":
    start()
