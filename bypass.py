import requests
import time
import datetime
import re
import json

uzyszkodnik = 'lololoks'
haslo = '4mzorwu4'
swiat = 'pl140'
wiocha = '2701'
url = 'https://www.plemiona.pl'
authurl = f'{url}/page/auth'
url_swiat = f"{url}/page/play/{swiat}"

ilosc = {"ilosc_spear": "2",
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

coordy = {"x": "584", "y": "638"}
rodzaj = ("Napad")

def rekrutacja():
    jednostka = "spear"
    ilosc = "1"
    body = f"units%5B{jednostka}%5D={ilosc}"
    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=barracks&ajaxaction=train&mode=train&&h={h}&&client_time={int(time.time())}"
    res = s.post(url, data=body, allow_redirects=False)

def atakowanie():
    now = time.time()
    url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=place&try=confirm"
    body = (f"14b73ac5ed6106dc1e403a=db3a67f914b73a&source_village={wiocha}&x={coordy['x']}&y={coordy['y']}&target_type=coord&attack={rodzaj}&input={coordy['x']}|{coordy['y']}&"
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
    print(f"funkcji zajelo {time.time() - now}")

def upgrade():
    upgrade_url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&screen=main&ajaxaction=upgrade_building&type=main&h={h}&&client_time={int(time.time())}"
    body = f'id={budynki["ratusz"]}&force=1&destroy=0&source={wiocha}'
    res = s.post(upgrade_url, data=body, allow_redirects=False)


s = requests.Session()

s.headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:63.0) Gecko/20100101 Firefox/63.0"
s.headers['Content-Type'] = 'application/x-www-form-urlencoded'
s.headers['X-Requested-With'] = 'XMLHttpRequest'

# get page cookies
res = s.get(url)

# login to account
data = f"username={uzyszkodnik}&password={haslo}&remember=1"
res = s.post(authurl, data=data, allow_redirects=False)

# login to gameworld
res = s.get(url_swiat)
url_token = res.json()['uri']

# get token
res = s.get(url_token)

# set tribal wars header
s.headers['TribalWars-Ajax'] = '1'
czas = res.text[-417:-390]
czas = re.sub(r'[itn(); \n]', '', czas)
roznica = float(czas)-time.time()
while True:
    local_time = time.ctime(time.time()+roznica)
    print("Local time:", local_time)

# logged into game
# get gameworld data
url = f"https://{swiat}.plemiona.pl/game.php?village={wiocha}&ajax=ree"
res = s.get(url)
game_data = res.json()

# get h token
h = game_data['game_data']['csrf']