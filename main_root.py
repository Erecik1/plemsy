# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_root.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login_screen(object):
    def setupUi(self, login_screen):
        login_screen.setObjectName("login_screen")
        login_screen.resize(312, 229)
        login_screen.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(login_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(80, 150, 131, 41))
        self.login_button.setObjectName("login_button")
        self.login = QtWidgets.QTextEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(80, 20, 104, 20))
        self.login.setObjectName("login")
        self.login_label = QtWidgets.QLabel(self.centralwidget)
        self.login_label.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.login_label.setObjectName("login_label")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(20, 50, 61, 20))
        self.password_label.setObjectName("password_label")
        self.haslo = QtWidgets.QTextEdit(self.centralwidget)
        self.haslo.setGeometry(QtCore.QRect(80, 50, 104, 20))
        self.haslo.setObjectName("haslo")
        self.url_label = QtWidgets.QLabel(self.centralwidget)
        self.url_label.setGeometry(QtCore.QRect(30, 80, 21, 16))
        self.url_label.setObjectName("url_label")
        self.url = QtWidgets.QTextEdit(self.centralwidget)
        self.url.setGeometry(QtCore.QRect(80, 80, 161, 20))
        self.url.setObjectName("url")
        self.world_label = QtWidgets.QLabel(self.centralwidget)
        self.world_label.setGeometry(QtCore.QRect(30, 110, 31, 16))
        self.world_label.setObjectName("world_label")
        self.world = QtWidgets.QTextEdit(self.centralwidget)
        self.world.setGeometry(QtCore.QRect(80, 110, 104, 20))
        self.world.setObjectName("world")
        login_screen.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login_screen)
        self.statusbar.setObjectName("statusbar")
        login_screen.setStatusBar(self.statusbar)

        self.retranslateUi(login_screen)
        QtCore.QMetaObject.connectSlotsByName(login_screen)

    def retranslateUi(self, login_screen):
        _translate = QtCore.QCoreApplication.translate
        login_screen.setWindowTitle(_translate("login_screen", "MainWindow"))
        self.login_button.setText(_translate("login_screen", "Log In"))
        self.login_label.setText(_translate("login_screen", "Login"))
        self.password_label.setText(_translate("login_screen", "Password"))
        self.url_label.setText(_translate("login_screen", "Url"))
        self.url.setHtml(_translate("login_screen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ex. &quot;www.plemiona.pl&quot;</p></body></html>"))
        self.world_label.setText(_translate("login_screen", "World"))
        self.world.setHtml(_translate("login_screen", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ex. &quot;pl144&quot;</p></body></html>"))
