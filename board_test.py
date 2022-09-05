# board_test

rows = [x for x in range(0, 10)]
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

board = []
board_items = {}

for x in rows:
    for y in columns:
        coord = f'{str(x)}:{y}'
        board.append(coord)
        board_items[coord] = '1'

'''for coord in board:
    print(coord)
    print(board_items[coord])
'''

# loop so add to 2d list
# loop over 2d list 2 add to gui