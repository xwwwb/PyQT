from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys

class Window(QWidget):
    move_Flag = False
    Window_Width = 1000
    Window_Length = 1000
    Window_Title = "Hello"
    def __init__(self):
        # 窗体
        super().__init__()
        self.setup_ui()
        self.show()

    def setup_ui(self):
        self.setWindowTitle(self.Window_Title)
        self.Title_Button()
        self.resize(self.Window_Width, self.Window_Length)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        # self.setWindowIcon(QIcon("43.png"))
        self.setWindowOpacity(0.9)


    # 标题按钮
    def Title_Button(self):
        # 关闭按钮
        self.close_button = MyPushButton(self)
        self.close_button.setText("关闭")
        self.close_button.clicked.connect(self.close)

        # 最大化按钮

        self.maximize_button = MyPushButton(self)
        self.maximize_button.setText("最大化")

        # 最大化按钮方法
        def maximize_method():
            if window.isMaximized():
                self.showNormal()
                self.maximize_button.setText("最大化")
            else:
                self.showMaximized()
                self.maximize_button.setText("恢复")

        self.maximize_button.clicked.connect(maximize_method)

        # 最小化按钮

        self.minimize_button = MyPushButton(self)
        self.minimize_button.setText("最小化")
        self.minimize_button.clicked.connect(self.showMinimized)

    def resizeEvent(self,evt):

        self.close_button_x = self.width() - MyPushButton.btn_width - MyPushButton.side_margin
        self.close_button.move(self.close_button_x, MyPushButton.top_margin)

        self.maximize_button_x = self.close_button_x - MyPushButton.btn_width - MyPushButton.side_margin
        self.maximize_button.move(self.maximize_button_x, MyPushButton.top_margin)

        self.minimize_button_x = self.maximize_button_x - MyPushButton.btn_width - MyPushButton.side_margin
        self.minimize_button.move(self.minimize_button_x, MyPushButton.top_margin)

# 窗口移动
    def mousePressEvent(self,evt):
        # if evt.x() <= self.minimize_button_x and evt.y() <= (MyPushButton.bottom_margin + MyPushButton.btn_height):
        if evt.x() <= self.minimize_button_x and evt.y() <= 60:

            if evt.button() == Qt.LeftButton:
                self.move_Flag = True
                self.window_origin_x = self.x()
                self.window_origin_y = self.y()
                self.mouse_origin_x = evt.globalX()
                self.mouse_origin_y = evt.globalY()
    def mouseMoveEvent(self, evt):
        if self.move_Flag:
            self.mouse_des_x = evt.globalX()
            self.mouse_des_y = evt.globalY()
            self.window_des_x = self.window_origin_x + self.mouse_des_x - self.mouse_origin_x
            self.window_des_y = self.window_origin_y + self.mouse_des_y - self.mouse_origin_y

            # 按照向量移动窗口
            self.move(self.window_des_x,self.window_des_y)

    def mouseReleaseEvent(self,evt):
        self.move_Flag = False


class MyPushButton(QPushButton):
    btn_width = 160
    btn_height = 50
    top_margin = 20
    side_margin = 10
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.resize(self.btn_width,self.btn_height)
        self.show()





if __name__ == '__main__':

    # 创建一个应用程序对象
    app = QApplication(sys.argv)

    window = Window()

    sys.exit(app.exec())