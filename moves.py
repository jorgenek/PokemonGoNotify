#!/usr/bin/env python

moves = {
    '13': 'Wrap(Normal) 25',
    '14': 'Hyper Beam(Normal) 120',
    '16': 'Dark Pulse(Dark) 45',
    '18': 'Sludge(Poison) 30',
    '21': 'Flame Wheel(Fire) 40',
    '22': 'Megahorn(Bug) 80',
    '24': 'Flamethrower(Fire) 55',
    '30': 'Psybeam(Psychic) 40',
    '31': 'Earthquake(Ground) 100',
    '32': 'Stone Edge(Rock) 80',
    '33': 'Ice Punch(Ice) 45',
    '35': 'Discharge(Electric) 35',
    '36': 'Flash Cannon(Steel) 60',
    '39': 'Ice Beam(Ice) 65',
    '40': 'Blizzard(Ice) 100',
    '47': 'Petal Blizzard(Grass) 65',
    '49': 'Bug Buzz(Bug) 75',
    '51': 'Night Slash(Dark) 30',
    '54': 'Submission(Fighting) 30',
    '56': 'Low Sweep(Fighting) 30',
    '57': 'Aqua Jet(Water) 25',
    '58': 'Aqua Tail(Water) 45',
    '59': 'Seed Bomb(Grass) 40',
    '60': 'Psyshock(Psychic) 40',
    '62': 'Ancient Power(Rock) 35',
    '63': 'Rock Tomb(Rock) 30',
    '64': 'Rock Slide(Rock) 50',
    '70': 'Shadow Ball(Ghost) 45',
    '74': 'Iron Head(Steel) 30',
    '77': 'Thunder Punch(Electric) 40',
    '78': 'Thunder(Electric) 100',
    '79': 'Thunderbolt(Electric) 55',
    '80': 'Twister(Dragon) 25',
    '83': 'Dragon Claw(Dragon) 35',
    '82': 'Dragon Pulse(Dragon) 65',
    '85': 'Draining Kiss(Fairy) 25',
    '87': 'Moonblast(Fairy) 85',
    '90': 'Sludge Bomb(Poison) 55',
    '95': 'Bulldoze(Ground) 35',
    '96': 'Mud Bomb(Ground) 30',
    '99': 'Signal Beam(Bug) 45',
    '100': 'X-Scissor(Bug) 35',
    '101': 'Flame Charge(Fire) 25',
    '102': 'Flame Burst(Fire) 30',
    '103': 'Fire Blast(Fire) 100',
    '104': 'Brine(Water) 25',
    '105': 'Water Pulse(Water) 35',
    '107': 'Hydro Pump(Water) 90',
    '108': 'Psychic(Psychic) 55',
    '115': 'Fire Punch(Fire) 40',
    '116': 'Solar Beam(Grass) 120',
    '118': 'Power Whip(Grass) 70',
    '126': 'Horn Attack(Normal) 25',
    '127': 'Stomp(Normal) 30',
    '131': 'Body Slam(Normal) 40',
    '200': 'Fury Cutter(Bug) 3',
    '202': 'Bite(Dark) 6',
    '203': 'Sucker Punch(Dark) 7',
    '204': 'Dragon Breath(Dragon) 6',
    '205': 'Thunder Shock(Electric) 5',
    '206': 'Spark(Electric) 7',
    '207': 'Low Kick(Fighting) 5',
    '208': 'Karate Chop(Fighting) 6',
    '209': 'Ember(Fire) 10',
    '212': 'Lick(Ghost) 5',
    '213': 'Shadow Claw(Ghost) 11',
    '214': 'Vine Whip(Grass) 7',
    '215': 'Razor Leaf(Grass) 15',
    '216': 'Mud Shot(Ground) 6',
    '217': 'Ice Shard(Ice) 15',
    '218': 'Frost Breath(Ice) 9',
    '219': 'Quick Attack(Normal) 10',
    '220': 'Scratch(Normal) 6',
    '221': 'Tackle(Normal) 12',
    '222': 'Pound(Normal) 7',
    '224': 'Poison Jab(Poison) 12',
    '226': 'Psycho Cut(Psychic) 7',
    '227': 'Rock Throw(Rock) 12',
    '229': 'Bullet Punch(Steel) 10',
    '230': 'Water Gun(Water) 6',
    '233': 'Mud Slap(Ground) 15',
    '234': 'Zen Headbutt(Psychic) 12',
    '235': 'Confusion(Psychic) 15',
    '237': 'Bubble(Water) 25',
    '239': 'Steel Wing(Steel) 15',
    '241': 'Rock Smash(Fighting) 15'
}

def getMoveName(move):
    if move in moves:
      return moves[move]
    else:
      return move
