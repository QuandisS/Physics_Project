
import PyQt5, os, time
import core_functions
import constants
from prettytable import PrettyTable
from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QPixmap
from forms.converted import base_form, credits_form, setting_form, custom_planet, vars_form
from colorama import init
from colorama import Fore, Back, Style
import settings_pack
import pyqtgraph as pg
import numpy as np
import webbrowser
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
import math



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
global_vars = {}
log_text = ''

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
        self.ui.actionClear_Log.triggered.connect(self.clear_log)
        self.ui.pushButton_6.clicked.connect(self.show_vars)

        self.log_add('Hello, this is log!')

        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap("pics/main_logo.png")))
        self.ui.actionExport_image_chart.setIcon(QtGui.QIcon(QtGui.QPixmap(("pics/if_export-outline_216189.png"))))
        self.ui.actionExport_log_file.setIcon(QtGui.QIcon(QtGui.QPixmap(("pics/if_export-outline_216189.png"))))
        self.ui.actionCustom_planet_settings.setIcon(QtGui.QIcon(QtGui.QPixmap(("pics/if_gnome-globe_22280.png"))))
        self.ui.actionSettings_Pack.setIcon(QtGui.QIcon(QtGui.QPixmap(("pics/if_gnome-globe_22280.png"))))
        self.ui.actionSpeed.setIcon(QtGui.QIcon(QtGui.QPixmap(("pics/if_performance-clock-speed_353431.png"))))
        self.ui.actionCredits.setIcon(QtGui.QIcon(QtGui.QPixmap(("pics/if_file_documents-07_854130.png"))))
        self.ui.actionDocumentation.setIcon(QtGui.QIcon(QtGui.QPixmap(("pics/if_Product-documentation_85540.png"))))
        self.ui.actionGitHub_Page_2.setIcon(QtGui.QIcon(QtGui.QPixmap(("pics/if_mark-github_298822.png"))))
        self.ui.actionClear_Log.setIcon(QtGui.QIcon(QtGui.QPixmap(("pics/if_edit-clear_118917.png"))))

        # PLot
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
        self.solve_the_problem()
        pass

    def export_log(self):
        QMessageBox.about(self, "Ouch!", "Will be added soon...")

    def export_img(self):
        QMessageBox.about(self, "Ouch!", "Will be added soon...")

    def clear_log(self):
        global log_text
        log_text = ''
        self.log_add('')
        QMessageBox.about(self, "Done!", "Log cleared...")
        pass

    def show_credits(self):
        print('CREDITS CLIKED')
        self.mySubwindow = subwindow()
       # self.mySubwindow.createWindow(500, 400)
        self.mySubwindow.ui = credits_form.Ui_MainWindow()
        self.mySubwindow.ui.setupUi(self.mySubwindow)
        self.mySubwindow.show()

    def show_vars(self):
        self.setings_subwind = subwindow()
        self.setings_subwind.ui = vars_form.Ui_MainWindow()
        self.setings_subwind.ui.setupUi(self.setings_subwind)
        self.setings_subwind.show()

        def set_vars():
            try:
                global global_vars
                if self.setings_subwind.ui.lineEdit.text() == core_functions.sign_var:
                    global_vars.update({"v0" : core_functions.sign_var})
                else:
                    global_vars.update({"v0": int(self.setings_subwind.ui.lineEdit.text())})

                if self.setings_subwind.ui.lineEdit_2.text() == core_functions.sign_var:
                    global_vars.update({"v0x" : core_functions.sign_var})
                else:
                    global_vars.update({"v0x": int(self.setings_subwind.ui.lineEdit_2.text())})

                if self.setings_subwind.ui.lineEdit_3.text() == core_functions.sign_var:
                    global_vars.update({"v0y" : core_functions.sign_var})
                else:
                    global_vars.update({"v0y": int(self.setings_subwind.ui.lineEdit_3.text())})

                if self.setings_subwind.ui.lineEdit_4.text() == core_functions.sign_var:
                    global_vars.update({"alpha" : core_functions.sign_var})
                else:
                    global_vars.update({"alpha": int(self.setings_subwind.ui.lineEdit_4.text())})

                if self.setings_subwind.ui.lineEdit_5.text() == core_functions.sign_var:
                    global_vars.update({"m" : core_functions.sign_var})
                else:
                    global_vars.update({"m": int(self.setings_subwind.ui.lineEdit_5.text())})

                if self.setings_subwind.ui.lineEdit_6.text() == core_functions.sign_var:
                    global_vars.update({"t_all" : core_functions.sign_var})
                else:
                    global_vars.update({"t_all": int(self.setings_subwind.ui.lineEdit_6.text())})

                if self.setings_subwind.ui.lineEdit_7.text() == core_functions.sign_var:
                    global_vars.update({"L" : core_functions.sign_var})
                else:
                    global_vars.update({"L": int(self.setings_subwind.ui.lineEdit_7.text())})

                if self.setings_subwind.ui.lineEdit_8.text() == core_functions.sign_var:
                    global_vars.update({"h_max" : core_functions.sign_var})
                else:
                    global_vars.update({"h_max": int(self.setings_subwind.ui.lineEdit_8.text())})

                if self.setings_subwind.ui.lineEdit_9.text() == core_functions.sign_var:
                    global_vars.update({"F" : core_functions.sign_var})
                else:
                    global_vars.update({"F": int(self.setings_subwind.ui.lineEdit_9.text())})

                if self.setings_subwind.ui.lineEdit_10.text() == core_functions.sign_var:
                    global_vars.update({"y0": core_functions.sign_var})
                else:
                    global_vars.update({"y0": int(self.setings_subwind.ui.lineEdit_10.text())})

                if self.setings_subwind.ui.lineEdit_11.text() == core_functions.sign_var:
                    global_vars.update({"x0": core_functions.sign_var})
                else:
                    global_vars.update({"x0": int(self.setings_subwind.ui.lineEdit_11.text())})

                if self.setings_subwind.ui.lineEdit_12.text() == core_functions.sign_var:
                    global_vars.update({"t": core_functions.sign_var})
                else:
                    global_vars.update({"t": int(self.setings_subwind.ui.lineEdit_12.text())})

                if self.setings_subwind.ui.lineEdit_13.text() == core_functions.sign_var:
                    global_vars.update({"x": core_functions.sign_var})
                else:
                    global_vars.update({"x": int(self.setings_subwind.ui.lineEdit_13.text())})

                if self.setings_subwind.ui.lineEdit_14.text() == core_functions.sign_var:
                    global_vars.update({"y": core_functions.sign_var})
                else:
                    global_vars.update({"y": int(self.setings_subwind.ui.lineEdit_14.text())})

                if self.setings_subwind.ui.lineEdit_15.text() == core_functions.sign_var:
                    global_vars.update({"vy": core_functions.sign_var})
                else:
                    global_vars.update({"vy": int(self.setings_subwind.ui.lineEdit_15.text())})

            except Exception:
                QMessageBox.warning(self, 'Ouch!', "Please enter the data!", QMessageBox.Ok, QMessageBox.Ok)
            self.setings_subwind.close()
            print(global_vars)
        self.setings_subwind.ui.pushButton.clicked.connect(set_vars)

        pass

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
            self.log_add('Planet selected!')
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
            self.ui.planet_label.setText(str(selected_planet.name) + '|')
            self.log_add('Speed selected')

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

            if cust_plnt.radius == 0 and cust_plnt.average_density == 0 and cust_plnt.mass == 0 and cust_plnt.name == 0:
                QMessageBox.warning(self, 'Ouch!', "Please enter the data!", QMessageBox.Ok, QMessageBox.Ok)
                selected_planet = settings_pack.earth
            else:
                self.check_vars()
            self.log_add('Planet selected!')
            self.setings_subwind.close()

        self.setings_subwind = subwindow()
        self.setings_subwind.ui = custom_planet.Ui_MainWindow()
        self.setings_subwind.ui.setupUi(self.setings_subwind)
        self.setings_subwind.show()
        self.setings_subwind.ui.buttonBox.rejected.connect(cancel_clicked)
        self.setings_subwind.ui.buttonBox.accepted.connect(ok_clicked)

        pass

    def log_add(self, log_msg):
        global log_text
        log_text = log_text + str(log_msg) + "\n"
        self.ui.textEdit.setText(log_text)



    def git_page_open(self):
        webbrowser.open('https://github.com/QuandisS/Physics_Project')

    def doc_page_open(self):
        webbrowser.open('https://github.com/QuandisS/Physics_Project/wiki')

