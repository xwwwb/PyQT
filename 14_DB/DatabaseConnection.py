from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(559, 159)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dbCreate = QtWidgets.QPushButton(Form)
        self.dbCreate.setObjectName("dbCreate")
        self.dbCreate.clicked.connect(self.create_database)
        self.horizontalLayout_2.addWidget(self.dbCreate)
        self.dbConnection = QtWidgets.QPushButton(Form)
        self.dbConnection.setObjectName("dbConnection")
        self.dbConnection.clicked.connect(self.db_connect)
        self.horizontalLayout_2.addWidget(self.dbConnection)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "DataBase Name"))
        self.dbCreate.setText(_translate("Form", "Database Creation"))
        self.dbConnection.setText(_translate("Form", "Database Connection"))

    def create_database(self):
        try:
            db = mc.connect(
                host="localhost",
                user="root",
                password="a20011226"
            )
            cursor = db.cursor()
            dbname = self.lineEdit.text()
            cursor.execute(f"CREATE DATABASE {dbname}")
            self.label_2.setText(f"Database {dbname} created")
            db.close()
        except mc.Error as e:
            print(e)
            self.label_2.setText("Databse Creation Failed ")
    def db_connect(self):
        try:
            db = mc.connect(
                host="localhost",
                user="root",
                password="a20011226",
                database=self.lineEdit.text()
            )
            self.label_2.setText("There is a connection")
        except mc.Error as e:
            print(e)
            self.label_2.setText("Database Connection Failed")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
