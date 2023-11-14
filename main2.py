import sys
from random import choice as ch
from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow


class GoYellow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.yeah)
        self.should_paint_circle = False

    def paintEvent(self, event):
        if self.should_paint_circle:
            painter = QPainter(self)
            painter.setPen(QPen(ch((Qt.red, Qt.yellow, Qt.green, Qt.blue, Qt.black, Qt.lightGray)), 8))
            a = ch(range(1, 100))
            painter.drawEllipse(ch(range(0, 756)), ch(range(0, 565)), a, a)
        self.should_paint_circle = False

    def yeah(self):
        self.should_paint_circle = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoYellow()
    ex.show()
    sys.exit(app.exec())
