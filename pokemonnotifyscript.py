#!/usr/bin/env python

import requests, time, smtplib, getpass

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

pokemons = ['lapras', 'dragonite', 'chansey', 'exeggutor', 'snorlax']
#pokemons = raw_input("Please enter the pokemons you are searching for seperated by ',': ")
pokemons = pokemons.split(',')
pokemons = map(str.strip, pokemons)
pokemons = map(str.lower, pokemons)
fromEmail = raw_input("Sending Gmail account: ")
password = getpass.getpass("Password: ")
toEmail = raw_input("Recieving email account: ")

pokemonHits = []

def getPokemons() :
    url = "https://www.pogovestfold.com/raw_data?pokemon=true&pokestops=false&gyms=false&swLat=59.887683&swLng=10.612793&neLat=59.96176813704309&neLng=10.901299487051347"
    return requests.get(url).json()

def notifyHitEmail(id, name, lat, lng, attack, defense, stamina) :
    print name + " was found!"
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = str(id) + " " + name + " was found!"

    body = """ {name} was found with:
    Attack: {attack}
    Defense: {defense}
    Stamina: {stamina}
    http://maps.google.com/maps?z=12&t=m&q=loc:{lat}+{lng}
    """.format(name=name, attack=attack, defense=defense, stamina=stamina, lat=lat, lng=lng)
    msg.attach(MIMEText(body, 'plain'))

    print bcolors.OKGREEN + """ {name} was found with:
    Attack: {attack}
    Defense: {defense}
    Stamina: {stamina}
    """.format(name=name, attack=attack, defense=defense, stamina=stamina) + bcolors.ENDC

    print "Sending email"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromEmail, password)
    text = msg.as_string()
    server.sendmail(fromEmail, toEmail, text)
    server.quit()

while True:
    print "Scanning..."
    try:
        pokemonJson = getPokemons()

        for i in pokemonJson['pokemons']:
            if i['pokemon_name'].lower() in pokemons and i['encounter_id'] not in pokemonHits:
                pokemonHits.append(i['encounter_id'])
                notifyHitEmail(i['pokemon_id'], i['pokemon_name'], i['latitude'], i['longitude'], i['individual_attack'], i['individual_defense'], i['individual_stamina'])

    except ValueError:
        print bcolors.WARNING + "Error fetching pokemons. Retrying..." + bcolors.ENDC

    time.sleep(30)
