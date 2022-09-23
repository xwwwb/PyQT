from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QTableWidget,QTableWidgetItem
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 TableWidget")
        self.setGeometry(500,200,500,400)
        vbox = QVBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(3)
        tableWidget.setColumnCount(3)


        tableWidget.setHorizontalHeaderItem(0,QTableWidgetItem("FNAME"))
        tableWidget.setHorizontalHeaderItem(1,QTableWidgetItem("LNAME"))
        tableWidget.setHorizontalHeaderItem(2,QTableWidgetItem("Email"))

        tableWidget.setItem(0,0,QTableWidgetItem("Xwb"))

        vbox.addWidget(tableWidget)
        self.setLayout(vbox)


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())