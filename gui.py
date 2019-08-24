from PyQt5 import QtWidgets, uic

def przypisz(self):
    print(dlg.login.text())
#   login = str(dlg.login.text())
#    haslo = str(dlg.haslo.text())
#    url = str(dlg.url.text())
#    world = str(dlg.world.text())"""

app = QtWidgets.QApplication([])
dlg = uic.loadUi("main_root.ui")

dlg.login_button.clicked.connect(przypisz)


dlg.show()
app.exec()