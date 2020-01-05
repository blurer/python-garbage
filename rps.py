#!/usr/bin/env python3
from random import randint

print('')
player=input('Rock (1), Paper (2), Scissors (3):? ')
print('')

if player == 1:
    person = 'Rock'
elif player == 2:
    person = 'Paper'
elif player == 3:
    person = 'Scissors'

chosen=randint(1,3)

if chosen == 1:
    computer = 'Rock'
elif chosen == 2:
    computer = 'Paper'
elif chosen == 3:
    computer = 'Scissors'

print(player, 'vs', computer)