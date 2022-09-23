from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter,QPen,QBrush
from PyQt6.QtCore import Qt
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 DrawEllipse")
        self.setGeometry(500, 200, 500, 400)

    def paintEvent(self,e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.yellow,5,Qt.PenStyle.DashDotLine))
        painter.setBrush(QBrush(Qt.GlobalColor.green,Qt.BrushStyle.Dense5Pattern))
        # 椭圆
        painter.drawEllipse(100,100,400,200)




app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
