from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout\
    ,QPushButton,QHBoxLayout,QGridLayout

from PyQt6.QtGui import QIcon

import sys

class VBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Layouts")
        self.setGeometry(500,200,500,400)

        vbox = QVBoxLayout()
        btn1 = QPushButton("Button One")
        btn2 = QPushButton("Button Two")

        btn3 = QPushButton("Button Three")
        btn4 = QPushButton("Button Four")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        self.setLayout(vbox)

class Hbox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Layouts")
        self.setGeometry(500,200,500,400)

        vbox = QHBoxLayout()
        btn1 = QPushButton("Button One")
        btn2 = QPushButton("Button Two")

        btn3 = QPushButton("Button Three")
        btn4 = QPushButton("Button Four")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        self.setLayout(vbox)

class Grid(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setGeometry(500, 200, 500, 400)
        btn1 = QPushButton("Button One")
        btn2 = QPushButton("Button Two")
        btn3 = QPushButton("Button Three")
        btn4 = QPushButton("Button Four")
        btn5 = QPushButton("Button Five")
        btn6 = QPushButton("Button Six")
        btn7 = QPushButton("Button Seven")
        btn8 = QPushButton("Button Eight")

        grid.addWidget(btn1,0,0)
        grid.addWidget(btn2,0,1)
        grid.addWidget(btn3,0,2)
        grid.addWidget(btn4,1,0)
        grid.addWidget(btn5,1,1)
        grid.addWidget(btn6,1,2)
        grid.addWidget(btn7,2,0)
        grid.addWidget(btn8,2,1)

        self.setLayout(grid)

app = QApplication(sys.argv)

window = VBox()
window2 = Hbox()
window3 = Grid()


window.show()
window2.show()
window3.show()

sys.exit(app.exec())