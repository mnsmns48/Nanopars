from db_models import month


def dict_c(dict_data: dict) -> dict:
    if dict_data.get('Дисплей'):
        dict_data['Дисплей'] = int(dict_data.get('Дисплей'))
    if dict_data.get('Камера'):
        dict_data['Камера'] = int(dict_data.get('Камера'))
    if dict_data.get('Производительность'):
        dict_data['Производительность'] = int(dict_data.get('Производительность'))
    if dict_data.get('Игры'):
        dict_data['Игры'] = int(dict_data.get('Игры'))
    if dict_data.get('Батарея'):
        dict_data['Батарея'] = int(dict_data.get('Батарея'))
    if dict_data.get('Коммуникации'):
        dict_data['Коммуникации'] = int(dict_data.get('Коммуникации'))
    if dict_data.get('Итоговая оценка'):
        dict_data['Итоговая оценка'] = int(dict_data.get('Итоговая оценка'))
    if dict_data.get('AnTuTu Benchmark 9'):
        dict_data['AnTuTu Benchmark 9'] = int(dict_data.get('AnTuTu Benchmark 9'))
    if dict_data.get('Количество каналов'):
        dict_data['Количество каналов'] = int(dict_data.get('Количество каналов'))
    if dict_data.get('Соотношение экрана к корпусу'):
        dict_data['Соотношение экрана к корпусу'] = float(dict_data.get('Соотношение экрана к корпусу').split('%')[0])
    if dict_data.get('Размер'):
        dict_data['Размер'] = float(dict_data.get('Размер').split(' ')[0])
    if dict_data.get('Разрешение'):
        dict_data['Разрешение'] = dict_data.get('Разрешение').rsplit(' ', 1)[0]
    if dict_data.get('Плотность пикселей'):
        dict_data['Плотность пикселей'] = int(dict_data.get('Плотность пикселей').split(' ', 1)[0])
    if dict_data.get('Частота обновления'):
        dict_data['Частота обновления'] = int(dict_data.get('Частота обновления').split(' ', 1)[0])
    if dict_data.get('Адаптивная частота обновления'):
        dict_data['Адаптивная частота обновления'] = False if dict_data.get(
            'Адаптивная частота обновления') == 'Нет' else True
    if dict_data.get('Макс. заявленная яркость'):
        dict_data['Макс. заявленная яркость'] = int(dict_data.get('Макс. заявленная яркость').split(' ')[0])
    if dict_data.get('Макс. заявленная яркость в HDR'):
        dict_data['Макс. заявленная яркость в HDR'] = int(dict_data.get('Макс. заявленная яркость в HDR').split(' ')[0])
    if dict_data.get('Реальная пиковая яркость (авто)'):
        dict_data['Реальная пиковая яркость (авто)'] = int(
            dict_data.get('Реальная пиковая яркость (авто)').split(' ')[0])
    if dict_data.get('Особенности'):
        dict_data['Особенности'] = dict_data.get('Особенности').replace('-', '').strip().split('  ')
    if dict_data.get('Высота'):
        dict_data['Высота'] = float(dict_data.get('Высота').split(' ', 1)[0])
    if dict_data.get('Ширина'):
        dict_data['Ширина'] = float(dict_data.get('Ширина').split(' ', 1)[0])
    if dict_data.get('Толщина'):
        dict_data['Толщина'] = float(dict_data.get('Толщина').split(' ', 1)[0])
    if dict_data.get('Вес'):
        dict_data['Вес'] = float(dict_data.get('Вес').split(' ', 1)[0])
    if dict_data.get('Размер системы из коробки'):
        dict_data['Размер системы из коробки'] = float(dict_data.get('Размер системы из коробки').split(' ', 1)[0])
    if dict_data.get('Максимальная громкость'):
        dict_data['Максимальная громкость'] = float(dict_data.get('Максимальная громкость').split(' ', 1)[0])
    if dict_data.get('Цветовой охват sRGB'):
        dict_data['Цветовой охват sRGB'] = float(dict_data.get('Цветовой охват sRGB').split('%', 1)[0])
    if dict_data.get('Доступные цвета'):
        dict_data['Доступные цвета'] = dict_data.get('Доступные цвета').replace(' ', '').split(',')
    if dict_data.get('Макс. частота'):
        dict_data['Макс. частота'] = int(dict_data.get('Макс. частота').split(' ', 1)[0])
    if dict_data.get('ШИМ (PWM)'):
        dict_data['ШИМ (PWM)'] = int(dict_data.get('ШИМ (PWM)').split(' ', 1)[0])
    if dict_data.get('Время отклика'):
        dict_data['Время отклика'] = int(dict_data.get('Время отклика').split(' ', 1)[0])
    if dict_data.get('Кэш L3'):
        dict_data['Кэш L3'] = int(dict_data.get('Кэш L3').split(' ', 1)[0])
    if dict_data.get('Stability'):
        dict_data['Stability'] = int(dict_data.get('Stability').split('%', 1)[0])
    if dict_data.get('Graphics test'):
        dict_data['Graphics test'] = int(dict_data.get('Graphics test').split(' ', 1)[0])
    if dict_data.get('Архитектура'):
        dict_data['Архитектура'] = dict_data.get('Архитектура').strip().split('- ')[1:]
    if dict_data.get('Размер транзистора'):
        dict_data['Размер транзистора'] = int(dict_data.get('Размер транзистора').split(' ', 1)[0])
    if dict_data.get('Частота GPU'):
        dict_data['Частота GPU'] = int(dict_data.get('Частота GPU').split(' ', 1)[0])
    if dict_data.get('FLOPS'):
        dict_data['FLOPS'] = int(dict_data.get('FLOPS').replace('~', '').split(' ', 1)[0])
    if dict_data.get('Объем ОЗУ'):
        dict_data['Объем ОЗУ'] = [int(i) for i in dict_data.get('Объем ОЗУ').replace(' ГБ', '').split(',')]
    if dict_data.get('Объем накопителя'):
        dict_data['Объем накопителя'] = [int(i) for i in
                                         dict_data.get('Объем накопителя').replace(' ГБ', '').split(',')]
    if dict_data.get('Карта памяти'):
        dict_data['Карта памяти'] = False if dict_data.get('Карта памяти') == 'Нет' else True
    if dict_data.get('Объем'):
        dict_data['Объем'] = int(dict_data.get('Объем').split(' ', 1)[0])
    if dict_data.get('Макс. мощность зарядки'):
        dict_data['Макс. мощность зарядки'] = int(dict_data.get('Макс. мощность зарядки').split(' ', 1)[0])
    if dict_data.get('Съемный'):
        dict_data['Съемный'] = False if dict_data.get('Съемный') == 'Нет' else True
    if dict_data.get('Матрица'):
        dict_data['Матрица'] = int(dict_data.get('Матрица').split(' ', 1)[0])
    if dict_data.get('Основной объектив'):
        dict_data['Основной объектив'] = dict_data.get('Основной объектив').split('- ')[1:]
    if dict_data.get('Телефото объектив'):
        dict_data['Телефото объектив'] = dict_data.get('Телефото объектив').split('- ')[1:]
    if dict_data.get('Сверхширокоугольный объектив'):
        dict_data['Сверхширокоугольный объектив'] = dict_data.get('Сверхширокоугольный объектив').split('- ')[1:]
    if dict_data.get('Особенности -2-'):
        dict_data['Особенности -2-'] = dict_data.get('Особенности -2-').split('- ')[1:]
    if dict_data.get('Количество мегапикселей'):
        dict_data['Количество мегапикселей'] = int(dict_data.get('Количество мегапикселей').split(' ', 1)[0])
    if dict_data.get('Фокусное расстояние'):
        dict_data['Фокусное расстояние'] = int(dict_data.get('Фокусное расстояние').split(' ', 1)[0])
    if dict_data.get('Размер пикселя'):
        dict_data['Размер пикселя'] = float(dict_data.get('Размер пикселя').split(' ', 1)[0])
    if dict_data.get('Функции Wi-Fi'):
        dict_data['Функции Wi-Fi'] = dict_data.get('Функции Wi-Fi').split('- ')[1:]
    if dict_data.get('Версия USB'):
        dict_data['Версия USB'] = float(dict_data.get('Версия USB'))
    if dict_data.get('Функции USB'):
        dict_data['Функции USB'] = dict_data.get('Функции USB').split('- ')[1:]
    if dict_data.get('GPS'):
        dict_data['GPS'] = dict_data.get('GPS').split(', ')
    if dict_data.get('NFC*'):
        dict_data['NFC*'] = False if dict_data.get('NFC*') == 'Нет' else True
    if dict_data.get('Инфракрасный порт'):
        dict_data['Инфракрасный порт'] = False if dict_data.get('Инфракрасный порт') == 'Нет' else True
    if dict_data.get('Dolby Atmos'):
        dict_data['Dolby Atmos'] = False if dict_data.get('Dolby Atmos') == 'Нет' else True
    if dict_data.get('Количество SIM*'):
        dict_data['Количество SIM*'] = int(dict_data.get('Количество SIM*'))
    if dict_data.get('Гибридный слот'):
        dict_data['Гибридный слот'] = False if dict_data.get('Гибридный слот') == 'Нет' else True
    if dict_data.get('Поддержка 5G'):
        dict_data['Поддержка 5G'] = False if dict_data.get('Поддержка 5G') is None else True
    if dict_data.get('Поддержка eSIM*'):
        dict_data['Поддержка eSIM*'] = False if dict_data.get('Поддержка eSIM*') is None else True
    if dict_data.get('3.5 мм аудио порт'):
        dict_data['3.5 мм аудио порт'] = False if dict_data.get('3.5 мм аудио порт') == 'Нет' else True
    if dict_data.get('FM-Радио'):
        dict_data['FM-Радио'] = False if dict_data.get('FM-Радио') == 'Нет' else True
    if dict_data.get('Сенсоры и датчики'):
        dict_data['Сенсоры и датчики'] = dict_data.get('Сенсоры и датчики').split('- ')[1:]
    if dict_data.get('Дата выхода'):
        dict_data['Дата выхода'] = dict_data.get('Дата выхода').split(' ')[1] + '-' + month.get(
            dict_data.get('Дата выхода').split(' ')[0])
    if dict_data.get('Дата начала продаж'):
        dict_data['Дата начала продаж'] = dict_data.get('Дата начала продаж').split(' ')[1] \
                                          + '-' + month.get(dict_data.get('Дата начала продаж').split(' ')[0])
    if dict_data.get('Уровень излучения SAR для головы'):
        dict_data['Уровень излучения SAR для головы'] = float(
            dict_data.get('Уровень излучения SAR для головы').split(' ', 1)[0])
    if dict_data.get('Уровень излучения SAR для тела'):
        dict_data['Уровень излучения SAR для тела'] = float(
            dict_data.get('Уровень излучения SAR для тела').split(' ', 1)[0])
    return dict_data
