from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import bypass

def przypisz():
    if dlg.loginLog.text()  =="": # or dlg.password.text().isEmpty() or dlg.url.text().isEmpty() or dlg.world.text().isEmpty():
        error_puste_pole()
    else:
        global login, password, url, world
        login = dlg.loginLog.text()
        password = dlg.passwordLog.text()
        url = f"https://{dlg.urlLog.text()}"
        world = dlg.worldLog.text()
        dlg.close()
        root.show()
        error_puste_pole()

def error_puste_pole():
    QMessageBox.information(None, "404", "One or more field is empty")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dlg = uic.loadUi("main_root.ui")
    root = uic.loadUi("main_win.ui")

    login = ""
    password = ""
    url = ""
    world = ""


    dlg.login_button.clicked.connect(przypisz)



    root.menubar.menuAtack.actionNormal.addAction(error_puste_pole)

    dlg.show()
    app.exec()

