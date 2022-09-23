from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QListWidget,QLabel
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 ListWidget")
        self.setGeometry(500,200,500,400)
        vbox = QVBoxLayout()

        self.listWidget = QListWidget()
        self.listWidget.insertItem(0,"PyQT")
        self.listWidget.insertItem(1,"wxPython")
        self.listWidget.insertItem(2,'Kivy')
        self.listWidget.insertItem(3,'Tkinter')
        self.listWidget.insertItem(4,'PySide2')

        self.listWidget.clicked.connect(self.item_selected)
        self.label = QLabel("Hello")

        vbox.addWidget(self.listWidget)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def item_selected(self):
        item = self.listWidget.currentItem()
        self.label.setText("You have selected:"+str(item.text()))

app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())