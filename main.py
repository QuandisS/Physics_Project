import PyQt5, os, time
import core_functions
from prettytable import PrettyTable
from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPixmap
from forms.converted import base_form
from colorama import init
from colorama import Fore, Back, Style
import settings_pack
import pyqtgraph as pg
import numpy as np



#colorama#
init(autoreset=True)
#--------#

main_version = 'Pre-Alpha Build'

# Запуск, приветствие, версии... #

print("Welcome!\n")

table = PrettyTable()
table.field_names = ['MODULE', 'VERSION']
table.add_row([Fore.GREEN + 'main' + Style.RESET_ALL, main_version])
table.add_row([Fore.GREEN + 'core functions' + Style.RESET_ALL, core_functions.version])
table.add_row([Fore.GREEN + 'base_form' + Style.RESET_ALL, base_form.version])
table.add_row([Fore.GREEN + 'settings pack' + Style.RESET_ALL, settings_pack.version])

print(table, '\n')

#--------------------------------#




# Главный Класс #

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = base_form.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_5.clicked.connect(self.draw_plot)


        # PLot
    def draw_plot(self):
        L = [0, 1, 2, 3, 4, 5 ,6]
        self.ui.plot = pg.PlotWidget(self.ui.centralwidget)
        self.ui.gridLayout.addWidget(self.ui.plot)
        self.ui.plot.plot(L)

        #


# ТЕЛО ПРОГРАММЫ #


# TESTS #

print(Back.GREEN + Fore.WHITE + Style.BRIGHT + 'testing...\n')

print(Back.GREEN + Fore.WHITE + Style.BRIGHT + 'testing settings pack...')
try:
    print('Earth mass:', settings_pack.earth.mass)
    print('Earth average density:', settings_pack.earth.average_density)
    print('Earth radius:', settings_pack.earth.radius)
except Exception:
    print(Back.GREEN + Fore.RED + Style.BRIGHT + 'something went wrong...')
else:
    print(Back.GREEN + Fore.WHITE + Style.BRIGHT + 'test done\n')

print(Back.GREEN + Fore.WHITE + Style.BRIGHT + 'testing functions pack...')
try:
    b = core_functions.response()
except Exception:
    print(Back.GREEN + Fore.RED + Style.BRIGHT + 'something went wrong...')
else:
    if b == True:
        print(Back.GREEN + Fore.WHITE + Style.BRIGHT + 'test done\n')
    else:
        print(Back.GREEN + Fore.RED + Style.BRIGHT + 'something went wrong...')


instr_test = core_functions.return_the_instructions('V')
print(instr_test)


#________________#




# _______________#


# Вызов окна #

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
