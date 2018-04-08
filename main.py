import PyQt5, os, time
import core_functions
from prettytable import PrettyTable
from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPixmap
from forms.converted import base_form, credits_form, setting_form, custom_planet
from colorama import init
from colorama import Fore, Back, Style
import settings_pack
import pyqtgraph as pg
import numpy as np
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox



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


###### Variable Settings ############

all_planets = settings_pack.planets


###### Selected Settings ############

selected_planet = settings_pack.earth
selected_speed = 1

#####################################




# Главный Класс #

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = base_form.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('TTTH')
        self.ui.speed_label.setText('speed: x' + str(selected_speed))
        self.ui.planet_label.setText(selected_planet.name + '|')

        self.ui.pushButton_5.clicked.connect(self.draw_plot)

        self.ui.actionCredits.triggered.connect(self.show_credits)
        self.ui.actionGitHub_Page_2.triggered.connect(self.git_page_open)
        self.ui.actionDocumentation.triggered.connect(self.doc_page_open)
        self.ui.actionSettings_Pack.triggered.connect(self.show_settings)
        self.ui.actionSpeed.triggered.connect(self.show_speed)
        self.ui.check_vars.clicked.connect(self.check_vars)
        self.ui.actionCustom_planet_settings.triggered.connect(self.show_custom_settings)
        self.ui.actionExport_log_file.triggered.connect(self.export_log)
        self.ui.actionExport_image_chart.triggered.connect(self.export_img)

        # PLot

    def check_vars(self):
        print('vars is checking...')

        self.ui.speed_label.setText('speed: x' + str(selected_speed))
        self.ui.planet_label.setText(selected_planet.name + '|')
        print('SELECTED PLANET NAME =', selected_planet.name)
        print('SELECTED PLANET MASS =', selected_planet.mass)
        print('SELECTED PLANET RADIUS =', selected_planet.radius)
        print('SELECTED PLANET AVERAGE DENSITY =', selected_planet.average_density)

        print('vars checked!')

    def draw_plot(self):
        L = [0, 1, 2, 3, 4, 5 ,6]
        self.ui.plot = pg.PlotWidget(self.ui.centralwidget)
        self.ui.gridLayout.addWidget(self.ui.plot)
        self.ui.plot.plot(L)
        pass

    def export_log(self):
        QMessageBox.about(self, "Ouch!", "Will be added soon...")

    def export_img(self):
        QMessageBox.about(self, "Ouch!", "Will be added soon...")

    def show_credits(self):
        print('CREDITS CLIKED')
        self.mySubwindow = subwindow()
       # self.mySubwindow.createWindow(500, 400)
        self.mySubwindow.ui = credits_form.Ui_MainWindow()
        self.mySubwindow.ui.setupUi(self.mySubwindow)
        self.mySubwindow.show()

    def show_settings(self):
        print('SETTING CLICKED')
        self.setings_subwind = subwindow()
        self.setings_subwind.ui = setting_form.Ui_MainWindow()
        self.setings_subwind.ui.setupUi(self.setings_subwind)

        def set_planet():
            global selected_planet
            selected_planet = all_planets[self.setings_subwind.ui.return_selected()]
            print('selected planet:', selected_planet)
            self.setings_subwind.close()
            self.ui.speed_label.setText('speed: x' + str(selected_speed))
            self.ui.planet_label.setText(selected_planet.name + '|')
        self.setings_subwind.ui.pushButton.clicked.connect(set_planet)
        self.setings_subwind.show()

        for i in all_planets.keys():
            self.setings_subwind.ui.add_item(i)



    def show_speed(self):
        print('SPEED CLICKED')
        self.setings_subwind = subwindow()
        self.setings_subwind.ui = setting_form.Ui_MainWindow()
        self.setings_subwind.ui.setupUi(self.setings_subwind)
        self.setings_subwind.ui.label.setText('Select Speed:')
        self.setings_subwind.setWindowTitle('Select Speed')

        def set_speed():
            global selected_speed
            selected_speed = self.setings_subwind.ui.return_selected()
            print('selected speed:', selected_speed)
            self.setings_subwind.close()
            self.ui.speed_label.setText('speed: x' + str(selected_speed))
            self.ui.planet_label.setText(selected_planet.name + '|')

        self.setings_subwind.ui.pushButton.clicked.connect(set_speed)
        self.setings_subwind.show()

        self.setings_subwind.ui.add_item('1')
        self.setings_subwind.ui.add_item('0,75')
        self.setings_subwind.ui.add_item('0,5')
        self.setings_subwind.ui.add_item('0,25')

    def show_custom_settings(self):
        print('Custom set. CLICKED')

        def cancel_clicked():
            print('cancel clicked')
            self.setings_subwind.close()
            pass

        def ok_clicked():
            print('ok clicked')
            cust_plnt = settings_pack.planet
            cust_plnt.radius = self.setings_subwind.ui.return_vars()[0]
            cust_plnt.average_density = self.setings_subwind.ui.return_vars()[1]
            cust_plnt.mass = self.setings_subwind.ui.return_vars()[2]
            cust_plnt.name = self.setings_subwind.ui.return_vars()[3]

            global selected_planet
            selected_planet = cust_plnt
            self.check_vars()
            self.setings_subwind.close()

        self.setings_subwind = subwindow()
        self.setings_subwind.ui = custom_planet.Ui_MainWindow()
        self.setings_subwind.ui.setupUi(self.setings_subwind)
        self.setings_subwind.show()
        self.setings_subwind.ui.buttonBox.rejected.connect(cancel_clicked)
        self.setings_subwind.ui.buttonBox.accepted.connect(ok_clicked)

        pass


    def git_page_open(self):
        webbrowser.open('https://github.com/QuandisS/Physics_Project')

    def doc_page_open(self):
        webbrowser.open('https://github.com/QuandisS/Physics_Project/wiki')

class subwindow(QtWidgets.QMainWindow):
    def createWindow(self, WindowWidth, WindowHeight):
        parent = None
        super(subwindow, self).__init__(parent)
        self.resize(WindowWidth, WindowHeight)
        self.show()
        #





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
