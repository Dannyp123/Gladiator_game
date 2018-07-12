from random import randint


def new_gladiator(health, rage, damage_low, damage_high, weapon_name):
    ''' int, int, int, int -> dict 
    '''
    new_glad = {
        'health': health,
        'rage': rage,
        'damage_low': damage_low,
        'damage_high': damage_high,
        'weapon': killing_weapons()[weapon_name]
    }
    return new_glad


def attack(attacker, defender):

    damage_dealt = randint(attacker['damage_low'], attacker['damage_high'])
    weapon_damage = attacker['weapon'] + damage_dealt
    critical = weapon_damage * 2
    if randint(1, 100) < attacker['rage']:
        health = defender['health'] - critical
        defender['health'] = max(health, 0)
        attacker['rage'] == 0
    else:
        health = defender['health'] - weapon_damage
        defender['health'] = max(health, 0)
        attacker['rage'] += 15
    return defender['health']


def killing_weapons():
    weapons = {'Battle Axe': 10, 'Stick': 5, 'Thors Hammer': 25}
    return weapons


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