#########################


    def solve_the_problem(self):
        global selected_planet
        global selected_speed
        global global_vars

        self.log_add('Solving the problem...')

        global_vars.update({'M': selected_planet.mass})
        global_vars.update({'r': selected_planet.radius})
        global_vars.update({'ro': selected_planet.average_density})
        global_vars.update({'sin_a': "-"})
        global_vars.update({'cos_a': "-"})
        global_vars.update({'G': constants.G})
        global_vars.update({'g': '-'})


        print(global_vars)



        if global_vars['alpha'] != '-':

            alpha = global_vars['alpha']
            alpha = math.radians(alpha)
            global_vars['alpha'] = alpha

        else:
            pass

        print(global_vars)

        solved = False
        solving = True
        unknown_vars = []

        for foo in global_vars.keys():
            if global_vars[foo] == '-':
                unknown_vars.append(foo)
            if global_vars[foo] == '0':
                pass
            else:
                continue

        if global_vars['t'] == 0:
            global_vars['t'] = core_functions.sign_var
        if global_vars['x'] == 0:
            global_vars['x'] = core_functions.sign_var
        if global_vars['y'] == 0:
            global_vars['y'] = core_functions.sign_var
        if global_vars['vy'] == 0:
            global_vars['vy'] = core_functions.sign_var
        if global_vars['m'] == 0:
            global_vars['m'] = core_functions.sign_var
        if global_vars['F'] == 0:
            global_vars['F'] = core_functions.sign_var

        if len(unknown_vars) == 0:
            solving = False
            solved = True

        while solving:
            unkn_before = unknown_vars
            for bar in unknown_vars:

                res = core_functions.doing_inst(core_functions.check_instr(core_functions.return_the_instructions(bar), global_vars), core_functions.return_the_instructions(bar), global_vars)

                if type(res) != int and type(res) != float and type(res) != complex:
                    if type(res) == str and res != 'абракадабра':
                        QMessageBox.critical(self, 'Ouch!', "Something went wrong in instruction:   " + res, QMessageBox.Ok,
                                             QMessageBox.Ok)
                        break
                    elif res != 'абракадабра':
                        QMessageBox.critical(self, 'Ouch!', "Something went wrong in instruction:   " + res.args[0], QMessageBox.Ok, QMessageBox.Ok)
                        solving = False
                        break

                if res == 'абракадабра':
                    continue
                else:
                    global_vars[bar] = res
                    unknown_vars.pop(bar)

            if len(unknown_vars) == len(unkn_before):
                if len(unknown_vars) == 0:
                    solving = False
                    solved = True
                    self.drawing_plot()

                else:
                    QMessageBox.warning(self, 'Ouch!', "There is not enough data to solve the problem!", QMessageBox.Ok,
                                        QMessageBox.Ok)
                    solving = False
            else:
                continue

        if solved:
            print('SOLED::::', global_vars)
            self.drawing_plot()

    def drawing_plot(self):
        QMessageBox.information(self, "Plot is drawing...", "Plot is drawing!", QMessageBox.Ok, QMessageBox.Ok)
        pass
#########################



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
