#!/usr/bin/env python

config = {
  'pokemons': """moltres, zapdos, articuno, mew, mewtwo, meganium, typhlosion,
  feraligatr, togetic, ampharos, unown, heracross, shuckle, delibird, skarmory,
  houndoom, donphan, smeargle, hitmontop, miltank, blissey, raikou, entei,
  suicune, lugia, ho-oh, celebi, larvitar, pupitar, tyranitar""",
  'latitude': "",
  'longitude': "",
  'sendingEmail': "", #Must be Gmail account
  'recievingEmail': "",
  'twitter' : {
    'consumer_key': "",
    'consumer_secret': "",
    'access_token': "",
    'access_token_secret': ""
    }
}

def getConfig():
    return config
