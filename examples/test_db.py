import sqlite3
import db_connect


db_connect.add_planet('earth', 40, 40, 33)
# db_connect.delete_planet_name('moon')


conn = sqlite3.connect('planet.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM planet')
row = cursor.fetchone()
while row is not None:
   print(row[0])
   print(row[1])
   print(row[2])
   print(row[3])
   print(row[4])
   row = cursor.fetchone()
