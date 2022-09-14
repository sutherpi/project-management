from dataclasses import dataclass
from Model import Character, Snack, Question, character, snacks, questions, rows, columns, movies, directions
from random import *
# board_test

rows = [x for x in range(0, 10)]
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

board = []

for x in rows:
    for y in columns:
        coord = f'{str(x)} : {y}'
        board.append(coord)

# loop so add to 2d list
# loop over 2d list 2 add to gui
'''
board = [
    ['0: A', '0 : B', '0 : C'],
    ['1 : A', '1 : B', '1 : C'],
    ['2 : A', '2 : B', '2 : C']
]'''

questions = {
    '50 First Dates': Question('50 First Dates',
        'How many first dates does Sandler go on in this movie?',
        ['3', '50', 'None', '30'], '50'),
    'Grown Ups': Question('Grown Ups',
        'In Grown Ups, who plays Sandler’s love interest?',
        ['Salma Haylek', 'Drew Barrymore','Adam Sandler', 'Gwyneth Paltrow'],
        'Salma Haylek'),
    'Grown Ups 2': Question('Grown Ups 2',
        'How many years apart were the releases of Grown ups 1 and 2?',
        ['10', '4', '3', '5'], '3'),
    'Click': Question('Click',
    'Click is often compared to which movie?',
    ['Back to the Future', 'The Truman Show',
    'Almost Famous', 'The Disaster Artist'], 'Back to the Future'),
    'The Longest Yard': Question('The Longest Yard',
        'The Longest Yard was set in a prison called:',
        ['Allenville Penitentiary', 'Alcatraz',
        'Avenal State Prison', 'Louisiana State Penitentiary'],
        'Allenville Penitentiary'),
    'Big Daddy': Question('Big Daddy',
    'When was Big Daddy released?',
        ['2001', '1997', '1999', '1998'], '1999'),
    'Blended': Question('Blended',
    'What is the premise of this movie?',
    ['Sandler works as a Vitamix salesman',
    'Sandler is stuck at a resort with another family',
    'Sandler’s family reunion over Thanksgiving',
    'Sandler pursues a DJ career in New York'],
    'Sandler is stuck at a resort with another family'),
    'You Don\'t Mess With the Zohan': Question(
        'You Don\'t Mess With the Zohan',
        'What is Sandler’s favourite drink in this movie?',
        ['Fizzy Bubblech', 'Seltzer', 'Beer', 'Rosewater'], 'Fizzy Bubblech'),
    'The Wedding Singer': Question('The Wedding Singer',
    'In The Wedding Singer, Sandler lives in:',
    ['Canada', 'Washington', 'New York', 'New Jersey'], 'New Jersey'),
    'Hotel Transylvania': Question(
        'Hotel Transylvania',
        'Which character does Sandler play in Hotel Transylvania?',
        ['Murray the Mummy', 'Uncle Brian', 'Dracula', 'Wayne'], 'Dracula'),
    'DOB': Question('N/A', 'What is Adam’s date of birth?',
    ['9/03/1966', '9/04/1966', '10/03/1968', '11/04/1968'],
    '9/09/1966'),
    'Height': Question('N/A', 'How tall is Adam Sandler?',
    ['1.8m', '1.82m', '1.79m', '1.77m'], '1.77m'),
    'False': Question('N/A', 
    'Which of these is false?\n\nAdam sandler:',
    ['Was shortlisted for the role of Willy Wonka',
    'Held a funeral for his dog Meatball',
    'Was previously married to Drew Barrymore', 'Starred on The Cosby Show'],
    'Was previously married to Drew Barrymore'),
    'Eyes': Question('N/A', 'What is Adam’s eye colour?',
    ['Brown', 'Black', 'Hazel', 'Dark Brown'], 'Dark Brown'),
    'Companies': Question('N/A',
        'Which of these products/companies does not appear in one of Sandler’s films?',
    ['The US Army', 'Spam', 'Wholefoods', 'Popeye\'s'], 'Wholefoods')
}

snacks = {
    'FIZZY BUBBLECH': Snack('FIZZY BUBBLECH', 10, 1,
    'With great joy, you imbibe the FIZZY BUBBLECH. *brrp prp* *bfp*'),
    'DILL PICKLE': Snack('DILL PICKLE', 1, 10,
    'Like a snake, you swallow DILL PICKLE whole. Rejuvenated, you gain'),
    'NYC BAGEL': Snack('NYC BAGEL', 5, 3,
    'I <3 NY!!!!!!!!!!!! NYC BAGEL consumed.'),
    'MYSTERY CHEESE': Snack('MYSTERY CHEESE', 1, 5,
    'You eat the MYSTERY CHEESE. It\'s okay.')
}

def fill_board():
    ''' fill board w/ randomized snacks, start, questions'''
    # create items list 2 fill board with
    items = ['X'] # location of character

    for snack in snacks:
        for i in range(0, snacks[snack].count):
            items.append(snack)

    for question in questions:
        items.append(question)

    # add empty slots 2 items
    no_empty_slots = len(board) - len(items)
    for i in range(0, no_empty_slots):
        items.append('')

    # randomise order via shuffle
    shuffle(items)

    # fill board via dictionary!
    board_items = {}

    for coord in board:
        # add coord w/ corresponding item (match list indices)
        board_items[coord] = items[board.index(coord)]
    
    return board_items


board_items = fill_board()

# ID start point
location = 'X : Y'

for key in board_items:
    for item in board_items[key]:
        if item == 'X':
            location = key

print(location)

# move up
def move_up(coord):
    ' move character up '
    row = int(coord[0])
    column = coord[4]

    # check isnt topmost
    if row != rows[0]:
        new_row = rows[rows.index(row) - 1]
        new_coord = f'{new_row} : {column}'
        print(f'moved up from {coord} to {new_coord}.')
        
    else:
        print(f'Cannot move up - {coord} is already at edge of board.')


# move right
def move_right(coord):
    ' move character right '
    row = int(coord[0])
    column = coord[4]
    
    # check isnt rightmost
    if column != columns[-1]:
        new_column = columns[columns.index(column) + 1]
        new_coord = f'{row} : {new_column}'
        print(f'moved right from {coord} to {new_coord}.')
    else:
        print(f'Cannot move right - {coord} is already at edge of board.')


# move down
def move_down(coord):
    ' move character down '
    row = int(coord[0])
    column = coord[4]

    # check isnt topmost
    if row != rows[-1]:
        new_row = rows[rows.index(row) + 1]
        new_coord = f'{new_row} : {column}'
        print(f'moved down from {coord} to {new_coord}.')
        
    else:
        print(f'Cannot move down - {coord} is already at edge of board.')

move_down(location)

# move left
def move_left(coord):
    ' move character left '
    row = int(coord[0])
    column = coord[4]
    
    # check isnt rightmost
    if column != columns[0]:
        new_column = columns[columns.index(column) - 1]
        new_coord = f'{row} : {new_column}'
        print(f'moved left from {coord} to {new_coord}.')
    else:
        print(f'Cannot move left - {coord} is already at edge of board.')

move_left(location)