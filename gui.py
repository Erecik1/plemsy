from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys

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

def error_puste_pole():
    QMessageBox.information(None, "404", "One or more field is empty")

def timeline_add_train(): # poprawic
    slot = f"{root.time_train.text()} | TRAIN | ID: {root.ID_village_train.text()} | {root.train_type.currentText()} | {root.amount_train.text()}"

    root.timeline.addItem(slot)

def timeline_add_build():  # poprawic
    slot = f"{root.time_build.text()} | BUILD | ID: {root.ID_village_build.text()} | {root.build_type.currentText()}"

    root.timeline.addItem(slot)

    slot_raw = root.time_build.text().split(":")
    print(slot_raw)
    slot_raw_raw = list(map(int,slot_raw))
    print(slot_raw_raw)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dlg = uic.loadUi("main_root.ui")
    root = uic.loadUi("main_win.ui")


    login = ""
    password = ""
    url = ""
    world = ""


    dlg.login_button.clicked.connect(przypisz)
    root.addToTime_train.clicked.connect(timeline_add_train)
    root.addToTime_build.clicked.connect(timeline_add_build)



    dlg.show()
    sys.exit(app.exec())

