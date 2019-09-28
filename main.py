from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import sys
import requests
import time
import datetime
import threading
import timeit

def time_thread():
    global login, password, url, world,authurl,url_world,gametype, roznica,dead
    s = requests.Session()
    s.headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0"
    s.headers['Content-Type'] = 'application/x-www-form-urlencoded'
    s.headers['X-Requested-With'] = 'XMLHttpRequest'
    res = s.get(url)
    data = f"username={login}&password={password}&remember=1"
    res = s.post(authurl, data=data, allow_redirects=False)
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
    print(local_time)

    s.close()
    while not dead:
        if len(main_table)==0:
            print(time.ctime(time.time() + roznica))

        else:
            if main_table[0][0]  <= time.time()+roznica + 60:
                s = requests.Session()
                s.headers[
                    'User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0"
                s.headers['Content-Type'] = 'application/x-www-form-urlencoded'
                s.headers['X-Requested-With'] = 'XMLHttpRequest'
                res = s.get(url)
                data = f"username={login}&password={password}&remember=1"
                res = s.post(authurl, data=data, allow_redirects=False)
                res = s.get(url_world)
                url_token = res.json()['uri']
                res = s.get(url_token)
                s.headers['TribalWars-Ajax'] = '1'
                url = f"https://{world}.{gametype}/game.php?village={main_table[0][2]}&ajax=ree"
                res = s.get(url)
                game_data = res.json()
                h = game_data['game_data']['csrf']


                if main_table[0][1] == "BUILD":
                    upgrade_url = f"https://{world}.{gametype}/game.php?village={main_table[0][2]}&screen=main&ajaxaction=upgrade_building&type=main&h={h}&&client_time={int(time.time())}"
                    body = f'id={main_table[0][2]}&force=1&destroy=0&source={main_table[0][2]}'
                    while True:
                        if time.time()+roznica >= main_table[0][0]:
                            res = s.post(upgrade_url, data=body, allow_redirects=False)
                            del main_table[0]
                            s.close()
                            break

                elif main_table[0][1] == "ATTACK": #work
                    url = f"https://{world}.{gametype}/game.php?village={main_table[0][2]}&screen=place"
                    res = s.get(url)
                    index = res.text.find('<input type="hidden" name="') +len('<input type="hidden" name="')
                    random_code1 = res.text[index:res.text.find('"', index)]
                    index = res.text.find('value="',index) +len('value="')
                    random_code2 = res.text[index:res.text.find('"', index)]
                    url = f"https://{world}.{gametype}/game.php?village={main_table[0][2]}&screen=place&try=confirm"
                    body = (f"{random_code1}={random_code2}&source_village={main_table[0][2]}&x={coordy['x']}&y={coordy['y']}&target_type=coord&attack={rodzaj}&input={coordy['x']}|{coordy['y']}&"
                    f"spear={ilosc['spear']}&sword={ilosc['sword']}&axe={ilosc['axe']}&archer={ilosc['archer']}&spy={ilosc['spy']}&light={ilosc['light']}&"
                    f"marcher={ilosc['marcher']}&heavy={ilosc['heavy']}&ram={ilosc['ram']}&catapult={ilosc['catapult']}&knight={ilosc['knight']}&snob={ilosc['snob']}")
                    res = s.post(url, data=body, allow_redirects=False)
                    index = res.text.find('<input type="hidden" name="ch" value="') + len('<input type="hidden" name="ch" value="')
                    ch = res.text[index:res.text.find('"', index)]
                    url = f"https://{world}.{gametype}/game.php?village={main_table[0][2]}&screen=place&action=command"
                    body_potwierdzenie = (f"attack=true&ch={ch}&x={coordy['x']}&y={coordy['y']}&source_village={main_table[0][2]}&village={main_table[0][3]}&"
                    f"spear={ilosc['ilosc_spear']}&sword={ilosc['ilosc_sword']}&axe={ilosc['ilosc_axe']}&archer={ilosc['ilosc_archer']}&spy={ilosc['ilosc_spy']}&light={ilosc['ilosc_light']}&"
                    f"marcher={ilosc['ilosc_marcher']}&heavy={ilosc['ilosc_heavy']}&ram={ilosc['ilosc_ram']}&catapult={ilosc['ilosc_catapult']}&knight={ilosc['ilosc_knight']}&snob={ilosc['ilosc_snob']}&building=main&h={h}")
                    while True:
                        if time.time()+roznica >= main_table[0][0]:
                            res = s.post(url, data=body_potwierdzenie, allow_redirects=True)
                            del main_table[0]
                            s.close()
                            break

                elif main_table[0][1] == "TRAIN":
                    body = f"units%5B{main_table[0][3]}%5D={main_table[0][4]}"
                    url = f"https://{world}.{gametype}/game.php?village={main_table[0][1]}&screen=barracks&ajaxaction=train&mode=train&&h={h}&&client_time={int(time.time())}"
                    while True:
                        if time.time()+roznica >= main_table[0][0]:
                            res = s.post(url, data=body, allow_redirects=False)
                            del main_table[0]
                            s.close()
                            break




def przypisz():
    if dlg.loginLog.text()  =="" or dlg.passwordLog.text()=="" or dlg.urlLog.text()=="" or dlg.worldLog.text()=="":
        error_puste_pole()
    else:
        global login, password, url, world,authurl,url_world,gametype
        login = dlg.loginLog.text()
        password = dlg.passwordLog.text()
        world = dlg.worldLog.text()
        gametype = f"{dlg.urlLog.text()[4::]}"
        url = f"https://{dlg.urlLog.text()}"
        authurl = f'{url}/page/auth'
        url_world = f"{url}/page/play/{world}"
        dlg.close()
        timer = threading.Thread(target=time_thread)
        timer.start()
        root.show()


def timeline_add_train():
    tm = make_time(root.time_train.text().split(":"))
    slot = (tm,"TRAIN",root.ID_village_train.text(),root.train_type.currentText(),root.amount_train.text())
    if len(main_table)==0:
        main_table.append(slot)
    else:
        i = 0
        for slot in main_table:
            if slot[0]<= main_table[i][0]:
                main_table.insert(i,slot)
            else:
                i += 1

def timeline_add_build():
    tm = make_time(root.time_build.text().split(":"))
    slot = (tm,"BUILD",root.ID_village_build.text(),root.build_type.currentText())
    if len(main_table) == 0:
        main_table.append(slot)
    else:
        i = 0
        for slot in main_table:
            if slot[0] <= main_table[i][0]:
                main_table.insert(i, slot)
                break
            else:
                i += 1

def timeline_add_atack():
    global ilosc
    a = 0
    for i in unit_type:
        ilosc[f'{i}'] = atk_win.amount_atack.item(a,0).text()
        a+=1
    tm = make_time(root.time_atack.text().split(":"))
    slot = (tm,"ATTACK",root.village_id_source.text(),root.target_xy.text(),ilosc)
    if len(main_table) == 0:
        main_table.append(slot)
    else:
        i = 0
        for slot in main_table:
            if slot[0] <= main_table[i][0]:
                main_table.insert(i, slot)
            else:
                i += 1

def make_time(data):
    time_func = list(map(int,data))
    dt = datetime.datetime(time_func[0],time_func[1],time_func[2],time_func[3],time_func[4],time_func[5],time_func[6])
    tm = time.mktime(dt.timetuple())
    return tm

def show_atack_content():
    atk_win.show()

def error_puste_pole():
    QMessageBox.information(None, "404", "One or more fields are empty")

if __name__ == '__main__':
    global dead
    app = QtWidgets.QApplication([])
    dlg = uic.loadUi("main_root.ui")
    root = uic.loadUi("main_win.ui")
    atk_win = uic.loadUi("amount.ui")

    dead = False
    login = ""
    password = ""
    url = ""
    world = ""
    authurl = ""
    url_world = ""
    gametype = ""
    main_table = []

    unit_type = ['spear','sword','axe','archer','spy','light','marcher','heavy','ram','catapult','knight','snob']

    ilosc = {}

    dlg.login_button.clicked.connect(przypisz)
    root.addToTime_train.clicked.connect(timeline_add_train)
    root.addToTime_build.clicked.connect(timeline_add_build)
    root.addToTime_atack.clicked.connect(timeline_add_atack)
    root.atack_content.clicked.connect(show_atack_content)



    dlg.show()

    sys.exit(app.exec())