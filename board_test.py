from dataclasses import dataclass
from Model import Character, Snack, Question, character, snacks, questions, rows, columns, movies, directions
from random import *
# board_test

character.inventory = [questions[x] for x in questions]

print(character.inventory)

check = []

for x in character.inventory:
    if x.name in movies:
        check.append(x.name)

if check == movies:
    print('game won!')
