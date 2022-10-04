from dataclasses import dataclass
from PySide6.QtWidgets import *
from Model import Character, Snack, Question, character, snacks, questions, rows, columns, movies, directions, board_items, location
from PySide6.QtGui import QPixmap
import os

@dataclass
class GameController():
    ''' a controller for events + connections
    within GUI/View.py
    '''
    app: QApplication
    location: str
    moves: int
    board_items: dict
    character: Character
    console: QLabel
    question: QWidget
    question_label: QLabel
    image_label: QLabel
    answer: QComboBox
    submit_answer: QPushButton
    board_grid_layout: QGridLayout
    board_widget: QWidget
    stamina_label: QLabel
    inventory_select: QListWidget
    use_item: QPushButton
    move_combobox: QComboBox
    move_button: QPushButton


    def load_photo(self, name, label: QLabel):
        ''' displays product photo in qlabel!!!! '''
        # path 2 python file where pictures are
        path = os.path.dirname(os.path.abspath(__file__))
        pixmap = QPixmap(os.path.join(
            path, '{}.png'.format(name.replace(' ', '_').lower()))).scaledToHeight(175)

        label.setPixmap(pixmap)


    def update_console(self, msg):
        ''' update console msgs based on:
            item used / tile changed / item found / answer submitted
        '''
        self.console.setText(f'{msg}')


    def update_stamina(self):
        ''' updates stamina label when depleted/items used '''
        # loss condition if stamina less than 0
        if self.character.stamina < 0:
            QMessageBox(QMessageBox.Icon.Critical, 'GAME LOST',
            'Stamina is below zero. Game lost :(').exec()

            self.app.exit()
        elif self.character.stamina < 5:
            self.stamina_label.setStyleSheet('color: red;')
        elif self.character.stamina < 10:
            self.stamina_label.setStyleSheet('color: orange;')
        else:
            self.stamina_label.setStyleSheet('color: green;')

        self.stamina_label.setText(f'Stamina: {self.character.stamina}')


    def tile_change_style(self, new_coord):
        ''' changes tile colour 2 show user where they are '''
        # reset stylesheet
        self.board_widget.setStyleSheet('border: 1px solid #9CC8EB; font: 10px; background-color: white;')

        # change tile style
        tile = self.board_grid_layout.itemAtPosition(
        rows.index(int(new_coord[0])),
        columns.index(new_coord[4]))
        tile.widget().setStyleSheet('''
        background-color: #F2A18F;
        border: 1px solid #D94A4A;
        font: 10px;''')


    def update_inventoryselect(self, inventory):
        ''' updates inventory '''
        self.inventory_select.clear()
        self.inventory_select.addItems(inventory)


    # move button click
    def move_button_clicked(self, checked: bool):
        ''' user moves based on combobox direction '''
        direction = self.move_combobox.currentText()

        # check selected direction isn't '-'
        if direction != '-':
            # move function
            def move(direction, coord):
                ''' move character based on direction, given location 
                    depletes stamina by 0.5/move
                '''
                # items from directions dictionary via key
                dir_items = directions[direction]
                row = int(coord[0])
                column = coord[4]

                if dir_items[0] == rows:
                    # check is not @ row boundary
                    if row != dir_items[0][dir_items[1]]:
                        new_coord = (f'{dir_items[0][dir_items[0].index(row) + dir_items[2]]}' +
                        f' : {column}')
                    else:
                        new_coord = coord
                else:
                    # check is not @ col boundary
                    if column != dir_items[0][dir_items[1]]:
                        new_coord = (f'{row} : ' +
                        f'{dir_items[0][dir_items[0].index(column) + dir_items[2]]}')
                    else:
                        new_coord = coord

                # check if changed, change console
                if coord == new_coord:
                    QMessageBox(QMessageBox.Icon.Critical, 'Error: Board Boundary',
                    f'Cannot {direction.lower()} - [ {coord} ] is already at edge of board.'
                    ).exec()
                else:
                    # update stamina, labels, tell user
                    self.moves += 1
                    self.character.stamina -= 0.5
                    self.update_stamina()

                    console_msg = (f'You {direction.lower()} from' +
                    f' [ {coord} ] to [ {new_coord} ].')

                    # update position on board
                    previous_tile = self.board_grid_layout.itemAtPosition(
                        rows.index(int(coord[0])),
                        columns.index(coord[4])).widget()
                    previous_tile.setStyleSheet('''
                    border: 1px solid #9CC8EB;
                    font: 10px;''')
                    self.tile_change_style(new_coord)

                    # check item
                    item = self.board_items[new_coord]

                    if item in questions.keys():
                        global question

                        question = item
                        console_msg += (f'\n\nQuestion found!' +
                        ' Please answer the question to the right.')
                        self.question.setHidden(False)

                        # set question text
                        self.question_label.setText(questions[item].question)

                        self.answer.clear()
                        self.answer.addItem('-')
                        self.load_photo(questions[item].name, self.image_label)
                        self.answer.addItems(x for x in (questions[item].options))

                    else:
                        # no question on tile, hide photo/question widget
                        self.question.setHidden(True)
                        self.load_photo('N/A', self.image_label)

                        if item in snacks.keys():
                            self.question_label.setText('')
                            character.inventory.append(snacks[item])
                            self.update_inventoryselect(character.inventory)

                            console_msg += (f'\n\nSnack - {item}' +
                            ' found! Added to inventory.')
                            self.board_items[new_coord] = ''

                    self.update_console(console_msg)

                return new_coord


            # set new location
            new_coord = move(direction, self.location)
            self.location = new_coord

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
                self.character.inventory.remove(item)
                self.update_inventoryselect(character.inventory)

                self.character.eat(item)
                self.update_stamina()
                self.update_console(f'{item.msg}')
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
                question
                ].options[answer_index - 1]

            if user_answer == questions[
                question
                ].answer:
                QMessageBox(
                    QMessageBox.Icon.Information, 'Answer correct!',
                    f'\'{user_answer}\' is the correct answer.\n').exec()

                # remove question from board items, add movie to inventory
                # + check whether all movies are in inventory
                self.board_items[self.location] = ''
                self.question.setHidden(True)
                self.load_photo('N/A', self.image_label)

                if questions[question].name != 'N/A':
                    self.character.inventory.append(questions[question])
                    self.update_inventoryselect(character.inventory)

                    def win_check(inventory: list):
                        check = []

                        for x in inventory:
                            if x.name in movies:
                                check.append(x.name)

                        if len(check) == len(movies):
                            QMessageBox(QMessageBox.Icon.Information, 'Game won!',
                            f'''Congrats! You\'ve found all the movies you need!!
                            Game completed in {self.moves} moves.\n
Click OK to close window.''').exec()
                            self.app.exit()
                        else:
                            QMessageBox(QMessageBox.Icon.Information, 'Movie added to inventory',
                            f'''{questions[question].name} added to inventory.\n
                            {len(movies) - len(check)} movies left to collect.''')

                    win_check(self.character.inventory)

            else:
                # update stamina
                self.character.stamina -= 1
                self.update_stamina()

                QMessageBox(
                    QMessageBox.Icon.Information, 'Answer incorrect.',
                    f'\'Try again - {user_answer}\' is the wrong answer. \n STAMINA -1.').exec()

