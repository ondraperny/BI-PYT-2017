# Python semestral work

import os
# clear display
print('\033[2J', end='')


def rotateRight():
    pass


def rotateLeft():
    pass


def mirror():
    pass


def invert():
    pass


def greyscale():
    pass


def lighten():
    pass


def darken():
    pass


def highlightEdge():
    pass

def loadInput():
    print('\033[2J')
    file = input('Zadejte jméno souboru:\n')
    while os.access(file, os.R_OK) == False:
        print('\033[2J', end='')
        print('Zadaný soubor nelze načíst, zadejte jiný:')
        file = input('Zadejte jméno souboru:\n')
    print('\033[2J', end='')
    return file

flag = 0
# interface
print('Program pro upravu obrazku, zadej jmeno souboru, ktery chces upravit: ')
file = loadInput()

while True:
    if flag == -1:
        print('Špatný výběr, volte znovu')
    else:
        print()

    print('Aktuální soubor: \"' + file + '\"' )
    print('''Seznam možností (vyber číslo a stiskni enter):
          0. exit - vypne program
          1. nový soubor - nechá uživatele zadat nový soubor
          2. rotace do prava o 90 stupňů
          3. rotace do leva o 90 stupňů
          4. zrcadlení obrazu
          5. inverze obrazu
          6. převod do odstínu šedi
          7. zesvětlení
          8. ztmavení
          9.zvýraznění hran''')
    flag = input()
    if flag == '0':
        print('\033[2J', end='')
        exit()
    elif flag == '1':
        file = loadInput()
    # elif flag == '2':
    # elif flag == '3':
    # elif flag == '4':
    # elif flag == '5':
    # elif flag == '6':
    # elif flag == '7':
    # elif flag == '8':
    # elif flag == '9':
    else:
        flag = -1
    print('\033[2J', end='')

