#!/usr/bin/env python

import tweepy, requests, os

def twitter_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def tweet(url, id, name, iv, attack, defense, stamina, cp, gender, height,
weight, types, form, move1, move2, lat, lng, disappear, config):
    if iv is "0.0 %":
        tweet = "#" + str(id) + " " + name + " har blitt oppdaget og forsvinner " + disappear + ". IV: " + str(iv) + " % (" + str(attack) + "/" + str(defense) + "/" + str(stamina) + "). CP: " + str(cp) + ". Kjonn: " + gender + ". Moves: " + move1 + ", " + move2 + ". Hoyde: " + str(height) + ". Vekt: " + str(weight) + ". http://maps.google.com/maps?z=8&t=m&q=loc:" + str(lat) + "+" + str(lng)
    else:
        tweet = "#" + str(id) + " " + name + " har blitt oppdaget og forsvinner " + disappear + ". http://maps.google.com/maps?z=8&t=m&q=loc:" + str(lat) + "+" + str(lng)

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
        api.update_status(status=message)
