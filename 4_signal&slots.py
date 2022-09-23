from PyQt6.QtWidgets import QApplication, QWidget,QPushButton,QLabel
from PyQt6.QtGui import QIcon,QFont
import sys
from PyQt6.QtGui import QIcon


# 也可以使用ui文件生成py文件后修改py文件添加
class windowClass(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQT6 Signal And Slots")
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
        btn.clicked.connect(self.clicked_btn)

        self.label = QLabel("My Label",self)
        # self.label.move(100,200)
        self.label.setGeometry(100,200,200,100)
        self.label.setStyleSheet('color:green')
        self.label.setFont(QFont("Times New Roman",15))

    def clicked_btn(self):
        self.label.setText("Text is changed")
        self.label.setStyleSheet('color:red')




app = QApplication([])

window = windowClass()

window.show()
sys.exit(app.exec())
