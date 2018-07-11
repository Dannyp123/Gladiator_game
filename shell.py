from core import *


def welcome():
    while True:
        print('\t    Welcome to GLADIATOR\n')
        print('\tThe game where you fight to the death!\n')
        print('\tDo You think you got what it takes?\n')
        print('\t     Hit Enter to see!')
        input()
        break


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
            print('\n\t****END--OF--THE--GAME****')
            break
            exit()

        turn(p, d)
        if is_dead(d) == True:
            print(d['name'], 'has pershied to a gruesome death...RIP')
            print()
            print(
                p['name'],
                'has become victorious and saved the world and wins the game')
            print('\n\t****END--OF--THE--GAME****')
            break
            exit()


def turn(attacker, defender):
    choice = ''
    while choice != 'Q':
        print(attacker['name'] + "'s", 'turn')
        print()
        print('>>> [A]TTACK')
        print('>>> [H]EAL')
        print('>>> [P]ASS')
        print('>>> [R]ampage')
        print('>>> [Q]UIT')

        choice = input(
            'Pick how you will destroy your ENEMY.... ').upper().strip()
        if choice == 'A':
            attack(attacker, defender)
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
            if attacker['health'] == 100:
                print('Can not heal because you are not injuried!!')
                print()
            elif attacker['rage'] < 10:
                print('\nNot enough power to heal!!\n')
            heal(attacker)
            print(attacker['name'], attacker['health'])
            break
        elif choice == 'P':
            print(attacker['name'], 'passes')
            break
        elif choice == 'R':
            if attacker['rage'] >= 20:
                print(
                    attacker['name'],
                    'used a RAMPAGE...killing everyone including himself, giving him the victory!!!'
                )
                print(attacker['name'], 'Wins The Game!!!!\n')
                print('\n\t****END--OF--THE--GAME****')
                exit()
            elif attacker['rage'] < 20:
                print('\nNot enough power to fuel your inner monster!!!')
                print()

        elif choice == 'Q':
            print(
                '\n{} felt pitty for the filthy animal {}, so he ended the game before there was a gruesome death!!!!'.
                format(attacker['name'], defender['name']))
            print('\n\t****END--OF--THE--GAME****')
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
    d = new_gladiator(100, 0, 15, 20)
    d['name'] = name
    p = new_gladiator(100, 0, 15, 20)
    p['name'] = name2
    print('Let the game Gladiator began!!!\n')
    battle(d, p)


if __name__ == '__main__':
    main()
