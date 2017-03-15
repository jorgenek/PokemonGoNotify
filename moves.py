#!/usr/bin/env python

moves = {
    '13': 'Wrap(Normal) 60',
    '14': 'Hyper Beam(Normal) 150',
    '16': 'Dark Pulse(Dark) 80',
    '18': 'Sludge(Poison) 50',
    '20': 'Vice Grip(Normal) 35',
    '21': 'Flame Wheel(Fire) 60',
    '22': 'Megahorn(Bug) 90',
    '24': 'Flamethrower(Fire) 70',
    '26': 'Dig(Ground) 100',
    '28': 'Cross Chop(Fighting) 50',
    '30': 'Psybeam(Psychic) 70',
    '31': 'Earthquake(Ground) 120',
    '32': 'Stone Edge(Rock) 100',
    '33': 'Ice Punch(Ice) 50',
    '35': 'Discharge(Electric) 65',
    '36': 'Flash Cannon(Steel) 100',
    '39': 'Ice Beam(Ice) 90',
    '40': 'Blizzard(Ice) 130',
    '45': 'Aerial Ace(Flying) 55',
    '46': 'Drill Run(Ground) 80',
    '47': 'Petal Blizzard(Grass) 110',
    '49': 'Bug Buzz(Bug) 90',
    '50': 'Poison Fang(Poison) 35',
    '51': 'Night Slash(Dark) 50',
    '53': 'Bubble Beam(Water) 45',
    '54': 'Submission(Fighting) 60',
    '56': 'Low Sweep(Fighting) 40',
    '57': 'Aqua Jet(Water) 45',
    '58': 'Aqua Tail(Water) 50',
    '59': 'Seed Bomb(Grass) 55',
    '60': 'Psyshock(Psychic) 65',
    '62': 'Ancient Power(Rock) 70',
    '63': 'Rock Tomb(Rock) 70',
    '64': 'Rock Slide(Rock) 80',
    '65': 'Power Gem(Rock) 80',
    '66': 'Shadow Sneak(Ghost) 50',
    '67': 'Shadow Punch(Ghost) 40',
    '69': 'Ominous Wind(Ghost) 50',
    '70': 'Shadow Ball(Ghost) 100',
    '72': 'Magnet Bomb(Steel) 70',
    '74': 'Iron Head(Steel) 60',
    '77': 'Thunder Punch(Electric) 45',
    '78': 'Thunder(Electric) 100',
    '79': 'Thunderbolt(Electric) 80',
    '80': 'Twister(Dragon) 45',
    '82': 'Dragon Pulse(Dragon) 90',
    '83': 'Dragon Claw(Dragon) 50',
    '84': 'Disarming Voice(Fairy) 70',
    '85': 'Draining Kiss(Fairy) 60',
    '86': 'Dazzling Gleam(Fairy) 100',
    '87': 'Moonblast(Fairy) 130',
    '88': 'Play Rough(Fairy) 90',
    '89': 'Cross Poison(Poison) 40',
    '90': 'Sludge Bomb(Poison) 80',
    '91': 'Sludge Wave(Poison) 110',
    '92': 'Gunk Shot(Poison) 130',
    '95': 'Bulldoze(Ground) 80',
    '96': 'Mud Bomb(Ground) 55',
    '99': 'Signal Beam(Bug) 75',
    '100': 'X-Scissor(Bug) 45',
    '101': 'Flame Charge(Fire) 70',
    '102': 'Flame Burst(Fire) 70',
    '103': 'Fire Blast(Fire) 140',
    '104': 'Brine(Water) 60',
    '105': 'Water Pulse(Water) 70',
    '107': 'Hydro Pump(Water) 130',
    '108': 'Psychic(Psychic) 100',
    '111': 'Icy Wind(Ice) 60',
    '115': 'Fire Punch(Fire) 55',
    '116': 'Solar Beam(Grass) 180',
    '118': 'Power Whip(Grass) 90',
    '121': 'Air Cutter(Flying) 60',
    '122': 'Hurricane(Flying) 110',
    '123': 'Brick Break(Fighting) 40',
    '125': 'Swift(Normal) 60',
    '126': 'Horn Attack(Normal) 40',
    '127': 'Stomp(Normal) 55',
    '129': 'Hyper Fang(Normal) 80',
    '131': 'Body Slam(Normal) 50',
    '133': 'Struggle(Normal) 35',
    '200': 'Fury Cutter(Bug) 3',
    '201': 'Bug Bite(Bug) 5',
    '202': 'Bite(Dark) 6',
    '203': 'Sucker Punch(Dark) 7',
    '204': 'Dragon Breath(Dragon) 6',
    '205': 'Thunder Shock(Electric) 5',
    '206': 'Spark(Electric) 6',
    '207': 'Low Kick(Fighting) 6',
    '208': 'Karate Chop(Fighting) 8',
    '209': 'Ember(Fire) 10',
    '210': 'Wing Attack(Flying) 8',
    '211': 'Peck(Flying) 10',
    '212': 'Lick(Ghost) 5',
    '213': 'Shadow Claw(Ghost) 9',
    '214': 'Vine Whip(Grass) 7',
    '215': 'Razor Leaf(Grass) 13',
    '216': 'Mud Shot(Ground) 5',
    '217': 'Ice Shard(Ice) 12',
    '218': 'Frost Breath(Ice) 10',
    '219': 'Quick Attack(Normal) 8',
    '220': 'Scratch(Normal) 6',
    '221': 'Tackle(Normal) 5',
    '222': 'Pound(Normal) 7',
    '223': 'Cut(Normal) 5',
    '224': 'Poison Jab(Poison) 10',
    '225': 'Acid(Poison) 9',
    '226': 'Psycho Cut(Psychic) 5',
    '227': 'Rock Throw(Rock) 12',
    '228': 'Metal Claw(Steel) 8',
    '229': 'Bullet Punch(Steel) 9',
    '230': 'Water Gun(Water) 5',
    '231': 'Splash(Water) 0',
    '233': 'Mud Slap(Ground) 15',
    '234': 'Zen Headbutt(Psychic) 12',
    '235': 'Confusion(Psychic) 20',
    '236': 'Poison Sting(Poison) 5',
    '237': 'Bubble(Water) 12',
    '238': 'Feint Attack(Dark) 10',
    '239': 'Steel Wing(Steel) 11',
    '241': 'Rock Smash(Fighting) 15',
    '243': 'Counter(Fighting) 12',
    '244': 'Powder Snow(Ice) 6',
    '245': 'Close Combat(Fighting) 100',
    '247': 'Focus Blast(Fighting) 140',
    '248': 'Aurora Beam(Ice) 80',
    '249': 'Charge Beam(Electric) 8',
    '251': 'Wild Charge(Electric) 90',
    '252': 'Zap Cannon(Electric) 140',
    '254': 'Avalanche(Ice) 90',
    '255': 'Air Slash(Flying) 14',
    '256': 'Brave Bird(Flying) 90',
    '257': 'Sky Attack(Flying) 70',
    '258': 'Sand Tomb(Ground 80',
    '259': 'Rock Blast(Rock) 50',
    '260': 'Infestation(Bug) 10',
    '261': 'Struggle Bug(Bug) 15',
    '262': 'Silver Wind(Bug) 70',
    '263': 'Astonish(Ghost) 8',
    '264': 'Hex(Ghost) 10',
    '266': 'Iron Tail(Steel) 15',
    '267': 'Gyro Ball(Steel) 80',
    '268': 'Heavy Slam(Steel) 70',
    '272': 'Grass Knot(Grass) 90',
    '273': 'Energy Ball(Grass) 90',
    '274': 'Extrasensory(Psychic) 12',
    '275': 'Futuresight(Psychic) 120',
    '276': 'Mirror Coat(Psychic) 60',
    '279': 'Crunch(Dark) 70',
    '280': 'Foul Play(Dark) 70',
    '281': 'Hidden Power(Normal) 15'
}

def getMoveName(move):
    if move in moves:
        return moves[move]
    else:
        return move
