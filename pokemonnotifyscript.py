#!/usr/bin/env python

import requests, time, smtplib, getpass, json, datetime
from config import getConfig
from twitter import tweet
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

def getMoveName(move, moveList):
    if move in moveList:
        if moveList[move]['type']:
            if moveList[move]['damage']:
                return moveList[move]['name'] + '(' + moveList[move]['type'] +')' + ' ' + str(moveList[move]['damage'])
            else:
                return moveList[move]['name'] + '(' + moveList[move]['type'] +')'
        else:
            return moveList[move]['name'] + '(???)'
    else:
        return move

def formatId (id):
    if len(id) == 1:
        return "00" + id
    elif len(id) == 2:
        return "0" + id
    else:
        return id

def getGender(gender):
    if gender == "1":
        return "Male"

    elif gender == "2":
        return "Female"

    elif gender == "3":
        return "None"
    else:
        return None

def formatPokemonsToList(string):
    string = string.split(",")
    string = map(str.strip, string)
    string = map(str.lower, string)
    return string

def getPokemons():
    url = "https://nomaps.me/raw_data?by=oslo&&pokemon=true&pokestops=false&gyms=false&scanned=false&spawnpoints=false&swLat=59.69824204817713&swLng=10.259857177734377&neLat=60.02678442879232&neLng=11.000061035156252&alwaysperfect=true&raids=false"
    return requests.get(url).json()

def getMoves():
    url = "https://nomaps.me/static/data/moves.min.json"
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

def resizeImage(url):
    index = url.find('px-')
    if index >= 0:
        return url[:index-3] + "250" + url[index:]
    else:
        return url

def checkValidUrl(url):
    if url.startswith('http'):
        return url
    else:
        return "https:" + url

def notifyDiscovery(id, name, lat, lng, attack, defense, stamina, rarity,
gender, cp, move1, move2, iv, disappear_time, level):

    id = formatId(str(id))
    pageurl = 'http://bulbapedia.bulbagarden.net/wiki/File:' + id + str(name) +'.png'
    page = requests.get(pageurl)
    tree = html.fromstring(page.content)
    pokemonImageUrl = tree.xpath('//div[@class="fullImageLink"]//a/img/@src')[0]
    pokemonImageUrl = resizeImage(pokemonImageUrl)
    pokemonImageUrl = checkValidUrl(pokemonImageUrl)

    genderSign = getGender(gender)
    ivString = str(iv) + "%"
    pokemonDistance = haversine(float(latAnswear), float(lngAnswear), float(lat), float(lng))
    pokemonDistance = "{0:.2f}".format(pokemonDistance) + " km"
    #pokemonTypes = getPokemonTypes(types)

    print time.strftime("%d. %b %Y %H:%M:%S")
    print bcolors.OKGREEN + """#{id} {name} was discovered with:
    IV: {iv}
    Attack: {attack}
    Defense: {defense}
    Stamina: {stamina}
    Move1: {move1}
    Move2: {move2}
    Gender: {gender}
    CP: {cp}
    Level: {level}
    Disappears: {disappear}
    Rarity: {rarity}
    Distance: {distance}
    Latitude: {lat}
    Longitude: {lng}
    """.format(name=name, gender=genderSign, rarity=rarity, iv=ivString,
    attack=attack, defense=defense, stamina=stamina, move1=move1, move2=move2,
    distance=pokemonDistance, lat=lat, lng=lng, disappear=disappear_time, cp=cp,
    id=id, level=level) + bcolors.ENDC

    msg = MIMEMultipart('alternative')
    msg["From"] = fromEmail
    msg["To"] = toEmail
    msg["Subject"] = name.upper() + " was discovered!"

    body = """
    ID: {id}
    Name: {name}
    Rarity: {rarity}
    Disappears: {disappear}
    Distance: {distance}
    http://maps.google.com/maps?z=8&t=m&q=loc:{lat}+{lng}
    """.format(name=name, id=id, rarity=rarity, distance=pokemonDistance, lat=lat,
    lng=lng, disappear=disappear_time)

    htmlemail = """
<html>
      <body>
          <div style="margin:0!important;padding:0!important">
            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                <td bgcolor="#132240" align="center" style="padding-bottom:50px;">
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width:200px">
                        <tbody>
                          <tr>
                            <td>
                                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                    <tbody>
                                    <tr>
                                        <td>
                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                <tbody><tr>
                                                    <td align="center" style="font-size:25px;font-family:Helvetica,Arial,sans-serif;color:#f2c12e;padding-top:30px">#{id} {name}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center"><br><img src={url} tabindex="0" width="100"></td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>Disappears:</b> {disappear}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>Distance:</b> {distance}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>CP:</b> {cp}</td>
                                                </tr
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>IV:</b> {iv}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>Level:</b> {level}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>Attack:</b> {attack}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>Defense:</b> {defense}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>Stamina:</b> {stamina}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>Gender:</b> {gender}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>Move1:</b> {move1}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>Move2:</b> {move2}</td>
                                                </tr>
                                                <tr>
                                                    <td align="center" style="font-size:16px;line-height:25px;font-family:Helvetica,Arial,sans-serif;color:#d8d8d8"><b>Rarity:</b> {rarity}</td>
                                                </tr>
                                            </tbody></table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td align="center">
                                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                                <tbody><tr>
                                                    <td align="center" style="padding-top:25px">
                                                        <table border="0" cellspacing="0" cellpadding="0">
                                                            <tbody><tr>
                                                                <td align="center" style="border-radius:3px" bgcolor="#256F9C"><a href="http://maps.google.com/maps?z=8&t=m&q=loc:{lat}+{lng}" style="font-size:16px;font-family:Helvetica,Arial,sans-serif;color:#ffffff;text-decoration:none;color:#ffffff;text-decoration:none;border-radius:3px;padding:15px 25px;border:1px solid #256f9c;display:inline-block" target="_blank">
                                                                  Get directions</a></td>
                                                            </tr>
                                                        </tbody></table>
                                                    </td>
                                                </tr>
                                            </tbody></table>
                                        </td>
                                    </tr>
                                </tbody></table>
                            </td>
                        </tr>
                    </tbody></table>
                </td>
            </table>
          </div>
      </body>
  </html>
    """.format(url=pokemonImageUrl, name=name, gender=genderSign, rarity=rarity,
    iv=ivString, attack=attack, defense=defense, stamina=stamina, move1=move1,
    move2=move2, distance=pokemonDistance, lat=lat, lng=lng,
    disappear=disappear_time, cp=cp, id=id, level=level)

    msg.attach(MIMEText(body, "plain"))

    msg.attach(MIMEText(htmlemail, 'html'))


    if (iv > 90 and level > 20) or level == 30 or iv == 100 or name.lower() == "unown":
        print bcolors.HEADER + "Sending email" + bcolors.ENDC
        print
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(fromEmail, password)
        text = msg.as_string()
        server.sendmail(fromEmail, toEmail, text)
        server.quit()

    if config['twitter']['consumer_key'] and config['twitter']['consumer_secret'] and config['twitter']['access_token'] and config['twitter']['access_token_secret']:
        tweet(pokemonImageUrl, id, name, ivString, attack, defense, stamina, cp,
        genderSign, move1, move2, lat, lng,
        disappear_time, level, config['twitter'])
        print bcolors.HEADER + "Tweeted" + bcolors.ENDC

    cnt[name] += 1
    seenCount = len(discoveredList)
    print "Discovered pokemons so far is: " + str(seenCount)
    for key,value in sorted(cnt.iteritems()):
        print key, value
    print

