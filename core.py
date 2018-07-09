from random import randint


def new_gladiator(health, rage, damage_low, damage_high):
    ''' int, int, int, int -> dict 
    '''
    new_glad = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high
    }
    return new_glad


def attack(attacker, defender):

    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    attacker['rage'] = 0
    critical = damage_dealt * 2
    if randint(1, 100) < attacker['rage']:
        defender['health'] = defender['health'] - critical
        attacker['rage'] == 0
    else:
        defender['health'] = defender['health'] - damage_dealt
        attacker['rage'] += 15
