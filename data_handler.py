# def dict_handler(*args):
#     count = len(*args)
#     for i in range(count-1):
#         for k, v in args[i].items():
#             if v[1] == int:
#                 print(v[0].split(' ', 1)[0])
#             if v[1] == list:
#                 print(v[0].split(sep=v[2])[1:])
# if args[0] == int:
#     print(args.values()[0].split(' ')[0])
# if args[0] == list:
#     print(data)
from db_models import month, processing_model


# 'Итоговая оценка': ['total_score', None],
# 'Дата выхода': ['announced', 'datecorr'],
# 'Дата начала продаж': ['release_date', 'datecorr']


def data_handler(*args):
    for i in range(1):
        for k, v in args[i].items():
            if v[1] in processing_model.keys():
                print(processing_model.get(v[1])(v[0]))


m = {
    'Тип': ['300 раз', 'to_int'],

    'Производительность': ['89', 'None'],
    'Реальная пиковая яркость (авто)': ['1204 нит', 'to_int'],
    'Geekbench 5 (одноядерный)': ['1543', 'None'],
    'Geekbench 5 (многоядерный)': ['5025', 'None'],
    'Дата выйхода': ['Февраль 2023 года', 'datecorr'],
    'Разрешение': ['1080 x 2340 пикселей', 'rsplit_str'],
    'Адаптивная частота обновления': ['Нет', 'to_bool'],
    'Соотношение экрана к корпусу': ['88.9%', '%'],
    'Особенности': ['- DCI-P3 - Always-On Display', '- '],
    'Цветовой охват sRGB': ['97.4%', '%'],
    'Объем ОЗУ': ['16, 8, 14 ГБ', 'int_list'],
    'Архитектура': ['- 3 ядра по 2 ГГц: Cortex-A510- 2 ядра по 2.8 ГГц: Cortex-A710- 2 ядра по 2.8 ГГц: Cortex-A715- 1 ядро по 3.2 ГГц: Cortex-X3', '- '],
    'Разрешение фото': ['8160 x 6120', 'None'],
    'Основной объектив': ['- 50 МП - Апертура: f/1.8 - Фокусное расстояние: 23 мм - Размер пикселя: 1 микрон - '
                          'Сенсор: 1/1.57, Samsung S5KGN3 (ISOCELL Plus CMOS) - Фазовый автофокус (Dual Pixel) - '
                          'Оптическая стабилизация', '- '],
    'Разрешение фото -2-': ['- Эффект "боке" - Режим "Pro" - Поддержка RAW', '- '],
}

data_handler(m)
#
#
# for k, v in m.items():
#     print(k, ':', v)
