from PyQt6.QtWidgets import QApplication,QWidget,QSpinBox,QHBoxLayout,QLabel,QLineEdit
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 SpinBox")
        self.setGeometry(500,200,500,400)
        self.create_spin()

    def create_spin(self):
        hbox = QHBoxLayout()
        label= QLabel("Laptop Price:")
        self.lineedit = QLineEdit()
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)
        self.result = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.result)

        self.setLayout(hbox)
    def spin_selected(self):
        if int( self.lineedit.text() )!=0:
            price = int(self.lineedit.text())
            toutalPrice = self.spinbox.value() *price
            self.result.setText(str(toutalPrice))


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())