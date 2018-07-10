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
    critical = damage_dealt * 2
    if randint(1, 100) < attacker['rage']:
        defender['health'] = defender['health'] - critical
        attacker['rage'] == 0
    else:
        defender['health'] = defender['health'] - damage_dealt
        attacker['rage'] += 15
    return defender['health']


def heal_glad(gladiator):
    if gladiator['rage'] >= 10 and gladiator['health'] <= 95:
        gladiator['rage'] = gladiator['rage'] - 10
        gladiator['health'] = gladiator['health'] + 5
    else:
        return None
