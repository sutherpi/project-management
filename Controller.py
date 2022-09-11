from dataclasses import dataclass
from PySide6.QtWidgets import *
from Model import Character, Snack, Question, character, snacks, questions, rows, columns, movies, directions

@dataclass
class GameController():
    ''' a controller for events + connections
    within GUI/View.py
    '''
    app: QApplication
    character: Character
    console: QLabel
    question_label: QLabel
    answer: QComboBox
    submit_answer: QPushButton
    board_grid_layout: QGridLayout
    stamina_label: QLabel
    inventory_select: QListWidget
    use_item: QPushButton
    move_combobox: QComboBox
    move_button: QPushButton

    def update_console(self):
        ''' update console msgs based on:
            item used / tile changed / item found / answer submitted
        '''
        self.console.setText('''''')


    def update_stamina(self):
        ''' updates stamina label when depleted/items used '''
        # loss condition if stamina less than 0
        if self.character.stamina <= -1:
            QMessageBox(QMessageBox.Icon.Critical, 'GAME LOST',
            'Stamina is below zero. Game lost :(.').exec()

            self.app.exit()

        self.stamina_label.setText(f'Stamina: {self.character.stamina}')


    # move row changed
    # 


    # move button click
    def move_button_clicked(self, checked: bool):
        ''' user moves based on combobox direction '''
        move_combobox_index = self.move_combobox.currentIndex()

        # check selected direction isn't '-'
        if move_combobox_index != 0:
            print(directions[move_combobox_index - 1])
        else:
            QMessageBox(QMessageBox.Icon.Critical, 'Error: empty input',
            'Please select a direction to move!').exec()


    # use item click
    def use_item_clicked(self, checked: bool):
        ''' uses item + replenishes user's stamina '''
        # create list of names
        names = []
        for x in self.character.inventory:
            names.append(x.name)
        
        print(self.inventory_select.currentItem())

        # get text from inventory item
        # check if an item was connected
        if self.inventory_select.currentItem() == None:
            QMessageBox(QMessageBox.Icon.Critical, 'Error: no item selected',
            'Select an item to use!').exec()
        else:
            item = self.inventory_select.currentItem().text()

            if item in questions.keys():
                QMessageBox(QMessageBox.Icon.Critical, 'Error: can\'t use item',
                f'{item} is not consumable!').exec()

            elif item in snacks.keys():
                # get obj, value so can access stamina
                item_index = names.index(item)
                item = self.character.inventory[item_index]
                # remove item from inventory, update list widget
                self.character.inventory.remove(
                    item)
                self.inventory_select.clear()
                self.inventory_select.addItems(x.name for x in character.inventory)
                self.character.eat(item)
                self.update_stamina()

                QMessageBox(QMessageBox.Icon.Information, 'Item used',
                f'{item.name} used. + {item.regen} stamina!').exec()

    # submit answer click
    def submit_answer_clicked(self, checked: bool):
        ''' submits answer in qcheckbox row '''
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
                # update stamina
                self.character.stamina -= 1
                self.update_stamina()

                QMessageBox(
                    QMessageBox.Icon.Information, 'Answer incorrect.',
                    f'\'{user_answer}\' is the wrong answer. \n STAMINA -1.').exec()


