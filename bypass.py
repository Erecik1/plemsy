import requests
import time
import datetime
import re
import timeit

uzyszkodnik = 'lololoks'
haslo = '4mzorwu4'
swiat = 'pl140'
wiocha = '92681'
url = 'https://www.plemiona.pl'
authurl = f'{url}/page/auth'
url_swiat = f"{url}/page/play/{swiat}"

ilosc = {"ilosc_spear": "1",
        "ilosc_sword": "0",
        "ilosc_axe": "0",
        "ilosc_archer": "0",
        "ilosc_spy": "0",
        "ilosc_light": "0",
        "ilosc_marcher": "0",
        "ilosc_heavy": "0",
        "ilosc_ram": "0",
        "ilosc_catapult": "0",
        "ilosc_knight": "0",
        "ilosc_snob": "0"
}

budynki = {
    'ratusz': 'main',
    'koszary': 'barracks',
    'piedestal': 'statue',
    'rynek': 'market',
    'tartak': 'wood',
    'cegielnia': 'stone',
    'huta': 'iron',
    'zagroda': 'farm',
    'spichlerz': 'storage',
    'schowek': 'hide',
    'mur': 'wall',
    'stajnia': 'stable',
    'warsztat': 'garage',
    'palac': 'snob',
    'kuznia': 'smith'
}

coordy = {"x": "780", "y": "560"}
rodzaj = ("Napad")
jednostka = "spear"

def rekrutacja(jednostka,ilosc):
    jednostka = "spear"
    ilosc = "1"
    body = f"units%5B{jednostka}%5D={ilosc}"
    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=barracks&ajaxaction=train&mode=train&&h={h}&&client_time={int(time.time())}"
    res = s.post(url, data=body, allow_redirects=False)

def atakowanie():
    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=place&try=confirm"
    body = (f"4020934f82eabb1efbb28c=458160e5402093&source_village={wiocha}&x={coordy['x']}&y={coordy['y']}&target_type=coord&attack={rodzaj}&input={coordy['x']}|{coordy['y']}&"
    f"spear={ilosc['ilosc_spear']}&sword={ilosc['ilosc_sword']}&axe={ilosc['ilosc_axe']}&archer={ilosc['ilosc_archer']}&spy={ilosc['ilosc_spy']}&light={ilosc['ilosc_light']}&"
    f"marcher={ilosc['ilosc_marcher']}&heavy={ilosc['ilosc_heavy']}&ram={ilosc['ilosc_ram']}&catapult={ilosc['ilosc_catapult']}&knight={ilosc['ilosc_knight']}&snob={ilosc['ilosc_snob']}")
    res = s.post(url, data=body, allow_redirects=False)
    index = res.text.find('<input type="hidden" name="ch" value="') + len('<input type="hidden" name="ch" value="')
    ch = res.text[index:res.text.find('"', index)]
    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=place&action=command"
    body_potwierdzenie = (f"attack=true&ch={ch}&x={coordy['x']}&y={coordy['y']}&source_village={wiocha}&village={wiocha}&"
    f"spear={ilosc['ilosc_spear']}&sword={ilosc['ilosc_sword']}&axe={ilosc['ilosc_axe']}&archer={ilosc['ilosc_archer']}&spy={ilosc['ilosc_spy']}&light={ilosc['ilosc_light']}&"
    f"marcher={ilosc['ilosc_marcher']}&heavy={ilosc['ilosc_heavy']}&ram={ilosc['ilosc_ram']}&catapult={ilosc['ilosc_catapult']}&knight={ilosc['ilosc_knight']}&snob={ilosc['ilosc_snob']}&building=main&h={h}")
    res = s.post(url, data=body_potwierdzenie, allow_redirects=True)

def upgrade():
    upgrade_url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=main&ajaxaction=upgrade_building&type=main&h={h}&&client_time={int(time.time())}"
    body = f'id={budynki["ratusz"]}&force=1&destroy=0&source={wiocha}'
    res = s.post(upgrade_url, data=body, allow_redirects=False)

def czasowka(*args):
    dt = datetime.datetime(*args)
    tm = time.mktime(dt.timetuple())
    while True:
        if  timeit.default_timer()+roznica >= tm:
            atakowanie()
            print(tm)
            print('wyslalo')
            break
        print(f'{time.ctime(timeit.default_timer()+roznica)} +  czekam na {time.ctime(tm)} ')

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
teraz = timeit.default_timer() - teraz
roznica = float(czas[1::]) - timeit.default_timer() + teraz

czas_strony = timeit.default_timer()+roznica
local_time = time.ctime(czas_strony)


url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&ajax=ree"
res = s.get(url)
game_data = res.json()

h = game_data['game_data']['csrf']

czasowka(2019,8,24,23,14,25)