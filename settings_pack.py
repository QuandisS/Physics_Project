############################################
# Это файл, содержащий настройки значений  #
############################################

# Настройка и вывод в лог #

version = 'Pre-Alpha Build'

# ------------------------#



# Классы Настроек #

class planet:
    def __init__(self, name, radius, average_density, mass):
        self.radius = radius
        self.average_density = average_density
        self.mass = mass
        self.name = name

class object:
    def __init__(self, mass, capacity, average_density, form):
        self.mass = mass
        self.capacity = capacity
        self.average_density = average_density
        self.form = form
#_____________________#

# Назначение в объект #


#Планеты#
earth = planet('Earth', 6371, 5515.3, 5.9726 * pow(10, 24))
moon = planet('Moon',  1731.1, 3346.4, 7.3477 * pow(10, 22))
mars = planet('Mars', 3389.5, 3933, 6.4171 * pow(10, 23))

#Объекты#
rock = object('test', 'test', 'test', 'test')

planets = {}
planets.update({'Earth' : earth})
planets.update({'Moon': moon})
planets.update({'Mars': mars})



print(planets)