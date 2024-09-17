from sqlalchemy.orm import Session

from db_tables import engine, physical_parameters, temp_table, metadata, s_main, display, performance, camera, energy, \
    communication

# create session object #
# session = Session(bind=engine)

# make a list with the necessary data for replacement #
# physical_parameters_ = session.query(physical_parameters).all()
# update_map = []
# for line in physical_parameters_:
#     update_map.append({'title': line.title, 'brand': line.title.split(' ')[0]})
# create temp table with the rows we want to change(update) #
# temp_table.create(bind=session.get_bind())
# session.execute(temp_table.insert().values(update_map))

# change the data in the required tables #
# session.execute(s_main
#                 .update()
#                 .values(brand=temp_table.c.brand)
#                 .where(s_main.c.title == temp_table.c.title))
# session.execute(display
#                 .update()
#                 .values(brand=temp_table.c.brand)
#                 .where(display.c.title == temp_table.c.title))
# session.execute(performance
#                 .update()
#                 .values(brand=temp_table.c.brand)
#                 .where(performance.c.title == temp_table.c.title))
# session.execute(camera.update()
#                 .values(brand=temp_table.c.brand)
#                 .where(camera.c.title == temp_table.c.title))
# session.execute(energy
#                 .update()
#                 .values(brand=temp_table.c.brand)
#                 .where(energy.c.title == temp_table.c.title))
# session.execute(communication
#                 .update()
#                 .values(brand=temp_table.c.brand)
#                 .where(communication.c.title == temp_table.c.title))

# drop temp table #
# temp_table.drop(bind=session.get_bind())
# session.commit()
