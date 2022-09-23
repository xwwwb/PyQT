from PyQt6.QtWidgets import QApplication, QWidget,QPushButton,QLabel
from PyQt6.QtGui import QIcon,QFont
import sys
from PyQt6.QtGui import QIcon

class windowClass(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello")
        self.setWindowIcon(QIcon("resource/logo.png"))
        # 设置后无法拖动窗口缩放
        # self.setFixedHeight(500)
        # self.setFixedWidth(500)
        self.setGeometry(500,800,400,300)
        # self.setStyleSheet('background-color:red')
        # stylesheet = (
        #     'background-color:red'
        # )
        # self.setStyleSheet(stylesheet)
        self.create_widgets()

    def create_widgets(self):
        btn = QPushButton("Click Me",self)
        btn.move(100,100)
        btn.setGeometry(100,100,100,100)
        btn.setStyleSheet('background-color:Red')
        btn.setIcon(QIcon('resource/logo.png'))

        label = QLabel("My Label",self)
        label.move(100,200)
        label.setStyleSheet('color:green')
        label.setFont(QFont("Times New Roman",15))


app = QApplication([])

window = windowClass()

window.show()
sys.exit(app.exec())
