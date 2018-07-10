from core import *


def welcome():
    print('\t    Welcome to GLADIATOR')
    print('\tThe best action game around')


def get_name():
    name = input('\tWhat is your name?? ')
    print('\tHey there ' + name)
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
            print(p['name'], 'won')
            break
            exit()


def turn(attacker, defender):
    choice = ''
    while choice != 'Q':
        print(attacker['name'], 'turn')
        print('[A]TTACK')
        print('[H]EAL')
        print('[P]ASS')
        print('[Q]UIT')
        choice = input('Choose an option! ').upper().strip()
        if choice == 'A':
            attack(attacker, defender)
            print(defender['health'])
            break
        elif choice == 'H':
            heal(attacker)
            print(attacker['health'])
            break
        elif choice == 'P':
            print(attacker['name'], 'passes')
            break
        elif choice == 'Q':
            exit()
        else:
            print('Please choose a valid option!!!')


def main():
    welcome()
    print()
    name = get_name()
    print()
    name2 = get_name()
    d = new_gladiator(100, 0, 15, 20)
    d['name'] = name
    p = new_gladiator(100, 0, 15, 20)
    p['name'] = name2
    battle(d, p)


if __name__ == '__main__':
    main()
