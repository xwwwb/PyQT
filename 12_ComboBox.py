from PyQt6.QtWidgets import QApplication,QWidget,QComboBox,QVBoxLayout,QLabel
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Combobox")
        self.setGeometry(500,200,500,400)

        vbox = QVBoxLayout()

        self.combo = QComboBox()

        self.combo.addItem("PyQT6")
        self.combo.addItem("wxPython")
        self.combo.addItem("Kivy")
        self.combo.addItem("TKinter")
        self.combo.addItem("PySide2")
        self.combo.currentIndexChanged.connect(self.item_change)
        self.label = QLabel("Hello")

        vbox.addWidget(self.combo)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def item_change(self):
        # current =  self.combo.currentIndex()
        # self.label.setText(self.combo.itemText(current))\
        value = self.combo.currentText()
        self.label.setText("You have selected:"+value)


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())