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
    defender['health'] -= damage_dealt
    attacker['rage'] += 15
    critical = damage_dealt * 2
    if critical:
        attacker['rage'] == 0
