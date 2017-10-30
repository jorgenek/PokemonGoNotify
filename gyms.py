#!/usr/bin/env python

import requests, time, smtplib, getpass, json, datetime
from collections import Counter
from config import getConfig
from twitter import tweet, tweetGymStatus

error = False

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def getGyms():
    url = "https://nomaps.me/raw_data?by=oslo&&pokemon=false&pokestops=false&gyms=true&scanned=false&spawnpoints=false&swLat=59.69824204817713&swLng=10.259857177734377&neLat=60.02678442879232&neLng=11.000061035156252&alwaysperfect=true&raids=false"
    return requests.get(url).json()

def getTeamName(number):
  if (number == 1):
    return 'Mystic'
  elif (number == 2):
    return 'Valor'
  elif (number == 3):
    return 'Instinct'
  else:
    return 'None'

print bcolors.OKBLUE + "-----------------------------------------------------------------------" + bcolors.ENDC

config = getConfig()

while True:
    try:
        cnt = Counter()
        error = False
        gymJson = getGyms()
        totalGyms = len(gymJson['gyms'])

        for i in gymJson['gyms']:
            teamName = getTeamName(i['team_id'])
            cnt[teamName] += 1

        print time.strftime("%d. %b %Y %H:%M:%S")
        print "Total gyms scanned: " + str(totalGyms)
        for key,value in sorted(cnt.items(), key=lambda i: i[1], reverse=True):
            percent = "{0:.1f}".format(float(value) / totalGyms * 100) + "%"
            print key + ':', value, '(' + percent + ')'

        if config['twitter']['consumer_key'] and config['twitter']['consumer_secret'] and config['twitter']['access_token'] and config['twitter']['access_token_secret']:
            tweetGymStatus(cnt, totalGyms, config['twitter'])
        print bcolors.OKBLUE + "-----------------------------------------------------------------------" + bcolors.ENDC

    except (ValueError, requests.exceptions.RequestException):
        error = True
        print bcolors.WARNING + "Error fetching gyms. Retrying..." + bcolors.ENDC

    if error:
        time.sleep(300)
    else:
        time.sleep(3600)
