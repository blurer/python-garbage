#!/usr/bin/env python3
from random import randint

print('')
player=input('Rock (r), Paper (p), Scissors (s):? ')

if player == "r":
    player = 'Rock'
elif player == "p":
    player = 'Paper'
elif player == "s":
    player = 'Scissors'


chosen=randint(1,3)

if chosen == 1:
    computer = 'Rock'
elif chosen == 2:
    computer = 'Paper'
elif chosen == 3:
    computer = 'Scissors'

print(player, 'vs', computer)
if player == computer:
    print('DRAW')