#!/usr/bin/env python

import tweepy, requests, os

def twitter_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def tweet(url, id, name, iv, attack, defense, stamina, cp, gender, height,
weight, types, form, move1, move2, lat, lng, disappear, config):

    googleMapsUrl = "http://maps.google.com/maps?z=8&t=m&q=loc:" + str(lat) + "+" + str(lng)
    if attack is not None:
        if '(' in move1 and '(' in move2:
            move = move1[:move1.index('(')] + "/" + move2[:move2.index('(')]
        else:
            move = move1 + "/" + move2
        infoPost = "#" + str(id) + " " + name + " " + disappear + ", IV:" + str(iv) + " (" + str(attack) + "/" + str(defense) + "/" + str(stamina) + "). cp" + str(cp) + ", "+ move + ", " + gender + ", " + height + "/" + weight + ". "
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
        except TweepError as err:
            print bcolors.WARNING + "Code: " + str(err.message[0]['code']) + " Message: " + err.message[0]['message'] + bcolors.ENDC
            continue
        break
