from sqlite3 import connect
from UI.addEditCoffeeFormDesign import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class CafeManage(QMainWindow, Ui_MainWindow):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)
        self.main = main
        con = connect('data//coffee.sqlite')
        c = con.cursor()
        a = c.execute('''SELECT * FROM cafe''').fetchall()
        self.alpha = {x[1]: {y: j for y, j in zip(('fry_str', 'ground', 'discrip', 'price', 'volume'), x[2:])}
                      for x in a}
        for x in c.execute('''SELECT name FROM cafe''').fetchall():
            self.comboBox.addItem(x[0])
        self.add_t.clicked.connect(self.add)
        self.update_t.clicked.connect(self.update016)

    def add(self):
        if (
                self.name.text() != '' and self.fry_str.text() != '' and self.ground.text() != '' and
                self.description.text != '' and self.price.text().isdigit() and self.volume.text() != ''):
            con = connect('data//coffee.sqlite')
            c1 = con.cursor()
            c1.execute('''INSERT INTO cafe(name, fry_str, ground, 
                descrip, price, volume) VALUES (?, ?, ?, ?, ?, ?)''',
                       (
                           self.name.text(), self.fry_str.text(), self.ground.text(), self.description.text(),
                           int(self.price.text()), self.volume.text()))
            con.commit()
            con.close()
            self.mistake.setText('SUCCESS')
            self.main.update()
            self.update()
        else:
            self.mistake.setText('Something is not cor')

    def update016(self):
        if self.price.text() == '' or self.price.text().isdigit():
            con = connect('data//coffee.sqlite')
            c1 = con.cursor()

            if self.name.text() != '':
                c1.execute('''UPDATE cafe
                                    SET name = ?
                                    WHERE name = ?''',
                           (self.name.text(), self.comboBox.currentText()))
            if self.fry_str.text() != '':
                c1.execute('''UPDATE cafe
                                               SET name = ?
                                               WHERE name = ?''',
                           (self.fry_str.text(), self.comboBox.currentText()))
            if self.ground.text() != '':
                c1.execute('''UPDATE cafe
                                               SET name = ?
                                               WHERE name = ?''',
                           (self.ground.text(), self.comboBox.currentText()))
            if self.description.text() != '':
                c1.execute('''UPDATE cafe
                                               SET name = ?
                                               WHERE name = ?''',
                           (self.description.text(), self.comboBox.currentText()))
            if self.price.text() != '':
                c1.execute('''UPDATE cafe
                                               SET name = ?
                                               WHERE name = ?''', (self.price.text(), self.comboBox.currentText()))
            if self.volume.text() != '':
                c1.execute('''UPDATE cafe
                                               SET name = ?
                                               WHERE name = ?''', (self.volume.text(), self.comboBox.currentText()))
            con.commit()
            con.close()
            self.mistake.setText('SUCCESS')
            self.main.update()
            self.update()
        else:
            self.mistake.setText('Something is not cor')

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
