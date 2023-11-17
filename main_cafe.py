import sys
from sqlite3 import connect

from UI.maindesign import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from choose import CafeManage



class Cafe(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        con = connect('data//coffee.sqlite')
        c = con.cursor()
        self.edit_t.clicked.connect(self.open_check16)
        self.comboBox.addItem('Please Choose a Coffee16')
        self.comboBox.currentIndexChanged.connect(self.yeah)
        a = c.execute('''SELECT * FROM cafe''').fetchall()
        self.alpha = {x[1]: {y: j for y, j in zip(('fry_str', 'ground', 'descrip', 'price', 'volume'), x[2:])}
                      for x in a}
        for x in c.execute('''SELECT name FROM cafe''').fetchall():
            self.comboBox.addItem(x[0])

    def yeah(self):
        a = self.comboBox.currentText()
        if a != 'Please Choose a Coffee16' and a:
            self.fry_str.setText(self.alpha.get(a).get('fry_str'))
            self.ground.setText(self.alpha.get(a).get('ground'))
            self.description.setText(self.alpha.get(a).get('descrip'))
            self.price.setText(str(self.alpha.get(a).get('price')))
            self.volume.setText(self.alpha.get(a).get('volume'))
        else:
            self.fry_str.setText('')
            self.ground.setText('')
            self.description.setText('')
            self.price.setText('')
            self.volume.setText('')

    def update(self):
        self.comboBox.clear()
        con = connect('data//coffee.sqlite')
        c = con.cursor()
        self.comboBox.addItem('Please Choose a Coffee16')
        a = c.execute('''SELECT * FROM cafe''').fetchall()
        self.alpha = {x[1]: {y: j for y, j in zip(('fry_str', 'ground', 'descrip', 'price', 'volume'), x[2:])}
                      for x in a}
        for x in c.execute('''SELECT name FROM cafe''').fetchall():
            self.comboBox.addItem(x[0])
        self.comboBox.currentIndexChanged.connect(self.yeah)

    def open_check16(self):
        self.check16 = CafeManage(self)
        self.check16.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cafe()
    ex.show()
    sys.exit(app.exec())
