from dataclasses import dataclass
from random import *
from sys import settrace

@dataclass
class Character:
    _inventory: list
    _inventory_names: list
    _stamina: int = 20.0 # max stamina

    @property
    def inventory(self) -> list:
        ' return inventory member '
        return self._inventory

    @property
    def inventory_names(self) -> list:
        ' return inventory names '
        return self._inventory_names
    
    @inventory.setter
    def inventory(self, new_inventory: list):
        ' set new inventory value '
        self._inventory = new_inventory

        '''self.inventory_names = []
        for x in self.inventory:
            self.inventory_names.append(x.name)'''
    
    @inventory_names.setter
    def inventory_names(self, new_inventory_names: list):
        ' set new inventory names value '
        self.inventory_names = new_inventory_names

    @property
    def stamina(self) -> int:
        ' return stamina '
        return self._stamina

    @stamina.setter
    def stamina(self, new_stamina: int):
        ' set new stamina '
        self._stamina = new_stamina

    # stamina replenishment goes here
    def eat(self, snack):
        ' replenish user\'s stamina when snack is used '
        self.stamina = self.stamina + snack.regen
        # check stamina isn't over max
        if self.stamina > 20:
            self.stamina = 20


@dataclass
class Snack:
    _name: str
    _regen: int
    _count: int
    _msg: str

    @property
    def name(self) -> str:
        ' return name value '
        return self._name

    @property
    def regen(self) -> int:
        ' return regeneration value'
        return self._regen

    @property
    def count(self) -> int:
        ' return num. of item '
        return self._count

    @property
    def msg(self) -> str:
        ' return console message '
        return self._msg


@dataclass
class Question:
    _name: str # movie name
    _question: str
    _options: list
    _answer: str

    @property
    def name(self) -> str:
        ' return name of movie 4 inventory widget '
        return self._name

    @property
    def title(self) -> str:
        ' return movie title / N/A (could make subclass shut up) '
        return self._title

    @property
    def question(self) -> str:
        ' return question cue '
        return self._question
    
    @property
    def options(self) -> list:
        ' return list of possible answers '
        return self._options
    
    @property
    def answer(self) -> str:
        ' return correct answer value '
        return self._answer


# setup snacks/powerups, character, Q/As, board
snacks = {
    'FIZZY BUBBLECH': Snack('FIZZY BUBBLECH', 10, 1,
    'With great joy, you imbibe the FIZZY BUBBLECH. *brrp prp* *bfp*'),
    'DILL PICKLE': Snack('DILL PICKLE', 1, 10,
    'Like a snake, you swallow DILL PICKLE whole. Rejuvenated, you gain'),
    'NYC BAGEL': Snack('NYC BAGEL', 5, 5,
    'I <3 NY!!!!!!!!!!!! NYC BAGEL consumed.'),
    'MYSTERY CHEESE': Snack('MYSTERY CHEESE', 5, 5,
    'You eat the MYSTERY CHEESE. It\'s okay.')
}

character = Character([], [])

movies = ['50 First Dates', 'Grown Ups', 'Grown Ups 2',
'Click', 'The Longest Yard', 'Big Daddy', 'Blended',
'You Don\'t Mess With the Zohan', 'The Wedding Singer',
'Hotel Transylvania']

# questions - no. as key, obj as item
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
    ['9/03/1966', '9/09/1966', '10/03/1968', '11/04/1968'],
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

directions = ['MOVE LEFT', 'MOVE RIGHT', 'MOVE UP', 'MOVE DOWN']

# populate board, randomized
rows = [x for x in range(0, 10)]
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
board = []

for x in rows:
    for y in columns:
        coord = f'{str(x)} : {y}'
        board.append(coord)

# fill da board
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
