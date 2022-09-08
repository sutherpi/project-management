from PySide6.QtWidgets import *
from Controller import GameController
from Model import Character, Snack, character, snacks, questions, rows, columns, movies

# set up app, main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle(' GAME ')
main_window.resize(1028, 768)

main_widget = QWidget()
main_window.setCentralWidget(main_widget)

# split window vertically
main_vbox = QVBoxLayout()
main_widget.setLayout(main_vbox)

# add top/bottom widgets to split window
top_widget = QWidget()
top_hbox = QHBoxLayout()
top_widget.setLayout(top_hbox)
bottom_widget = QWidget()
bottom_hbox = QHBoxLayout()
bottom_widget.setLayout(bottom_hbox)

main_vbox.addWidget(top_widget)
main_vbox.addWidget(bottom_widget)

# add board to TOP LEFT
board_main_widget = QWidget()
board_main_vbox = QVBoxLayout()
board_main_widget.setLayout(board_main_vbox)
board_grid_layout = QGridLayout()

board_widget = QWidget()
board_widget.setMinimumWidth(500)
board_widget.setMinimumHeight(300)
board_widget.setLayout(board_grid_layout)
board_main_vbox.addWidget(board_widget)

for row in range(0, len(rows)):
    for column in range(0, len(columns)):
        board_grid_layout.addWidget(QLabel(f'{rows[row]} : {str(columns[column])}'), row, column)

top_hbox.addWidget(board_main_widget)

# add movies, inventory to top right
top_right_widget = QWidget()
top_right_layout = QHBoxLayout()
top_right_widget.setLayout(top_right_layout)

top_right_A = QWidget()
top_right_layout.addWidget(top_right_A)

top_right_A_layout = QVBoxLayout()

movies_widget = QListWidget()
movies_widget.addItems(x for x in movies)

top_right_A_layout.addWidget(movies_widget)
top_right_A.setLayout(top_right_A_layout)

top_hbox.addWidget(top_right_A)




# connect controller, run app
main_window.show()
app.exec()

