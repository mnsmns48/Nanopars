from sqlalchemy import create_engine, MetaData, Text, Integer, Table, Column, ARRAY, Float, Boolean, \
    SmallInteger, VARCHAR, select, text
from sqlalchemy.orm import Session

engine = create_engine('postgresql+psycopg2://baza:baza534@localhost:5432/phones',
                       echo=True)

metadata = MetaData()

smartphone_main = Table('smartphone_main', metadata,
                        Column('title', VARCHAR(40), primary_key=True),
                        Column('brand', VARCHAR(10)),
                        Column('advantage', ARRAY(Text), nullable=True),
                        Column('disadvantage', ARRAY(Text), nullable=True),
                        Column('final_score', SmallInteger)
                        )

display = Table('display', metadata,
                Column('title', VARCHAR(40), primary_key=True),
                Column('brand', VARCHAR(10)),
                Column('type', VARCHAR(15)),
                Column('size', Float, nullable=True),
                Column('resolution', VARCHAR(10), nullable=True),
                Column('ratio', VARCHAR(10), nullable=True),
                Column('pixel_density', SmallInteger, nullable=True),
                Column('frequency', SmallInteger, nullable=True),
                Column('adaptive_refresh_rate', Boolean, nullable=True),
                Column('max_brightness', SmallInteger, nullable=True),
                Column('hdr_suport', Boolean, nullable=True),
                Column('display_protection', VARCHAR(20), nullable=True),
                Column('display_total_score', SmallInteger)
                )
display_model_dict = {
    'Тип': 'type_',
    'Размер': 'size',
    'Разрешение': 'resolution',
    'Соотношение сторон': 'ratio',
    'Плотность пикселей': 'pixel_density',
    'Частота обновления': 'frequency',
    'Адаптивная частота обновления': 'adaptive_refresh_rate',
    'Макс. заявленная яркость': 'max_brightness',
    'Поддержка HDR': 'hdr_suport',
    'Защита дисплея': 'display_protection'
}

design_and_body = Table('design_and_body', metadata,
                        Column('title', VARCHAR(40), primary_key=True),
                        Column('brand', VARCHAR(10)),
                        Column('height', Float, nullable=True),
                        Column('wight', Float, nullable=True),
                        Column('thickness', Float, nullable=True),
                        Column('weight', Float, nullable=True),
                        Column('waterproof', Boolean, nullable=True),
                        Column('fingerprint_scanner', VARCHAR(15), nullable=True),
                        Column('backpanel_material', VARCHAR(10), nullable=True),
                        Column('frame_material', VARCHAR(10), nullable=True),
                        Column('colors', ARRAY(Text)),
                        Column('screen_to_body_ratio', VARCHAR(10), nullable=True)
                        )
design_and_body_model_dict = {
    'Высота': 'height',
    'Ширина': 'wight',
    'Толщина': 'thickness',
    'Вес': 'weight',
    'Водонепроницаемость': 'waterproof',
    'Сканер отпечатков пальцев': 'fingerprint_scanner',
    'Материал задней панели': 'backpanel_material',
    'Материал рамки': 'frame_material',
    'Доступные цвета': 'colors',
}

performance = Table('performance', metadata,
                    Column('title', VARCHAR(40), primary_key=True),
                    Column('brand', VARCHAR(10)),
                    Column('chipset', VARCHAR(20), nullable=True),
                    Column('frequency', SmallInteger, nullable=True),
                    Column('architecture', ARRAY(Text), nullable=True),
                    Column('transistor_size', SmallInteger, nullable=True),
                    Column('graphics_chip', VARCHAR(20), nullable=True),
                    Column('graphics_frequency', SmallInteger, nullable=True),
                    Column('flops', SmallInteger, nullable=True),
                    Column('geekbench_singlecore', SmallInteger, nullable=True),
                    Column('geekbench_multicore', SmallInteger, nullable=True),
                    Column('antutu', Integer, nullable=True),
                    Column('performance_total_score', SmallInteger)
                    )

ram = Table('ram', metadata,
            Column('title', VARCHAR(40), primary_key=True),
            Column('brand', VARCHAR(10), nullable=True),
            Column('volume', ARRAY(SmallInteger), nullable=True),
            Column('type', VARCHAR(10), nullable=True)
            )

storage = Table('storage', metadata,
                Column('title', VARCHAR(40), primary_key=True),
                Column('brand', VARCHAR(10)),
                Column('volume', ARRAY(SmallInteger), nullable=True),
                Column('memorycard', Boolean, nullable=True),
                Column('max_volume_card', SmallInteger, nullable=True)
                )

