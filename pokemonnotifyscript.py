#!/usr/bin/env python

import requests, time, smtplib, getpass, json, datetime
from moves import getMoveName
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from math import radians, cos, sin, asin, sqrt
from collections import Counter
from lxml import html

cnt = Counter()

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def addMailEnding(mail):
    if "@" not in mail:
        return mail + "@gmail.com"
    else:
        return mail

def formatId (id):
    if len(id) == 1:
        return "00" + id
    elif len(id) == 2:
        return "0" + id
    else:
        return id

def setNoneToZero(value):
    if value is None:
        return 0
    else:
        return value

def getGender(gender):
    if gender == 1:
        return "Male";

    elif gender == 2:
        return "Female"

    elif gender == 3:
        return "None"
    else:
        return "Unknown"

def formatHeightWeight(value):
    if value is not None:
        return "{0:.2f}".format(value)

def sumIV(attack, defense, stamina):
    attack = setNoneToZero(attack)
    defense = setNoneToZero(defense)
    stamina = setNoneToZero(stamina)
    return attack + defense + stamina

def formatPokemonsToList(string):
    string = string.split(",")
    string = map(str.strip, string)
    string = map(str.lower, string)
    return string

def getPokemons():
    url = "https://www.pogonorge.com/takkforbidraget/raw_data?pokemon=true&pokestops=false&gyms=false&swLat=59.887683&swLng=10.612793&neLat=59.96176813704309&neLng=10.901299487051347"
    return requests.get(url).json()

def getPokemonTypes(typeList):
    if len(typeList) == 1:
        return typeList[0]["type"]
    elif len(typeList) > 1:
        types = typeList[0]["type"]
        typeList.pop(0)
        for t in typeList:
            types = types + " / " + t["type"]
            return types
    else:
        return None

