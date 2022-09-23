from PyQt6.QtWidgets import QApplication,QWidget

from PyQt6 import uic
import sys

# 可以使用pyuic将ui文件转成py文件
class UI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./resource/2_window.ui",self)

app= QApplication(sys.argv)
window = UI()

window.show()

sys.exit(app.exec())