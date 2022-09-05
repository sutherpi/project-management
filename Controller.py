from dataclasses import dataclass
from inspect import CORO_CLOSED
from msilib.schema import Billboard
from multiprocessing.connection import answer_challenge
from PySide6.QtWidgets import *
from Model import Character, Snack, character, snacks, questions, rows, columns

@dataclass
class GameController():
    ''' a controller for events + connections
    within GUI/View.py
    '''
    console: QLabel
    question_label: QLabel
    answer: QComboBox
    submit_answer: QPushButton
    board_grid_layout: QGridLayout
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
        answer_index = self.answer.currentIndex()

        # check whether input is empty
        if answer_index == 0:
            QMessageBox(
                QMessageBox.Icon.Critical, 'Error: empty input',
                'Please select an answer!').exec()
        else:
            # check is answer is correct
            user_answer = questions[
                'You Don\'t Mess With the Zohan'
                ].options[answer_index - 1]
            correct_answer = questions[
                'You Don\'t Mess With the Zohan'
                ].answer

            if user_answer == questions[
                'You Don\'t Mess With the Zohan'
                ].answer:
                QMessageBox(
                    QMessageBox.Icon.Information, 'Answer correct!',
                    f'\'{user_answer}\' is the correct answer.').exec()
            else:
                QMessageBox(
                    QMessageBox.Icon.Information, 'Answer incorrect.',
                    f'\'{user_answer}\' is the wrong answer.').exec()


    def inventory_select_currentRowChanged(self):
        ' update console based on item selected '
        pass

