from PySide6.QtWidgets import *

# set up app, main window
app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle(' GAME ')
main_window.resize(1028, 768)

# set up main widget
main_widget = QWidget()
main_window.setCentralWidget(main_widget)

main_layout = QVBoxLayout()

button = QPushButton('PUSH')
bottom_widget = QWidget()
main_layout.addWidget(button)
main_layout.addWidget(bottom_widget)

boob_layout = QHBoxLayout()
boob_layout.addWidget(QLabel('01'))

poo_layout = QHBoxLayout()
poo_layout.addWidget(QLabel('10'))
main_widget.setLayout(main_layout)

def button_clicked_connect(checked: bool):
    bottom_widget.setLayout(boob_layout)

button.clicked.connect(button_clicked_connect)

# execute app
main_window.show()
app.exec()