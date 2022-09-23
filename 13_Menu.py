from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtGui import QIcon,QAction
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 Menu")
        self.setGeometry(500,200,500,400)
        self.create_menu()

    def create_menu(self):
        mainMenu = self.menuBar()
        # mainMenu.setNativeMenuBar(False) # 使用非原生的menuBar 解决Exit不显示的问题 但是效果太差了
        fileMenu = mainMenu.addMenu("File")

        newAction = QAction(QIcon("./resource/logo.png"),"New",self)
        newAction.setShortcut("Ctrl+N")
        fileMenu.addAction(newAction)

        fileMenu.addSeparator()

        saveAction = QAction(QIcon("./resource/logo.png"), "Save", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)


        # 此外,当在Mac上使用PyQt时,系统将拦截某些包含"退出","退出","设置","设置","首选项"以及可能还有一些其他命令的命令,并将其从菜单栏中删除因为它们是保留标签.如果菜单栏标题没有项目,它将不会显示,使其看起来好像您没有修改菜单栏.
        # 这里打出Exit之后就不显示了
        exitAction = QAction(QIcon("./resource/logo.png"),"Exi",self)
        exitAction.triggered.connect(self.close_window)
        fileMenu.addAction(exitAction)

    def close_window(self):
        self.close()


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())