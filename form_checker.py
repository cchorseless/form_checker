import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton


class MainUi(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pushbutton = QPushButton('red',self)
        pushbutton.setGeometry(10, 10, 50, 100)
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    UI = MainUi()
    sys.exit(app.exec_())
