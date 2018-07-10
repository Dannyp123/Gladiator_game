from core import *


def welcome():
    print('\t    Welcome to GLADIATOR')
    print('\tThe best action game around')


def get_name():
    name = input('\tWhat is your name?? ')
    print('\tHey there ' + name)
    return name


def battle(name, name2, d, p):
    while True:
        if is_dead(d) == True:
            print(name, 'died')
            print(name2, 'won')
            break
            exit()
        turn1(name, d, p)
        if is_dead(p) == True:
            print(name2, 'died')
            print(name, 'won')
            break
            exit()
        turn2(name, d, p)


def turn1(name, d, p):
    while True:
        print(name, 'turn')
        print('[A]TTACK')
        print('[H]EAL')
        print('[P]ASS')
        print('[Q]UIT')
        choice = input('Choose an option! ').upper().strip()
        if choice == 'A':
            attack(d, p)
            print(p['health'])
            break
        elif choice == 'H':
            heal(d)
            print(d['health'])
            break
        elif choice == 'P':
            print(name, 'passes')
            break
        elif choice == 'Q':
            exit()
        else:
            print('Please choose a valid option!!!')


def turn2(name2, d, p):

    while True:
        print(name2, 'turn')
        print('[A]TTACK')
        print('[H]EAL')
        print('[P]ASS')
        print('[Q]UIT')
        choice = input('Choose an option! ').upper().strip()
        if choice == 'A':
            attack(d, p)
            print(p['health'])
            break
        elif choice == 'H':
            heal(d)
            print(d['health'])
            break
        elif choice == 'P':
            print(name2, 'passes')
            break
        elif choice == 'Q':
            exit()
        else:
            print('Please choose a valid option!!!')


def main():
    welcome()
    name = get_name()
    name2 = get_name()
    d = new_gladiator(100, 0, 15, 20)
    p = new_gladiator(100, 0, 15, 20)
    battle(name, name2, d, p)


if __name__ == '__main__':
    main()
