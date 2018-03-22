# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

version = "v1"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 60, 731, 441))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCredits = QtWidgets.QMenu(self.menubar)
        self.menuCredits.setObjectName("menuCredits")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExport_image_chart = QtWidgets.QAction(MainWindow)
        self.actionExport_image_chart.setObjectName("actionExport_image_chart")
        self.actionSettings_Pack = QtWidgets.QAction(MainWindow)
        self.actionSettings_Pack.setObjectName("actionSettings_Pack")
        self.actionSpeed = QtWidgets.QAction(MainWindow)
        self.actionSpeed.setObjectName("actionSpeed")
        self.actionCustom_planet_settings = QtWidgets.QAction(MainWindow)
        self.actionCustom_planet_settings.setObjectName("actionCustom_planet_settings")
        self.actionCredits = QtWidgets.QAction(MainWindow)
        self.actionCredits.setObjectName("actionCredits")
        self.actionExport_log_file = QtWidgets.QAction(MainWindow)
        self.actionExport_log_file.setObjectName("actionExport_log_file")
        self.actionDocumetation = QtWidgets.QAction(MainWindow)
        self.actionDocumetation.setObjectName("actionDocumetation")
        self.actionGitHub_Page = QtWidgets.QAction(MainWindow)
        self.actionGitHub_Page.setObjectName("actionGitHub_Page")
        self.menuSetting.addAction(self.actionSettings_Pack)
        self.menuSetting.addSeparator()
        self.menuSetting.addAction(self.actionSpeed)
        self.menuSetting.addAction(self.actionCustom_planet_settings)
        self.menuSetting.addSeparator()
        self.menuFile.addAction(self.actionExport_image_chart)
        self.menuFile.addAction(self.actionExport_log_file)
        self.menuCredits.addAction(self.actionCredits)
        self.menuCredits.addAction(self.actionDocumetation)
        self.menuCredits.addAction(self.actionGitHub_Page)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuCredits.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setWindowTitle('Physics')
        self.centralwidget.setLayout(self.gridLayout)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "Ввод данных"))
        self.pushButton_7.setText(_translate("MainWindow", "..."))
        self.pushButton_5.setText(_translate("MainWindow", "Создать График"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCredits.setTitle(_translate("MainWindow", "Info"))
        self.actionExport_image_chart.setText(_translate("MainWindow", "Export image (chart)"))
        self.actionSettings_Pack.setText(_translate("MainWindow", "Settings Pack"))
        self.actionSpeed.setText(_translate("MainWindow", "Speed"))
        self.actionCustom_planet_settings.setText(_translate("MainWindow", "Custom planet settings"))
        self.actionCredits.setText(_translate("MainWindow", "Credits"))
        self.actionExport_log_file.setText(_translate("MainWindow", "Export log file"))
        self.actionDocumetation.setText(_translate("MainWindow", "Documetation"))
        self.actionGitHub_Page.setText(_translate("MainWindow", "GitHub Page"))

