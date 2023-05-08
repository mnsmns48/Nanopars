from sqlalchemy import create_engine, MetaData, Text, Integer, Table, Column, ARRAY, Float, Boolean, \
    SmallInteger, VARCHAR

engine = create_engine('postgresql+pg8000://postgres:534534@localhost:5433/phones',
                       echo=True)

metadata = MetaData()

smartphone_main = Table('smartphone_main', metadata,
                        Column('title', VARCHAR(40), primary_key=True),
                        Column('brand', VARCHAR(10)),
                        Column('advantage', ARRAY(Text), nullable=True),
                        Column('disadvantage', ARRAY(Text), nullable=True),
                        Column('final_score', SmallInteger)
                        )

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
                        Column('Colors', ARRAY(Text)),
                        Column('screen_to_body_ratio', VARCHAR(10), nullable=True)
                        )

performance = Table('performance', metadata,
                    Column('title', VARCHAR(40), primary_key=True),
                    Column('brand', VARCHAR(10)),
                    Column('chipset', VARCHAR(20)),
                    Column('frequency', SmallInteger),
                    Column('architecture', ARRAY(Text)),
                    Column('transistor_size', SmallInteger),
                    Column('graphics_chip', VARCHAR(20)),
                    Column('graphics_frequency', SmallInteger),
                    Column('flops', SmallInteger),
                    Column('geekbench_singlecore', SmallInteger),
                    Column('geekbench_multicore', SmallInteger),
                    Column('antutu', Integer),
                    Column('performance_total_score', SmallInteger)
                    )

ram = Table('ram', metadata,
            Column('title', VARCHAR(40), primary_key=True),
            Column('brand', VARCHAR(10)),
            Column('volume', ARRAY(SmallInteger)),
            Column('type', VARCHAR(10))
            )

display = Table('display', metadata,
                Column('title', VARCHAR(40), primary_key=True),
                Column('brand', VARCHAR(10)),
                Column('type', VARCHAR(15)),
                Column('size', Float),
                Column('resolution', VARCHAR(10)),
                Column('ratio', VARCHAR(10)),
                Column("pixel_density", SmallInteger),
                Column("frequency", SmallInteger),
                Column("adaptive_refresh_rate", Boolean),
                Column("max_brightness", SmallInteger),
                Column("hdr_suport", Boolean),
                Column("display_protection", VARCHAR(20)),
                Column("display_total_score", SmallInteger)
                )
storage = Table('storage', metadata,
                Column('title', VARCHAR(40), primary_key=True),
                Column('brand', VARCHAR(10)),
                Column('volume', ARRAY(SmallInteger)),
                Column('memorycard', Boolean),
                Column('max_volume_card', SmallInteger)
                )
software = Table('software', metadata,
                 Column('title', VARCHAR(40), primary_key=True),
                 Column('brand', VARCHAR(10)),
                 Column("operating_system", VARCHAR(15)),
                 Column("shell_ui", VARCHAR(15)),
                 Column("system_size", Float)
                 )






with engine.connect() as conn:
    insert_query = smartphone_main.insert().values(
        [
            {'title': 'Samsung A32',
             'brand': 'Samsung',
             'advantage': ["nnn", "mmmm"],
             'disadvantage': ["dsfsdf", "mfdgsdfgmmm"],
             'final_score': 5}
        ]
    )
    conn.execute(insert_query)
    conn.commit()
