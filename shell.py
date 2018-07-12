from core import *
import time


def welcome():
    while True:
        print('\t     Welcome to GLADIATOR\n')
        print('\tThe game where you fight to the death!\n')
        print('\tDo You think you got what it takes?\n')
        print('\t     Hit Enter to see!')
        input()
        break


def what_weapon(prompt):
    while True:
        weapon = input(prompt).strip().title()
        if weapon == 'Battle Axe':
            return weapon
        elif weapon == 'Stick':
            return weapon
        elif weapon == 'Thors Hammer':
            return weapon
        elif weapon == 'Pan':
            return weapon
        elif weapon == 'M-16':
            return weapon
        else:
            print('choose a real weapon!')


def get_name():
    name = input('What is your name, mighty gladiator? ').strip().title()
    print('Welcome to Gladiator You must fight to the DEATH ' + name)
    return name


def battle(d, p):
    while True:
        turn(d, p)
        if is_dead(p) == True:
            print(p['name'], 'has pershied to a gruesome death...RIP')
            print()
            print(
                d['name'],
                'has become victorious and saved the world and wins the game')
            print('\n\t****END--OF--GLADIATORS****')
            break
            exit()

        turn(p, d)
        if is_dead(d) == True:
            print(d['name'], 'has pershied to a gruesome death...RIP')
            print()
            print(
                p['name'],
                'has become victorious and saved the world and wins the game')
            print('\n\t****END--OF--GLADIATORS****')
            break
            exit()


def turn(attacker, defender):
    choice = ''
    while choice != 'C':
        print(attacker['name'] + "'s", 'turn')
        print()
        print('>>> [A]TTACK <<<')
        print('>>> [H]EAL <<<')
        print('>>> [P]ASS <<<')
        print('>>> [R]AMPAGE <<<')
        print('>>> [C]OWARDS WAY OUT <<<')

        choice = input(
            'Pick how you will destroy your ENEMY.... ').upper().strip()
        if choice == 'A':
            attack(attacker, defender)
            print(attacker['name'], 'is attacking your gladiator!!')
            time.sleep(1)
            print()
            print('\nWOW....{} attacked {}, that was gruesome!!'.format(
                attacker['name'], defender['name']))
            print()
            print('Health of', defender['name'], ':', defender['health'])
            print('Health of', attacker['name'], ':', attacker['health'])
            print()
            print('Rage of', defender['name'], ';', defender['rage'])
            print('Rage of', attacker['name'], ':', attacker['rage'])
            print()

            break
        elif choice == 'H':
            print('Healing Your Gladiator......')
            time.sleep(4)
            print()
            if attacker['health'] == 100:
                print('Can not heal because you are not injuried!!')
                print()
            elif attacker['rage'] < 10:
                print('\nNot enough power to heal!!\n')
            print()
            heal(attacker)
            print(attacker['name'], attacker['health'])
            break
        elif choice == 'P':
            print(attacker['name'], 'passes')
            break
        elif choice == 'R':
            if attacker['rage'] >= 20:
                print()
                print('Poor sucker....*evil laugh*')
                print('Building the power from within....')
                time.sleep(2)
                print('....KAABOOOOM')
                time.sleep(1)
                print(
                    attacker['name'],
                    'used a RAMPAGE...killing everyone including himself, giving him the victory\n!!!'
                )
                print(attacker['name'], 'Wins The Game!!!!\n')
                print('\n\t****END--OF--GLADIATORS****')
                exit()
            elif attacker['rage'] < 20:
                print('\nNot enough power to fuel your inner monster!!!')
                print()

        elif choice == 'C':
            print(
                '\n{} felt pitty for the filthy animal {}, so he ended the game before there was a gruesome death!!!!'.
                format(attacker['name'], defender['name']))
            print('\n\t****END--OF--GLADIATORS****')
            exit()
        else:
            print('Please choose a valid option!!!')


def main():
    welcome()
    print()
    name = get_name()
    print()
    name2 = get_name()
    print()
    weapons = killing_weapons()
    print('\nHere are your choices....')
    for weapon_name, dmg in weapons.items():
        print('\n{} with a damage of {}'.format(weapon_name, dmg))
    weapon = what_weapon('\nChose your weapon of choice!! ')
    if weapon == 'Battle Axe':
        print('\nYou have picked the mighty Battle Axe, killer of man!!')
    elif weapon == 'Stick':
        print(
            '\nYou have picked the puny stick, great for walking not fighting!!'
        )
    elif weapon == 'Thors Hammer':
        print(
            '\nYou have picked the greatest of all weapons, it has SHOCKING results!!'
        )
    elif weapon == 'Pan':
        print(
            "\nYou have picked the mighty pan, good at cooking your gladiator's rage"
        )
    elif weapon == 'M-16':
        print(
            '\nYou have picked the common but powerful M-16, blows your defender away!!'
        )
    d = new_gladiator(100, 0, 15, 20, weapon)
    d['name'] = name
    p = new_gladiator(100, 0, 15, 20, weapon)
    p['name'] = name2

    print('\n\tLet the game Gladiator began!!!\n')
    battle(d, p)


if __name__ == '__main__':
    main()
