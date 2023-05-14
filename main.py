import time
import requests
from bs4 import BeautifulSoup
from sqlalchemy.exc import IntegrityError

from db_models import main_model, display_model, performance_model, camera_model, energy_model, communication_model, \
    physical_parameters_model, processing_model
from db_tables import engine, \
    s_main, display, performance, camera, energy, communication, physical_parameters


def url_generator(link):
    counter = 626
    while counter != len(link):
        result = link[counter]
        counter += 1
        yield result


def get_data(soup: BeautifulSoup) -> dict:
    data = dict()
    brand = soup.find_all('span', class_='breadcrumbs-link')[1].find('a').text.split(' ')[1]
    title = soup.find('h1', class_="title-h1").text
    data.update({'brand': brand, 'title': title})
    advantage_ = soup.find('ul', class_='proscons-list two-columns-item').find_all('li')
    advantage = [i.text for i in advantage_]
    disadvantage_ = soup.find_all('ul', class_='proscons-list two-columns-item')[1].find_all('li')
    disadvantage = [i.text for i in disadvantage_]
    data.update({'Advantage': advantage, 'Disadvantage': disadvantage})
    total_score_model_title = soup.find_all('div', class_='score-bar-name')
    for index in total_score_model_title:
        value = index.find_next('span', class_='score-bar-result-square') \
                or index.find_next('span', class_='score-bar-result-square-dark') \
                or index.find_next('span', class_='score-bar-result-number')
        if value:
            if index.text.strip() in data.keys():
                index = str(index.text.strip()) + ' -2-'
            else:
                index = index.text.strip()
            data.update({str(index): value.text.replace('*', '').strip()})
    total_score_model_value_red = soup.find_all('span', class_='score-bar-result-number-review')
    for value in total_score_model_value_red:
        index = value.find_previous('div', class_='score-bar-name')
        data.update({index.text.strip(): value.text.replace('*', '').strip()})
    display_data_title = soup.find_all('td', class_='cell-h')
    for index in display_data_title:
        value = index.find_next('td', class_='cell-s')
        if value:
            if index.text.strip() in data.keys():
                index = str(index.text.strip()) + ' -2-'
            else:
                index = index.text.strip()
            data.update({str(index): value.text.strip()})
    return data


def edit_dicts(data: dict, model: dict) -> dict:
    cross_dict_ = dict()
    for key, value in model.items():
        if key in data.keys():
            cross_dict_.update({value[0]: processing_model.get(value[1])(data.get(key))})
    return cross_dict_


def write_in_db(soup: BeautifulSoup) -> None:
    with engine.connect() as conn:
        smartphone_main_query = s_main.insert().values(edit_dicts(get_data(soup), main_model))
        display_query = display.insert().values(edit_dicts(get_data(soup), display_model))
        performance_query = performance.insert().values(edit_dicts(get_data(soup), performance_model))
        camera_query = camera.insert().values(edit_dicts(get_data(soup), camera_model))
        energy_query = energy.insert().values(edit_dicts(get_data(soup), energy_model))
        communication_query = communication.insert().values(edit_dicts(get_data(soup), communication_model))
        physical_parameters_query = physical_parameters.insert().values(
            edit_dicts(get_data(soup), physical_parameters_model))
        try:
            conn.execute(smartphone_main_query)
            conn.execute(display_query)
            conn.execute(performance_query)
            conn.execute(camera_query)
            conn.execute(energy_query)
            conn.execute(communication_query)
            conn.execute(physical_parameters_query)
            conn.commit()
        except IntegrityError:
            pass


def start():
    headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                   'Safari/537.36 OPR/98.0.0.0'}
    with open('card_list.txt', 'r') as card_file:
        result_reading = card_file.read()
        card_url_list_ = result_reading.split('\n')
    for card_url in url_generator(card_url_list_):
        response = requests.get(card_url, headers=headers, timeout=2)
        soup_ = BeautifulSoup(response.text, 'lxml')
        write_in_db(soup_)
        time.sleep(2)


if __name__ == "__main__":
    start()
