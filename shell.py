from core import *


def welcome():
    while True:
        print('\t    Welcome to GLADIATOR\n')
        print('\tThe game where you fight to the death!')
        print('\tDo You think you got what it takes?')
        print('\tHit Enter to see!')
        input()
        break


def get_name():
    name = input('What is your name, mighty gladiator? ')
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
                'has become victories and saved the world and wins the game')
            break
            exit()

        turn(p, d)
        if is_dead(d) == True:
            print(d['name'], 'has pershied to a gruesome death...RIP')
            print()
            print(
                p['name'],
                'has become victories and saved the world and wins the game')
            break
            exit()


def turn(attacker, defender):
    print('Begin Gladiator!!!\n')
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

            break
        elif choice == 'H':
            if attacker['health'] == 100:
                print('Can not heal because you are not injuried!!')
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
                    'used a RAMPAGE....KAAABOOOOM...he sacrifies himself for the WORLD and wins the game...'
                )
                exit()
            elif attacker['rage'] < 20:
                print('\nNot enough power to fuel your inner monster!!!')
                print()

        elif choice == 'Q':
            print('\n{}felt pitty for {},you filthy animal!!!!'.format(
                attacker['name'], defender['name']))
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
    battle(d, p)


if __name__ == '__main__':
    main()