software = Table('software', metadata,
                 Column('title', VARCHAR(40), primary_key=True),
                 Column('brand', VARCHAR(10)),
                 Column("operating_system", VARCHAR(15), nullable=True),
                 Column("shell_ui", VARCHAR(15), nullable=True),
                 Column("system_size", Float, nullable=True)
                 )

battery = Table('battery', metadata,
                Column('title', VARCHAR(40), primary_key=True),
                Column('brand', VARCHAR(10)),
                Column("charging_power", SmallInteger, nullable=True),
                Column("wireless_charge", Boolean, nullable=True),
                Column("reverse_charge", Boolean, nullable=True),
                Column("fast_charge", VARCHAR(40), nullable=True),
                Column("time_full_charge", VARCHAR(10), nullable=True)
                )

main_camera = Table('main_camera', metadata,
                    Column('title', VARCHAR(40), primary_key=True),
                    Column('brand', VARCHAR(10)),
                    Column("matrix", SmallInteger, nullable=True),
                    Column("_8k_video_rec", VARCHAR(20), nullable=True),
                    Column("_4k_video_rec", VARCHAR(20), nullable=True),
                    Column("_fullhd_video_rec", VARCHAR(20), nullable=True),
                    Column("lenses", VARCHAR(40), nullable=True),
                    Column("primary_lens", ARRAY(Text), nullable=True),
                    Column("camera_total_score", SmallInteger)
                    )

selfie_camera = Table('selfie_camera', metadata,
                      Column('title', VARCHAR(40), primary_key=True),
                      Column('brand', VARCHAR(10)),
                      Column("matrix", SmallInteger, nullable=True),
                      Column("aperture", Float, nullable=True),
                      Column("video_rec_resolution", VARCHAR(40), nullable=True)
                      )

communications = Table('communications', metadata,
                       Column('title', VARCHAR(40), primary_key=True),
                       Column('brand', VARCHAR(10)),
                       Column("sim_count", SmallInteger, nullable=True),
                       Column("eSIM_support", Boolean, nullable=True),
                       Column("hybrid_sim_slot", Boolean, nullable=True),
                       Column("wifi_version", VARCHAR(40), nullable=True),
                       Column("bt_version", Float, nullable=True),
                       Column("usb_type", VARCHAR(10), nullable=True),
                       Column("gps", VARCHAR(40), nullable=True),
                       Column("nfc", Boolean, nullable=True),
                       Column("_5g_support", Boolean, nullable=True),
                       Column("communications_total_score", SmallInteger)
                       )

sound = Table('sound', metadata,
              Column('title', VARCHAR(40), primary_key=True),
              Column('brand', VARCHAR(10)),
              Column("speakers", VARCHAR(10), nullable=True),
              Column("_3_5mm_port", Boolean, nullable=True)
              )

other = Table('other', metadata,
              Column('title', VARCHAR(40), primary_key=True),
              Column('brand', VARCHAR(10)),
              Column("_class", VARCHAR(20), nullable=True),
              Column("release_date", VARCHAR(30), nullable=True),
              Column("sales_start_day", VARCHAR(30), nullable=True),
              Column("head_sar_radiation", Float, nullable=True),
              Column("body_sar_radiation", Float, nullable=True),
              Column("contents_delivery", ARRAY(Text), nullable=True)
              )
indicators = {
    'Дисплей': 'display_total_score',
    'Камера': 'camera_total_score',
    'Производительность': 'performance_total_score',
    'Батарея': 'battery_total_score',
    'Коммуникации': 'communications_total_score',
    'Итоговая оценка': 'total_score_value',
    'Соотношение экрана к корпусу': 'screen_to_body_ratio',
    'Geekbench 5 (одноядерный)': 'geekbench_singlecore',
    'Geekbench 5 (многоядерный)': 'geekbench_multicore',
    'AnTuTu Benchmark 9': 'antutu'
}

# with engine.connect() as conn:
#     insert_query = smartphone_main.insert().values(
#         [
#             {'title': 'Samsung A55',
#              'brand': 'Samsung',
#              'advantage': ["nnn", "mmmm"],
#              'disadvantage': ["dsfsdf", "mfdgsdfgmmm"],
#              'final_score': 5}
#         ]
#     )
#     conn.execute(insert_query)
#     conn.commit()


# with engine.connect() as conn:
#     result = smartphone_main.c.title
#     print(result)

# with Session(engine) as sess:
#     result = sess.execute(
#         select(smartphone_main.c.final_score).where(smartphone_main.c.title == 'Samsung A55'))
#     print(result.scalar())
