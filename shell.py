from core import *


def welcome():
    print('\t    Welcome to GLADIATOR')
    print('\tThe best action game around')


def get_name():
    name = input('What is your name?? ')
    print('Hey there ' + name)
    return name


def battle(d, p):
    while True:
        turn(d, p)
        if is_dead(p) == True:
            print(p['name'], 'died')
            print(d['name'], 'won')
            break
            exit()

        turn(p, d)
        if is_dead(d) == True:
            print(d['name'], 'died')
            print()
            print(p['name'], 'won')
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
            print('Health of', defender['name'], defender['health'])
            print()
            print('Health of', attacker['name'], attacker['health'])
            print()
            print('Rage of', defender['name'], defender['rage'])
            print()
            print('Rage of', attacker['name'], attacker['rage'])

            break
        elif choice == 'H':
            heal(attacker)
            print(attacker['name'], attacker['health'])
            break
        elif choice == 'P':
            print(attacker['name'], 'passes')
            break
        elif choice == 'R':
            if attacker['rage'] > 20:
                print(
                    attacker['name'],
                    'used a RAMPAGE....he sacrifies thereself for the WORLD...'
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
