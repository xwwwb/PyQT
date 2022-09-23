from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,QVBoxLayout,QHBoxLayout

import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("智商检测")
        self.setGeometry(200,200,400,100)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.title = QLabel("输入姓名进行检测",self)
        self.result = QLabel(self)

        self.button = QPushButton("检测")
        self.button.clicked.connect(self.on_clicked)
        self.textLine = QLineEdit(self)

        hbox.addWidget(self.textLine)
        hbox.addWidget(self.button)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.title)
        hbox2.addWidget(self.result)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def on_clicked(self):
        name = self.textLine.text()
        if(name == "徐文博"):
            self.result.setText("智商正常")
            self.result.setStyleSheet('color:green')
        else:
            self.result.setText("傻逼")
            self.result.setStyleSheet('color:red')
app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())