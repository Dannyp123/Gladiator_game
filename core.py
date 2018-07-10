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
        health = defender['health'] - critical
        defender['health'] = max(health, 0)
        attacker['rage'] == 0
    else:
        health = defender['health'] - damage_dealt
        defender['health'] = max(health, 0)
        attacker['rage'] += 15
    return defender['health']


def heal(gladiator):
    if gladiator['rage'] >= 10:
        gladiator['rage'] = gladiator['rage'] - 10
        health = gladiator['health'] + 5
        gladiator['health'] = min(100, health)
    else:
        gladiator['rage'] = 0


def is_dead(gladiator):
    if gladiator['health'] <= 0:
        return True
