############################################
# Это файл, содержащий настройки значений  #
############################################

# Настройка и вывод в лог #

version = 'Pre-Alpha Build'

# ------------------------#



# Классы Настроек #

class planet:
    def __init__(self, radius, average_density, mass):
        self.radius = radius
        self.average_density = average_density
        self.mass = mass

class object:
    def __init__(self, mass, capacity, average_density, form):
        self.mass = mass
        self.capacity = capacity
        self.average_density = average_density
        self.form = form
#_____________________#

# Назначение в объект #


#Планеты#
earth = planet('test', 'test', 'test')

#Объекты#
rock = object('test', 'test', 'test', 'test')

planets = {}
planets.update({'earth' : earth})



print(planets)