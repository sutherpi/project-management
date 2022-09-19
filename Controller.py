from dataclasses import dataclass
from PySide6.QtWidgets import *
from Model import Character, Snack, Question, character, snacks, questions, rows, columns, movies, directions, board_items, location

@dataclass
class GameController():
    ''' a controller for events + connections
    within GUI/View.py
    '''
    app: QApplication
    location: str
    board_items: dict
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

        self.stamina_label.setText(f'Stamina: {self.character.stamina}')


    # move button click
    def move_button_clicked(self, checked: bool):
        ''' user moves based on combobox direction '''
        move_combobox_index = self.move_combobox.currentIndex()

        # check selected direction isn't '-'
        if move_combobox_index != 0:
            direction = directions[move_combobox_index - 1]
            
            # move function
            def move(direction, coord):
                ''' move character based on direction, given location 
                    depletes stamina by 0.5/move
                '''
                row = int(coord[0])
                column = coord[4]

                # check isnt at boundary
                if direction == 'MOVE UP':
                    if row != rows[0]:
                        new_coord = f'{rows[rows.index(row) - 1]} : {column}'
                    else:
                        new_coord = coord

                elif direction == 'MOVE RIGHT':
                    if column != columns[-1]:
                        new_coord = f'{row} : {columns[columns.index(column) + 1]}'
                    else:
                        new_coord = coord

                elif direction == 'MOVE DOWN':
                    if row != rows[-1]:
                        new_coord = f'{rows[rows.index(row) + 1]} : {column}'
                    else:
                        new_coord = coord
                
                elif direction == 'MOVE LEFT':
                    if column != columns[0]:
                        new_coord = f'{row} : {columns[columns.index(column) - 1]}'
                    else:
                        new_coord = coord

                # check if changed, change console
                if coord == new_coord:
                    QMessageBox(QMessageBox.Icon.Critical, 'Error: Board Boundary',
                    f'Cannot {direction.lower()} - [ {coord} ] is already at edge of board.'
                    ).exec()
                else:
                    # update stamina, labels, tell user
                    self.character.stamina -= 0.5
                    self.update_stamina()

                    console_msg = (f'You {direction.lower()} from' +
                    f' [ {coord} ] to [ {new_coord} ].')

                    # check item
                    item = self.board_items[new_coord]

                    if item in questions.keys():
                        console_msg += (f'\n\nQuestion found!' +
                        ' Please answer the question to the right.')

                        # set question text
                        self.question_label.setText(questions[item].question)
                        self.answer.clear()
                        self.answer.addItem('-')
                        self.answer.addItems(x for x in (questions[item].options))

                    elif item in snacks.keys():
                        character.inventory.append(snacks[item])
                        self.inventory_select.clear()
                        self.inventory_select.addItems(
                            x.name for x in character.inventory)

                        console_msg += (f'\n\nSnack - {item}' +
                        ' found! Added to inventory.')
                        self.board_items[new_coord] = ''
                    else:
                        pass
                        # set widget as empty

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
                self.character.inventory.remove(item)
                self.inventory_select.clear()
                self.inventory_select.addItems(
                    x.name for x in character.inventory)

                self.character.eat(item)
                self.update_stamina()
                self.update_console(f'{item.msg}')
                QMessageBox(QMessageBox.Icon.Information, 'Item used',
                f'{item.name} used. + {item.regen} stamina!').exec()

    # submit answer click
    def submit_answer_clicked(self, checked: bool):
        ''' submits answer in qcheckbox row '''
        answer_index = self.answer.currentIndex()
        question_index = self.question_label

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

                # remove question from board items, add movie to inventory
                # + check whether all movies are in inventory
                self.board_items[self.location] = ''
                self.character.inventory.append(questions['You Don\'t Mess With the Zohan'])

                self.inventory_select.clear()
                self.inventory_select.addItems(
                    x.name for x in self.character.inventory)

                def win_check(self, inventory):
                    check = []
                    
                    for x in character.inventory:
                        if x.name in movies:
                            check.append(x.name)
                        if check == movies:
                            QMessageBox(QMessageBox.Icon.Information, 'Game won!',
                            'Congrats! You\'ve found all the movies you need!!!!!')
                
                win_check(character.inventory)

            else:
                # update stamina
                self.character.stamina -= 1
                self.update_stamina()

                QMessageBox(
                    QMessageBox.Icon.Information, 'Answer incorrect.',
                    f'\'{user_answer}\' is the wrong answer. \n STAMINA -1.').exec()


