#!/usr/bin/env python

import requests, time, smtplib, getpass, time

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def addMailEnding(mail):
    if '@' not in mail:
        return mail + "@gmail.com"
    else:
        return mail

def setZerotoNone(value):
    if value == 0:
        return None
    else:
        return value

def sumIV(attack, defense, stamina):
    attack = setNonetoZero(attack)
    defense = setNonetoZero(defense)
    stamina = setNonetoZero(stamina)
    return attack + defense + stamina

def formatPokemonsToList(string):
    string = string.split(',')
    string = map(str.strip, string)
    string = map(str.lower, string)
    return string

def getPokemons():
    url = "https://www.pogovestfold.com/raw_data?pokemon=true&pokestops=false&gyms=false&swLat=59.887683&swLng=10.612793&neLat=59.96176813704309&neLng=10.901299487051347"
    return requests.get(url).json()

def setZerotoNone(value):
    if value == 0:
        return None
    else:
        return value

def setNonetoZero(value):
    if value is None:
        return 0
    else:
        return value

def notifyDiscoveryEmail(id, name, lat, lng, attack, defense, stamina):
    print time.strftime("%d. %b %Y %H:%M:%S")
    print bcolors.OKGREEN + """ {name} was found with:
    Attack: {attack}
    Defense: {defense}
    Stamina: {stamina}
    """.format(name=name, attack=attack, defense=defense, stamina=stamina) + bcolors.ENDC

    if name.lower() == "chansey" or sumIV(attack, defense, stamina) >= int(ivLvl):
        name = name.upper()
        msg = MIMEMultipart()
        msg['From'] = fromEmail
        msg['To'] = toEmail
        msg['Subject'] = "#" + str(id) + " " + name + " was found!"

        body = """ {name} was found with:
        Attack: {attack}
        Defense: {defense}
        Stamina: {stamina}
        http://maps.google.com/maps?z=8&t=m&q=loc:{lat}+{lng}
        """.format(name=name, attack=attack, defense=defense, stamina=stamina, lat=lat, lng=lng)
        msg.attach(MIMEText(body, 'plain'))

        print bcolors.HEADER + "Sending email" + bcolors.ENDC
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromEmail, password)
        text = msg.as_string()
        server.sendmail(fromEmail, toEmail, text)
        server.quit()


# raw_input returns the empty string for "enter"
yes = set(['yes','y', 'ye', ''])

defaults = ['lapras', 'dragonite', 'chansey', 'exeggutor', 'snorlax', 'gyarados', 'porygon', 'vaporeon', 'rhydon', 'omastar', 'kabutops', 'aerodactyl', 'hitmonlee', 'hitmonchan', 'lickitung', 'tangela']
print defaults
choice = raw_input("Use the default Pokemons? [Yes/No] ").lower()
if choice in yes:
    pokemons = defaults
else:
    pokemons = formatPokemonsToList(raw_input("Please enter the pokemons you are searching for seperated by ',': "))

print pokemons

ivLvl = raw_input("How strong should the pokemon be? [0-45] ")
fromEmail = addMailEnding(raw_input("Sending Gmail account: "))
password = getpass.getpass("Password: ")
toEmail = addMailEnding(raw_input("Recieving email account: "))

#List of pokemons that are discoverd so you won't get spammed
discoveredList = []

while True:
    print "Scanning..."
    try:
        pokemonJson = getPokemons()

        for i in pokemonJson['pokemons']:
            if i['pokemon_name'].lower() in pokemons and i['encounter_id'] not in discoveredList:
                discoveredList.append(i['encounter_id'])
                notifyDiscoveryEmail(i['pokemon_id'], i['pokemon_name'], i['latitude'], i['longitude'], i['individual_attack'], i['individual_defense'], i['individual_stamina'])

    except ValueError:
        print bcolors.WARNING + "Error fetching pokemons. Retrying..." + bcolors.ENDC

    time.sleep(30)
