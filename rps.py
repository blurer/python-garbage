#!/usr/bin/env python3
from random import randint

print('')
player=input('Rock (r), Paper (p), Scissors (s):? ')

if player == 'r':
    print('Rock', end=' ')
elif input == 'p':
    print('Paper', end=' ')
elif input == 's':
    print('Scissors', end=' ')


chosen=randint(1,3)

if chosen == 1:
    computer = 'Rock'
elif chosen == 2:
    computer = 'Paper'
elif chosen == 3:
    computer = 'Scissors'

print( 'vs', computer)
