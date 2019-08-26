from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys

def przypisz():
    if dlg.loginLog.text()  =="" or dlg.passwordLog.text()=="" or dlg.urlLog.text()=="" or dlg.worldLog.text()=="":
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
    QMessageBox.information(None, "404", "One or more fields are empty")

def timeline_add_train(): # poprawic
    slot = f"{root.time_train.text()} | TRAIN | ID: {root.ID_village_train.text()} | {root.train_type.currentText()} | {root.amount_train.text()}"

    root.timeline.addItem(slot)

def timeline_add_build():
    slot = f"{root.time_build.text()} | BUILD | ID: {root.ID_village_build.text()} | {root.build_type.currentText()}"

    root.timeline.addItem(slot)

    slot_raw = root.time_build.text().split(":")
    slot_raw_raw = list(map(int,slot_raw))

def timeline_add_atack():
    slot = f"{root.time_atack.text()} | ATTACK | ID: {root.village_id_source.text()} | {root.target_xy.Text()}"
    print(root.time_atack.text(),root.village_id_source.text(),root.target_xy.Text())
    root.timeline.addItem(slot)

def show_atack_content():
    atk_win.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    dlg = uic.loadUi("main_root.ui")
    root = uic.loadUi("main_win.ui")
    atk_win = uic.loadUi("amount.ui")


    login = ""
    password = ""
    url = ""
    world = ""


    dlg.login_button.clicked.connect(przypisz)
    root.addToTime_train.clicked.connect(timeline_add_train)
    root.addToTime_build.clicked.connect(timeline_add_build)
    root.addToTime_atack.clicked.connect(timeline_add_atack)
    root.atack_content.clicked.connect(show_atack_content)



    dlg.show()
    sys.exit(app.exec())

