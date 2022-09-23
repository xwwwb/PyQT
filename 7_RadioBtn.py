from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QRadioButton,QGroupBox,QLabel,QHBoxLayout

import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Radio Button")
        self.setGeometry(50,50,500,500)

        self.radio_btn()

        vbox = QVBoxLayout()
        vbox.addWidget(self.grpbox)
        self.label = QLabel("Hello")
        self.label.setFont(QFont("Sanserif",13))
        vbox.addWidget(self.label)

        self.setLayout(vbox)


    def radio_btn(self):
        self.grpbox = QGroupBox("Choose Programming Language")
        self.grpbox.setFont(QFont("Sanserif",13))
        hbox = QHBoxLayout()
        self.rad1 = QRadioButton("Python")
        self.rad2 = QRadioButton("Java")
        self.rad1.toggled.connect(self.on_selected)
        self.rad2.toggled.connect(self.on_selected)

        hbox.addWidget(self.rad1)
        hbox.addWidget(self.rad2)
        self.grpbox.setLayout(hbox)

    def on_selected(self):
        radio = self.sender()

        # if radio.isChecked():
        #     self.label.setText("You have selected "+radio.text())

        if self.rad2.isChecked():
            self.label.setText("You have selected Java")
        if self.rad1.isChecked():
            self.label.setText("You have selected Python")


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())