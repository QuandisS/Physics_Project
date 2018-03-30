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
earth = planet('Earth', 'test', 'test', 'test')
moon = planet('Moon', 'test', 'test', 'test')
mars = planet('Mars', 'test', 'test', 'test')

#Объекты#
rock = object('test', 'test', 'test', 'test')

planets = {}
planets.update({'Earth' : earth})
planets.update({'Moon': moon})
planets.update({'Mars': mars})



print(planets)