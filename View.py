from PySide6.QtWidgets import *
from Controller import GameController
from Model import Character, Snack, Question, character, snacks, questions, rows, columns, movies, directions, location, board_items
from PySide6.QtGui import QPixmap
import os

# set up app, main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle(' GAME ')
main_window.resize(1028, 768)

# set up main widget
main_widget = QWidget()
main_window.setCentralWidget(main_widget)

# split window vertically
main_vbox = QVBoxLayout()
main_widget.setLayout(main_vbox)

# add top/bottom widgets to split window
top_widget = QWidget()
top_hbox = QHBoxLayout()
bottom_hbox = QHBoxLayout()

# add board to TOP LEFT
board_main_widget = QWidget()
board_main_vbox = QVBoxLayout()
board_main_widget.setLayout(board_main_vbox)
board_grid_layout = QGridLayout()

board_widget = QWidget()
board_widget.setMinimumWidth(500)
board_widget.setMinimumHeight(300)
board_widget.setLayout(board_grid_layout)

# construct board, 2d list to change stylesheet
board_2d_list = [[] for x in range(0, len(rows))]

for row in range(0, len(rows)):
    for column in range(0, len(columns)):
        board_2d_list[row].append(f'{rows[row]} : {str(columns[column])}')
        new_widget = QLabel(f'{rows[row]} : {str(columns[column])}')
        board_grid_layout.addWidget(new_widget, row, column)


board_label = QLabel('BOARD')
board_main_vbox.addWidget(board_label)
board_main_vbox.addWidget(board_widget)

top_hbox.addWidget(board_main_widget)

# add inventory, movies list to TOP RIGHT
top_right_widget = QWidget()
top_right_layout = QHBoxLayout()
top_hbox.addWidget(top_right_widget)

movies_stamina = QWidget()
movies_stamina_layout = QVBoxLayout()

movies_widget = QListWidget()
movies_widget.addItems(x for x in movies)
movies_label = QLabel('MOVIES TO COLLECT')
movies_stamina_layout.addWidget(movies_label)

movies_stamina_layout.addWidget(movies_widget)

stamina_label = QLabel(f'Stamina: {character.stamina}')
movies_stamina_layout.addWidget(stamina_label)

character_inventory = QWidget()
character_inventory_vbox = QVBoxLayout()
inventory_select = QListWidget()

inventory_select.addItems(x.name for x in character.inventory)
inventory_label = QLabel('INVENTORY')
character_inventory_vbox.addWidget(inventory_label)
character_inventory_vbox.addWidget(inventory_select)
use_item = QPushButton('Use Item')
character_inventory_vbox.addWidget(use_item)

character_inventory.setLayout(character_inventory_vbox)

movies_stamina.setLayout(movies_stamina_layout)
top_right_layout.addWidget(movies_stamina)
top_right_layout.addWidget(character_inventory)
top_right_widget.setLayout(top_right_layout)

# create bottom widget
bottom_widget = QWidget()
bottom_hbox = QHBoxLayout()

# create bottom left widget
bottom_left_widget = QWidget()
bottom_left_layout = QVBoxLayout()

move_widget = QWidget()
move_layout = QHBoxLayout()
move_widget.setLayout(move_layout)

move_combobox = QComboBox()
move_combobox.addItem('-')
move_combobox.addItems(x for x in directions)
move_button = QPushButton('Move')
move_button.setMaximumWidth(75)
move_widget.setMaximumWidth(225)
move_layout.addWidget(move_combobox)
move_layout.addWidget(move_button)

console = QLabel(
    f'''Hey! Welcome to SANDLERSEARCH! This is an educational game about Adam Sandler. 

SANDLERSEARCH takes place in your musty living room on a boring, lonely night. 
Desperate for company, you decide to embark on a Sandlerthon.

You must find all 10 Sandler films in order to begin your movie marathon!!!

YOU ARE LOCATED AT:   [ {location} ]''')


bottom_left_layout.addWidget(move_widget)
bottom_left_layout.addWidget(console)

bottom_left_widget.setLayout(bottom_left_layout)
bottom_hbox.addWidget(bottom_left_widget)

# add question to BOTTOM RIGHT
bottom_right_widget = QWidget()
bottom_right_layout = QHBoxLayout()

question = QWidget()
question_vbox = QVBoxLayout()
question_label = QLabel()
answer = QComboBox()
answer.addItem('-')
submit_answer = QPushButton('SUBMIT ANSWER')
question_vbox.addWidget(question_label)
question_vbox.addWidget(answer)
question_vbox.addWidget(submit_answer)
question.setLayout(question_vbox)
question.setMinimumWidth(595)

bottom_right_layout.addWidget(question)
image_label = QLabel('')
image_label.setMaximumWidth(150)
bottom_right_layout.addWidget(image_label)
bottom_right_widget.setLayout(bottom_right_layout)

# add image
bottom_hbox.addWidget(bottom_right_widget)

# set top/bottom widget layouts
top_widget.setLayout(top_hbox)
top_widget.setMaximumHeight(350)
bottom_widget.setLayout(bottom_hbox)

main_vbox.addWidget(top_widget)
main_vbox.addWidget(bottom_widget)

# connect controller, set question widget hidden
question.setHidden(True)

controller = GameController(
    app, location, board_items, character, console, question, question_label, 
    image_label, answer, submit_answer, board_grid_layout, stamina_label,
    inventory_select, use_item, move_combobox, move_button
)

controller.submit_answer.clicked.connect(
    controller.submit_answer_clicked
)
controller.use_item.clicked.connect(
    controller.use_item_clicked
)
controller.move_button.clicked.connect(
    controller.move_button_clicked
)

# set styles
app.setStyleSheet('''
    QMainWindow {
        background-color: #F7F8FC;
    }

    QPushButton {
        background-color: #F58D40;
        font-weight: regular;
        border: 2px solid #F58D40;
    }

    QListWidget {
        border: .3px solid white;
    }
''')

board_widget.setStyleSheet('border: 1px solid #F58D40; font: 10px')
bottom_widget.setStyleSheet('''font:13px;
QComboBox {
    border: 2px solid #CCE8FF
    }''')
top_widget.setStyleSheet('''QLabel {
        color: #0F1316;
        font: bold 14px;
    }''')

current_tile = board_grid_layout.itemAtPosition(0, 0)


# execute app
main_window.show()
app.exec()


