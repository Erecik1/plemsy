from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import requests
import time
import datetime
import timeit
import re

def logout(city_id):
    url_logout = f"https://pl140.plemiona.pl/game.php?village={city_id}&screen=&action=logout&h={h}"

def prime(village_id,url,*args): #wypierdala sie przy wywołaniu url 15 linia
    s = requests.Session()
    s.headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0"
    s.headers['Content-Type'] = 'application/x-www-form-urlencoded'
    s.headers['X-Requested-With'] = 'XMLHttpRequest'
    print('tutaj')
    print(url)
    res = s.get(url)
    print('tutaj1/2')
    data = f"username={login}&password={password}&remember=1"
    print('tutaj2')
    res = s.post(authurl, data=data, allow_redirects=False)
    print(authurl)
    print('tutaj3')
    print(url_world)
    res = s.get(url_world)
    url_token = res.json()['uri']
    teraz = timeit.default_timer()
    res = s.get(url_token)

    s.headers['TribalWars-Ajax'] = '1'
    czas = res.text[-600:-300]
    index = czas.find("Timing.init(") + len(("Timing.init("))
    index_2nd = czas.find("TribalWars.initTab") - 11
    czas = czas[index:index_2nd]
    teraz = timeit.default_timer() - teraz
    roznica = float(czas) - time.time() + teraz

    czas_strony = time.time() + roznica
    local_time = time.ctime(czas_strony)

    url = f"https://{world}.plemiona.pl/game.php?village={village_id}&ajax=ree"
    res = s.get(url)
    game_data = res.json()

    h = game_data['game_data']['csrf']
    print(args)
    dt = datetime.datetime(*args)
    tm = time.mktime(dt.timetuple())
    while True:
        if  time.time()+roznica >= tm:
            print(tm)
            print('wyslalo')
            break
        print(f'{time.ctime(timeit.default_timer()+roznica)} +  czekam na {time.ctime(tm)} ')



def przypisz():
    if dlg.loginLog.text()  =="" or dlg.passwordLog.text()=="" or dlg.urlLog.text()=="" or dlg.worldLog.text()=="":
        error_puste_pole()
    else:
        global login, password, url, world,authurl,url_world
        login = dlg.loginLog.text()
        password = dlg.passwordLog.text()
        world = dlg.worldLog.text()
        url = f"https://{dlg.urlLog.text()}"
        authurl = f'{url}/page/auth'
        url_world = f"{url}/page/play/{world}"
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

def timeline_add_atack():
    global ilosc
    a = 0
    for i in unit_type:
        ilosc[f'{i}'] = atk_win.amount_atack.item(a,0).text()
        a+=1
    slot = f"{root.time_atack.text()} | ATTACK | ID: {root.village_id_source.text()} | {root.target_xy.text()} | {ilosc}"
    print(slot)
    root.timeline.addItem(slot)
    prime('92681',url,2019,8,27,2,13,30,1234)

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
    authurl = ""
    url_world = ""

    unit_type = ['spear','sword','axe','archer','spy','light','marcher','heavy','ram','catapult','knight','snob']

    ilosc = {}

    dlg.login_button.clicked.connect(przypisz)
    root.addToTime_train.clicked.connect(timeline_add_train)
    root.addToTime_build.clicked.connect(timeline_add_build)
    root.addToTime_atack.clicked.connect(timeline_add_atack)
    root.atack_content.clicked.connect(show_atack_content)



    dlg.show()
    sys.exit(app.exec())

