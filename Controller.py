from dataclasses import dataclass
from multiprocessing.connection import answer_challenge
from PySide6.QtWidgets import *
from Model import Character, Snack, character, snacks, questions

@dataclass
class GameController():
    ''' a controller for events + connections
    within GUI/View.py
    '''
    console: QLabel
    question_label: QLabel
    answer: QComboBox
    submit_answer: QPushButton

    # board here
    stamina_label: QLabel
    inventory_select: QListWidget
    use_item: QPushButton
    #move_button = QPushButton

    def update_console(self):
        ''' update console msgs based on:
            item used / tile changed / item found / answer submitted
        '''
        self.console.setText('''''')

    def update_stamina(self):
        ' updates stamina label when depleted/items used '
        self.stamina_label.setText(f'Stamina: {character.stamina}')

    def submit_answer_clicked(self, checked: bool):
        ' submits answer in qcheckbox row '
        global answer
        global answer_index

        answer_index = self.answer.currentIndex()
        print(answer_index)
        
        # figure out if answer is correct
        print(self.answers) #####



    def inventory_select_currentRowChanged(self):
        ' update console based on item selected '
        pass