config = getConfig()
send_url = "http://freegeoip.net/json"
r = requests.get(send_url)
j = json.loads(r.text)
yourlat = j['latitude']
yourlng = j['longitude']
print bcolors.OKBLUE + "-----------------------------------------------------------------------" + bcolors.ENDC

pokemons = formatPokemonsToList(config['pokemons'])
latAnswear = str(yourlat) if config['latitude'] == '' else config['latitude'].replace(",", ".")
lngAnswear = str(yourlng) if config['longitude'] == '' else config['longitude'].replace(",", ".")
fromEmail = addMailEnding(config['sendingEmail'])
toEmail = addMailEnding(config['recievingEmail'])
fromEmail = addMailEnding(config['sendingEmail'])

print "Pokemons: "
print bcolors.WARNING + config['pokemons'] + bcolors.ENDC
print "Latitude: " + bcolors.WARNING + latAnswear + bcolors.ENDC
print "Longitude: " + bcolors.WARNING + lngAnswear + bcolors.ENDC
print "Recieving email: " + bcolors.WARNING + toEmail + bcolors.ENDC
print "Sending email: " + bcolors.WARNING + str(fromEmail) + bcolors.ENDC

password = getpass.getpass("Input password for " + addMailEnding(config['sendingEmail']) + ":")

#List of pokemons that are discoverd so you won"t get spammed
discoveredList = []

moveList = getMoves()

while True:
    print "Scanning..."
    try:
        pokemonJson = getPokemons()

        for i in pokemonJson['pokemons']:
            if (i['pokemon_name'].lower() in pokemons and i['iv'] > 0) or i['iv'] > 81 or i['pokemon_name'].lower() == 'unown':
                if i['encounter_id'] not in discoveredList:
                    disappear_time = convertTimestampToTime(int(str(i['disappear_time'])[:-3]))
                    move1 = getMoveName(str(i['move_1']), moveList)
                    move2 = getMoveName(str(i['move_2']), moveList)
                    discoveredList.append(i['encounter_id'])
                    notifyDiscovery(i['pid'], i['pokemon_name'], i['latitude'],
                    i['longitude'], i['atk'], i['def'],
                    i['sta'], i['pokemon_rarity'],
                    i['gender'], i['cp'],
                    move1, move2, i['iv'], disappear_time, i['level'])
    except (ValueError, requests.exceptions.RequestException):
        print bcolors.WARNING + "Error fetching pokemons. Retrying..." + bcolors.ENDC

    time.sleep(120)
