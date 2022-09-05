from PySide6.QtWidgets import *
from Controller import GameController
from Model import Character, Snack, character, snacks, questions, rows, columns

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

for row in range(0, len(rows)):
    for column in range(0, len(columns)):
        board_grid_layout.addWidget(QLabel(f'{str(rows[row])} : {columns[column]}'), row, column)

board_main_vbox.addWidget(QLabel('BOARD'))
board_main_vbox.addWidget(board_widget)

top_hbox.addWidget(board_main_widget)

# add inventory to TOP RIGHT
character_inventory = QWidget()
character_inventory_vbox = QVBoxLayout()
inventory_select = QListWidget()
inventory_select.addItems(x for x in character.inventory)
character_inventory_vbox.addWidget(QLabel('INVENTORY'))
character_inventory_vbox.addWidget(inventory_select)
use_item = QPushButton('Use Item')
character_inventory_vbox.addWidget(use_item)
stamina_label = QLabel(f'Stamina: {character.stamina}')
character_inventory_vbox.addWidget(stamina_label)
character_inventory.setLayout(character_inventory_vbox)

top_hbox.addWidget(character_inventory)

# add console msg to BOTTOM LEFT
bottom_widget = QWidget()
bottom_hbox = QHBoxLayout()
console = QLabel('ITEM/CONSOLE')

bottom_hbox.addWidget(console)

# add question to BOTTOM RIGHT
question = QWidget()
question_vbox = QVBoxLayout()
question_label = QLabel(questions['You Don\'t Mess With the Zohan'].question)
answer = QComboBox()
answer.addItem('-')
answer.addItems(x for x in questions['You Don\'t Mess With the Zohan'].options)
submit_answer = QPushButton('SUBMIT ANSWER')
question_vbox.addWidget(question_label)
question_vbox.addWidget(answer)
question_vbox.addWidget(submit_answer)
question.setLayout(question_vbox)

bottom_hbox.addWidget(question)

# set top/bottom widget layouts
top_widget.setLayout(top_hbox)
top_widget.setMaximumHeight(350)
bottom_widget.setLayout(bottom_hbox)

main_vbox.addWidget(top_widget)
main_vbox.addWidget(bottom_widget)

# connect controller
controller = GameController(
    console, question_label, answer, submit_answer,
    board_grid_layout, stamina_label, inventory_select,
    use_item #move_button
)

controller.submit_answer.clicked.connect(
    controller.submit_answer_clicked
)

# execute app
main_window.show()
app.exec()

