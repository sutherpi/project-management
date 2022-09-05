from PySide6.QtWidgets import *
from Controller import GameController
from board_test import board, board_items

# set up app, main window
app = QApplication()
main_window = QMainWindow()

main_widget = QWidget()
main_window.setCentralWidget(main_widget)
hbox = QHBoxLayout()
main_widget.setLayout(hbox)

board_grid = QWidget()
grid = QGridLayout()
board_grid.setLayout(grid)

rows = [x for x in range(0, 10)]
columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

for row in range(0, len(rows)):
    for column in range(0, len(columns)):
        grid.addWidget(QLabel(f'{str(rows[row])}:{columns[column]}'), row, column)

hbox.addWidget(board_grid)

# execute app
main_window.show()
app.exec()