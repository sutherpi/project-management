from ast import Num


directions = ['MOVE LEFT', 'MOVE RIGHT', 'MOVE UP', 'MOVE DOWN']

rows = [(x for x in range(0, 3))]
columns = ['A', 'B', 'C']

board = ['0 : A', '0 : B', '0 : C', '1 : A', '1 : B', '1 : C', '2 : A', '2 : B', '2 : C']

for coord in board:

direction = 'MOVE LEFT'

def move(direction, coord):
    row = coord[0]
    column = coord[4]

    if direction == 'MOVE LEFT':
        # check not @ left of board
        if row != rows[0]:
            new_row = row - 1
            new_coord = f'{new_row} : {column}'
        else:
            print(f'Cannot {direction.lower()} - {} would be out ')
    elif direction == 'MOVE RIGHT':
        # check not @ right of board
        if row != rows[-1]:
            new_row = row + 1
        
    elif direction == 'MOVE UP':

    elif direction == 'MOVE DOWN':


move(direction, '0 : A')