#!/usr/bin/env python

import tweepy, requests, os
from collections import Counter

class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def twitter_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def tweet(url, id, name, iv, attack, defense, stamina, cp, gender, move1, move2, lat, lng, disappear, config):
    googleMapsUrl = "http://maps.google.com/maps?z=8&t=m&q=loc:" + str(lat) + "+" + str(lng)
    if attack is not None:
        if '(' in move1 and '(' in move2:
            move = move1[:move1.index('(')] + "/" + move2[:move2.index('(')]
        else:
            move = move1 + "/" + move2
        infoPost = "#" + str(id) + " " + name + " " + disappear + ", IV:" + str(iv) + " (" + str(attack) + "/" + str(defense) + "/" + str(stamina) + "). cp" + str(cp) + ", "+ str(move) + ", " + str(gender) + ". "
        tweet = infoPost + googleMapsUrl
        if len(tweet) > 140:
            overflow = len(tweet) - 140
            tweet = infoPost[:len(tweet)-overflow] + googleMapsUrl
    else:
        tweet = "#" + str(id) + " " + name + " forsvinner " + disappear + ". http://maps.google.com/maps?z=8&t=m&q=loc:" + str(lat) + "+" + str(lng)

    for i in range(0,10):
        try:
            api = twitter_api(config)
            filename = name + '.jpg'
            request = requests.get(url, stream=True)
            if request.status_code == 200:
                with open(filename, 'wb') as image:
                    for chunk in request:
                        image.write(chunk)
                api.update_with_media(filename, status=tweet, long=lng, lat=lat)
                os.remove(filename)
            else:
                print "Unable to download image"
                api.update_status(status=tweet)
        except tweepy.TweepError as err:
            print bcolors.WARNING + "Code: " + str(err.message[0]['code']) + " Message: " + err.message[0]['message'] + bcolors.ENDC
            continue
        break

def tweetGymStatus(cnt, total, config):
    tweet = "Av totalt " + str(total) + " gymer i Oslo:"

    for key, value in sorted(cnt.items(), key=lambda i: i[1], reverse=True):
        percent = "{0:.1f}".format(float(value) / total * 100) + "%"
        tweet = tweet + '\n' + key + ': ' + str(value) + ' (' + percent + ')'

    for i in range(0,1):
        try:
            api = twitter_api(config)
            api.update_status(status=tweet)
        except tweepy.TweepError as err:
            print bcolors.WARNING + "Code: " + str(err.message[0]['code']) + " Message: " + err.message[0]['message'] + bcolors.ENDC
            continue
        break
