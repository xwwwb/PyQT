import sys

from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPainter, QTextDocument
from PyQt6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 DrawEllipse")
        self.setGeometry(500, 200, 500, 400)

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.drawText(100, 100, "PyQt6")
        rect = QRectF(100, 150, 250, 25)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "Study PyQt6")

        document = QTextDocument()
        rect2 = QRectF(0, 0, 250, 250)
        document.setTextWidth(rect2.width())
        document.setHtml("<b>Hello World</b>")
        document.drawContents(painter, rect2)


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())
