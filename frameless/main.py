from PyQt6.QtWidgets import QWidget,QApplication
from PyQt6.QtCore import Qt
from PyQt6 import uic

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("MainWindow.ui", self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)

if __name__ == "__main__":

    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()