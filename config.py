#!/usr/bin/env python

config = {
  'pokemons': """moltres, zapdos, articuno, mew, mewtwo, meganium, typhlosion,
  feraligatr, togetic, ampharos, unown, heracross, shuckle, delibird, skarmory,
  houndoom, donphan, smeargle, hitmontop, miltank, blissey, raikou, entei,
  suicune, lugia, ho-oh, celebi, larvitar, pupitar, tyranitar""",
  'latitude': "",
  'longitude': "",
  'distance': 1.5, #Double in km
  'sendingEmail': "", #Must be Gmail account
  'recievingEmail': ""
}

def getConfig():
    return config