def convertTimestampToTime(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')

def notifyDiscovery(id, name, lat, lng, attack, defense, stamina, rarity, types, gender, height, weight, move1, move2, iv, disappear_time):

    id = formatId(str(id))
    pageurl = 'http://bulbapedia.bulbagarden.net/wiki/File:' + id + str(name) +'.png'
    page = requests.get(pageurl)
    tree = html.fromstring(page.content)
    pokemonImageUrl = tree.xpath('//div[@class="fullImageLink"]//a/@href')[0]

    strongEnoughPokemon = iv >= ivLvl
    perfect = False

    if iv == 45:
        perfect = True

    weight = formatHeightWeight(weight) + "kg"
    height = formatHeightWeight(height) + "m"
    genderSign = getGender(gender)
    ivtemp = "{0:.1f}".format((float(iv) / 45) * 100) + " %"
    pokemonDistance = haversine(float(latAnswear), float(lngAnswear), float(lat), float(lng))
    pokemonNearby = pokemonDistance <= float(distanceAnswear)
    pokemonDistance = "{0:.2f}".format(pokemonDistance) + " km"
    pokemonTypes = getPokemonTypes(types)

    strengthText = "Normal"
    if perfect:
        strengthText = "PERFECT"
    elif iv > 42 and not perfect:
        strengthText = "Very strong"
    elif iv <= 42 and iv > 30:
        strengthText = "Strong"
    elif iv <= 22:
        strengthText = "Weak"

    print time.strftime("%d. %b %Y %H:%M:%S")
    print bcolors.OKGREEN + """{name} was discovered with:
    Strength: {strength}
    IV: {iv}
    Attack: {attack}
    Defense: {defense}
    Stamina: {stamina}
    Move1: {move1}
    Move2: {move2}
    Gender: {gender}
    Height: {height}
    Weight: {weight}
    Disappears: {disappear}
    Rarity: {rarity}
    Types: {types}
    Nearby: {nearby}
    Distance: {distance}
    Latitude: {lat}
    Longitude: {lng}
    """.format(name=name, strength=strengthText, types=pokemonTypes, gender=genderSign, height=height, weight=weight, rarity=rarity, iv=ivtemp, attack=attack, defense=defense, stamina=stamina, nearby=pokemonNearby, move1=move1, move2=move2, distance=pokemonDistance, lat=lat, lng=lng, disappear=disappear_time) + bcolors.ENDC

    if strongEnoughPokemon or pokemonNearby:
        if strongEnoughPokemon and pokemonNearby:
            pokemonDescription = strengthText + " and nearby"
        elif strongEnoughPokemon and not pokemonNearby:
            pokemonDescription = strengthText
        elif not strongEnoughPokemon and pokemonNearby:
            pokemonDescription = "Nearby"
        else:
            pokemonDescription = ""

        msg = MIMEMultipart('alternative')
        msg["From"] = fromEmail
        msg["To"] = toEmail
        msg["Subject"] = "#" + id + " " + name.upper() + " was found!"

        body = """ {description} {name} was discovered with:
        IV: {iv}
        Attack: {attack}
        Defense: {defense}
        Stamina: {stamina}
        Strength: {strength}
        Gender: {gender}
        Move1: {move1}
        Move2: {move2}
        Types: {types}
        Rarity: {rarity}
        Disappears: {disappear}
        Nearby: {nearby}
        Distance: {distance}
        http://maps.google.com/maps?z=8&t=m&q=loc:{lat}+{lng}
        """.format(description=pokemonDescription, name=name, strength=strengthText, gender=genderSign, height=height, weight=weight, types=pokemonTypes, rarity=rarity, iv=ivtemp, attack=attack, defense=defense, stamina=stamina, move1=move1, move2=move2, nearby=pokemonNearby, distance=pokemonDistance, lat=lat, lng=lng, disappear=disappear_time)

        htmlemail = """
        <html>
            <body>
                <h2>{description} {name} was discovered</h2>
                <img src={url} alt="Pokemon image" style="width:35%; float:right; max-width: 200px;">
                <ul style="list-style-position: inside; list-style-type: none;">
                <li>IV: {iv}</li>
                <li>Attack: {attack}</li>
                <li>Defense: {defense}</li>
                <li>Stamina: {stamina}</li>
                <li>Strength: {strength}</li>
                <li>Gender: {gender}</li>
                <li>Move1: {move1}</li>
                <li>Move2: {move2}</li>
                <li>Types: {types}</li>
                <li>Rarity: {rarity}</li>
                <li>Disappears: {disappear}</li>
                <li>Nearby: {nearby}</li>
                <li>Distance: {distance}</li>
                </ul>
                <h3><a href="http://maps.google.com/maps?z=8&t=m&q=loc:{lat}+{lng}">See on map!</a></h3>
            </body>
        </html>
        """.format(url=pokemonImageUrl, description=pokemonDescription, name=name, strength=strengthText, gender=genderSign, height=height, weight=weight, types=pokemonTypes, rarity=rarity, iv=ivtemp, attack=attack, defense=defense, stamina=stamina, move1=move1, move2=move2, nearby=pokemonNearby, distance=pokemonDistance, lat=lat, lng=lng, disappear=disappear_time)

        msg.attach(MIMEText(body, "plain"))

        msg.attach(MIMEText(htmlemail, 'html'))

        print bcolors.HEADER + "Sending email" + bcolors.ENDC
        print
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(fromEmail, password)
        text = msg.as_string()
        server.sendmail(fromEmail, toEmail, text)
        server.quit()

    cnt[name] += 1
    seenCount = len(discoveredList)
    print "Discovered pokemons so far is: " + str(seenCount)
    for key,value in sorted(cnt.iteritems()):
        print key, value
    print

# raw_input returns the empty string for "enter"
yes = set(["yes","y", "ye", ""])

send_url = "http://freegeoip.net/json"
r = requests.get(send_url)
j = json.loads(r.text)
yourlat = j["latitude"]
yourlng = j["longitude"]
print bcolors.OKBLUE + "-----------------------------------------------------------------------" + bcolors.ENDC
print "Your latitude: " + str(yourlat)
print "Your longitude: " + str(yourlng)
print "Default pokemons: "

defaults = ["moltres", "zapdos", "articuno", "mew", "mewtwo", "chikorita", "bayleef", "meganium", "cyndaquil", "quilava", "typhlosion", "totodile", "croconaw", "feraligatr", "togetic", "ampharos", "bellossom", "ursaring", "politoed", "sunflora", "espeon", "umbreon", "slowking", "unown", "steelix", "scizor", "heracross", "shuckle", "delibird", "skarmory", "houndoom", "kingdra", "donphan", "porygon2", "smeargle", "hitmontop", "miltank", "blissey", "raikou", "entei", "suicune", "lugia", "ho-oh", "celebi", "larvitar", "pupitar", "tyranitar"]
print defaults

choice = raw_input("Use the default Pokemons? [Yes/No] ").lower()
if choice in yes:
    choseDefault = True
    pokemons = defaults
else:
    choseDefault = False
    pokemons = formatPokemonsToList(raw_input("Please enter the pokemons you are searching for seperated by ",": "))

print pokemons
latAnswear = raw_input("What is your current latitude location? (Press enter to use location based on your IP-address) ").replace(",", ".");
lngAnswear = raw_input("What is your current longitude location? (Press enter to use location based on your IP-address) ").replace(",", ".");

if latAnswear == "":
    latAnswear = yourlat

if lngAnswear == "":
    lngAnswear = yourlng

ivLvl = int(float(raw_input("How strong should the pokemon be before sending email? [0-45] ").replace(",", ".")))

if ivLvl > 45 :
    ivLvl = 45
elif ivLvl < 0:
    ivLvl = 0

distanceAnswear = raw_input("How near should the pokemon be before you send an email? (km) ").replace(",", ".")
fromEmail = addMailEnding(raw_input("Sending Gmail account: "))
password = getpass.getpass("Password: ")
toEmail = addMailEnding(raw_input("Recieving email account: "))

#List of pokemons that are discoverd so you won"t get spammed
discoveredList = []

while True:
    print "Scanning..."
    try:
        pokemonJson = getPokemons()

        for i in pokemonJson["pokemons"]:
            attack = int(setNoneToZero(i["individual_attack"]));
            defense = int(setNoneToZero(i["individual_defense"]));
            stamina = int(setNoneToZero(i["individual_stamina"]));
            iv = sumIV(attack, defense, stamina)
            if i["encounter_id"] not in discoveredList :
                if i["pokemon_name"].lower() in pokemons or iv >= 45 :
                    disappear_time = convertTimestampToTime(int(str(i["disappear_time"])[:-3]))
                    move1 = getMoveName(str(i["move_1"]))
                    move2 = getMoveName(str(i["move_2"]))
                    discoveredList.append(i["encounter_id"])
                    notifyDiscovery(i["pokemon_id"], i["pokemon_name"], i["latitude"], i["longitude"], i["individual_attack"], i["individual_defense"], i["individual_stamina"], i["pokemon_rarity"], i["pokemon_types"], i["gender"], i["height"], i["weight"], move1, move2, iv, disappear_time)
    except ValueError:
        print bcolors.WARNING + "Error fetching pokemons. Retrying..." + bcolors.ENDC

    time.sleep(30)
