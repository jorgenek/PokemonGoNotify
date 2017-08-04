#!/usr/bin/env python

config = {
  'pokemons': """moltres, zapdos, articuno, mew, mewtwo, meganium,
  typhlosion, feraligatr, ampharos, unown, heracross, delibird, smeargle,
  corsola, blissey, raikou, entei, suicune, lugia, ho-oh, celebi, tyranitar,
  snorlax, dragonite, lapras, chansey, hitmontop, hitmonlee, hitmonchan,
  togetic, miltank, porygon, aerodactyl, kabutops, omastar,
  charizard, blastoise, venusaur, kangaskhan, tauros, farfetch'd""",
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
