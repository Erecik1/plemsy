import requests
import time
import datetime
import re
import timeit

coordy = {"x": "780", "y": "560"}
rodzaj = ("Napad")

def sprawdz_konto(login,haslo): # poprawic
    s = requests.Session()

    s.headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0"
    s.headers['Content-Type'] = 'application/x-www-form-urlencoded'
    s.headers['X-Requested-With'] = 'XMLHttpRequest'

    res = s.get(url)

    data = f"username={login}&password={haslo}&remember=1"
    res = s.post(authurl, data=data, allow_redirects=False)
    if res.cookies == 200:
        return True
    else:
        return False

def rekrutacja(jednostka,ilosc):
    body = f"units%5B{jednostka}%5D={ilosc}"
    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=barracks&ajaxaction=train&mode=train&&h={h}&&client_time={int(time.time())}"
    res = s.post(url, data=body, allow_redirects=False)

def atakowanie(wioska,cel,jednoski,godzina):
    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=place&try=confirm"
    body = (f"4020934f82eabb1efbb28c=458160e5402093&source_village={wiocha}&x={coordy['x']}&y={coordy['y']}&target_type=coord&attack={rodzaj}&input={coordy['x']}|{coordy['y']}&"
    f"spear={ilosc['spear']}&sword={ilosc['sword']}&axe={ilosc['axe']}&archer={ilosc['archer']}&spy={ilosc['spy']}&light={ilosc['light']}&"
    f"marcher={ilosc['marcher']}&heavy={ilosc['heavy']}&ram={ilosc['ram']}&catapult={ilosc['catapult']}&knight={ilosc['knight']}&snob={ilosc['snob']}")
    res = s.post(url, data=body, allow_redirects=False)
    index = res.text.find('<input type="hidden" name="ch" value="') + len('<input type="hidden" name="ch" value="')
    ch = res.text[index:res.text.find('"', index)]
    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=place&action=command"
    body_potwierdzenie = (f"attack=true&ch={ch}&x={coordy['x']}&y={coordy['y']}&source_village={wiocha}&village={wiocha}&"
    f"spear={ilosc['ilosc_spear']}&sword={ilosc['ilosc_sword']}&axe={ilosc['ilosc_axe']}&archer={ilosc['ilosc_archer']}&spy={ilosc['ilosc_spy']}&light={ilosc['ilosc_light']}&"
    f"marcher={ilosc['ilosc_marcher']}&heavy={ilosc['ilosc_heavy']}&ram={ilosc['ilosc_ram']}&catapult={ilosc['ilosc_catapult']}&knight={ilosc['ilosc_knight']}&snob={ilosc['ilosc_snob']}&building=main&h={h}")
    res = s.post(url, data=body_potwierdzenie, allow_redirects=True)

def upgrade(wiocha,budynek,godzina):
    upgrade_url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=main&ajaxaction=upgrade_building&type=main&h={h}&&client_time={int(time.time())}"
    body = f'id={budynki["ratusz"]}&force=1&destroy=0&source={wiocha}'
    res = s.post(upgrade_url, data=body, allow_redirects=False)

def czasowka(*args): #liczby
    dt = datetime.datetime(*args) #date
    tm = time.mktime(dt.timetuple(dt)) #czas maszynowy
    while True:
        if  timeit.default_timer()+roznica >= tm:
            atakowanie()
            print(tm)
            print('wyslalo')
            break
        print(f'{time.ctime(timeit.default_timer()+roznica)} +  czekam na {time.ctime(tm)} ')

def kareta():
    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=place&try=confirm"
    
    index = res.text.find('<input type="hidden" name="ch" value="') + len('<input type="hidden" name="ch" value="')
    ch = res.text[index:res.text.find('"', index)]
    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=place&action=command"
    form_data = ("attack=true&ch=bbf4cdc8291e96bc4958ec163f5f5d12%3A05e7e45866152b540f9c1b71441b26313e1519efe9ce028e6055d4d1a212715b&x=413&y=524&"
    "source_village=2965&village=2965&attack_name=&train%5B2%5D%5Bspear%5D=&train%5B2%5D%5Bsword%5D=&train%5B2%5D%5Baxe%5D=&train%5B2%5D%5Barcher%5D="
    "&train%5B2%5D%5Bspy%5D=&train%5B2%5D%5Blight%5D=833&train%5B2%5D%5Bmarcher%5D=&train%5B2%5D%5Bheavy%5D=&train%5B2%5D%5Bram%5D=&train%5B2%5D%5Bcatapult%5D="
    "&train%5B2%5D%5Bknight%5D=&train%5B2%5D%5Bsnob%5D=1&train%5B3%5D%5Bspear%5D=&train%5B3%5D%5Bsword%5D=&train%5B3%5D%5Baxe%5D=&train%5B3%5D%5Barcher%5D="
    "&train%5B3%5D%5Bspy%5D=&train%5B3%5D%5Blight%5D=833&train%5B3%5D%5Bmarcher%5D=&train%5B3%5D%5Bheavy%5D=&train"
    "%5B3%5D%5Bram%5D=&train%5B3%5D%5Bcatapult%5D=&train%5B3%5D%5Bknight%5D=&train%5B3%5D%5Bsnob%5D=1&train%5B4%5D%5Bspear%5D=&train%5B4%5D%5Bsword%5D=&train"
    "%5B4%5D%5Baxe%5D=&train%5B4%5D%5Barcher%5D=&train%5B4%5D%5Bspy%5D=&train%5B4%5D%5Blight%5D=834&train%5B4%5D%5Bmarcher%5D=&train%5B4%5D%5Bheavy%5D=&train%5B4%5D%5Bram%5D=&train%5B4%5D%5Bcatapult%5D=&train%5B4%5D%5Bknight%5D="
    "&train%5B4%5D%5Bsnob%5D=1&spear=0&sword=0&axe=6000&archer=0&spy=0&light=0&marcher=0&heavy=0&ram=0&catapult=0&knight=0&snob=1&building=farm&h=f2adb1fb")
    res = s.post(url, data=body_potwierdzenie, allow_redirects=True)

def main():
    wiocha = '92681'
    authurl = f'{url}/page/auth'
    url_swiat = f"{url}/page/play/{swiat}"

    s = requests.Session()

    s.headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0"
    s.headers['Content-Type'] = 'application/x-www-form-urlencoded'
    s.headers['X-Requested-With'] = 'XMLHttpRequest'

    res = s.get(url)

    data = f"username={uzyszkodnik}&password={haslo}&remember=1"
    res = s.post(authurl, data=data, allow_redirects=False)

    res = s.get(url_swiat)
    url_token = res.json()['uri']
    teraz = timeit.default_timer()
    res = s.get(url_token)


    s.headers['TribalWars-Ajax'] = '1'
    czas = res.text[-395:-360]
    czas = re.sub(r'[Tmgitn(); \n]', '', czas)
    print(czas)
    teraz = timeit.default_timer() - teraz
    print(teraz)
    roznica = float(czas[1::]) - timeit.default_timer() + teraz
    print(roznica)

    czas_strony = timeit.default_timer()+roznica
    print(czas_strony)
    local_time = time.ctime(czas_strony)
    print(local_time)


    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&ajax=ree"
    res = s.get(url)
    game_data = res.json()

    h = game_data['game_data']['csrf']

#czasowka(2019,8,24,23,14,25)
#print(sprawdz_konto('lololoks','4mzkkk'))
print(timeit.default_timer())
print(time.time())
print(time.time()+timeit.default_timer())