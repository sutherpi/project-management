from dataclasses import dataclass
import random

@dataclass
class Character:
    _inventory: list
    _stamina: int = 20 # max stamina

    @property
    def inventory(self) -> list:
        ' return inventory member '
        return self._inventory
    
    @inventory.setter
    def inventory(self, new_inventory: list):
        ' set new inventory value '
        self.inventory = new_inventory

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
        print(f'stamina + {snack.regen}! New stamina: {self.stamina}')


@dataclass
class Snack:
    _name: str
    _regen: int
    _count: int

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


@dataclass
class Question:
    _question: str
    _options: list
    _answer: str

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
    'FIZZY BUBBLECH': Snack('FIZZY BUBBLECH', 10, 1),
    'DILL PICKLE': Snack('DILL PICKLE', 1, 10),
    'NYC BAGEL': Snack('NYC BAGEL', 5, 3),
    'MYSTERY CHEESE': Snack('MYSTERY CHEESE', 1, 5)
}

character = Character([])

# questions - no. as key, obj as item
questions = {
    '50 First Dates': Question(
        'How many first dates does Sandler go on in this movie?',
        ['3', '50', 'None', '30'], '50'),
    'Grown Ups': Question(
        'In Grown Ups, who plays Sandler’s love interest?',
        ['Salma Haylek', 'Drew Barrymore','Adam Sandler', 'Gwyneth Paltrow'],
        'Salma Haylek'),
    'Grown Ups 2': Question(
        'How many years apart were the releases of Grown ups 1 and 2?',
        ['10', '4', '3', '5'], '3'),
    'Click': Question('Click is often compared to which movie?',
    ['Back to the Future', 'The Truman Show',
    'Almost Famous', 'The Disaster Artist'], 'Back to the Future'),
    'The Longest Yard': Question(
        'The Longest Yard was set in a prison called:',
        ['Allenville Penitentiary', 'Alcatraz',
        'Avenal State Prison', 'Louisiana State Penitentiary'],
        'Allenville Penitentiary'),
    'Big Daddy': Question('When was Big Daddy released?',
        ['2001', '1997', '1999', '1998'], '1999'),
    'Blended': Question('What is the premise of this movie?',
    ['Sandler works as a Vitamix salesman',
    'Sandler is stuck at a resort with another family',
    'Sandler’s family reunion over Thanksgiving',
    'Sandler pursues a DJ career in New York'],
    'Sandler is stuck at a resort with another family'),
    'You Don\'t Mess With the Zohan': Question(
        'What is Sandler’s favourite drink in this movie?',
        ['Fizzy Bubblech', 'Seltzer', 'Beer', 'Rosewater'], 'Fizzy Bubblech'),
    'The Wedding Singer': Question('In The Wedding Singer, Sandler lives in:',
    ['Canada', 'Washington', 'New York', 'New Jersey'], 'New Jersey'),
    'Hotel Transylvania': Question(
        'Which character does Sandler play in Hotel Transylvania?',
        ['Murray the Mummy', 'Uncle Brian', 'Dracula', 'Wayne'], 'Dracula'),
    'DOB': Question('What is Adam’s date of birth?',
    ['9/03/1966', '9/04/1966', '10/03/1968', '11/04/1968'],
    '9/09/1966'),
    'Height': Question('How tall is Adam Sandler?',
    ['1.8m', '1.82m', '1.79m', '1.77m'], '1.77m'),
    'False': Question('Which of these is false?\n\nAdam sandler:',
    ['Was shortlisted for the role of Willy Wonka',
    'Held a funeral for his dog Meatball',
    'Was previously married to Drew Barrymore', 'Starred on The Cosby Show'],
    'Was previously married to Drew Barrymore'),
    'Eyes': Question('What is Adam’s eye colour?',
    ['Brown', 'Black', 'Hazel', 'Dark Brown'], 'Dark Brown'),
    'Companies': Question(
        'Which of these products/companies does not appear in one of Sandler’s films?',
    ['The US Army', 'Spam', 'Wholefoods', 'Popeye\'s'], 'Wholefoods')
}

# populate board, randomized
rows = [x for x in range(0, 10)]
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
board = {}

for row in range(0, len(rows)):
    for column in range(0, len(columns)):
        coord = f'{rows[row]} : {columns[column]}'
        board[coord] = ''

print(board['1 : A'])
# practice
'''
for snack in snacks:
    # access object via str key
    snack = snacks[snack]

    print(f'{snack.name} consumed! Your Stamina is now: {snack.regen + character.stamina}\n')'''

# practice adding 2 inventory
#character.inventory.append(snacks['FIZZY BUBBLECH'])
#print(character.inventory[0].name)
