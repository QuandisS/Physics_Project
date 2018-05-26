import sqlite3

def add_planet (name, mass, radius, average_density):
    conn = sqlite3.connect('planet.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO planet (name, mass, radius, average_density) VALUES ('%s', '%f', '%f', '%f')"%(name, mass, radius, average_density))
    conn.commit()
    conn.close()
#
# def delete_planet_name (name):
#     conn = sqlite3.connect('planet.db')
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM planet WHERE name = name")
#     conn.commit()
#     conn.close()
#
