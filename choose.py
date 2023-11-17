import io
import sys
from sqlite3 import connect

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>350</y>
      <width>61</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>GROUND</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>400</y>
      <width>71</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Description'</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>300</y>
      <width>61</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Fry Str</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>450</y>
      <width>61</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Price</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_10">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>500</y>
      <width>61</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Volume</string>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>50</y>
      <width>271</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Create Your Coffe TODAY!</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="fry_str">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>310</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="placeholderText">
     <string>text</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="ground">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>360</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="placeholderText">
     <string>text</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="description">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>410</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="placeholderText">
     <string>text</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="price">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>460</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="placeholderText">
     <string>x</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="volume">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>510</y>
      <width>113</width>
      <height>20</height>
     </rect>
    </property>
    <property name="placeholderText">
     <string>text</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>110</y>
      <width>291</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Or update your Coffe TODAY!</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>340</x>
      <y>110</y>
      <width>141</width>
      <height>22</height>
     </rect>
    </property>
    <item>
     <property name="text">
      <string>Choose</string>
     </property>
    </item>
   </widget>
   <widget class="QPushButton" name="add_t">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>460</y>
      <width>75</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>ADD</string>
    </property>
   </widget>
   <widget class="QPushButton" name="update_t">
    <property name="geometry">
     <rect>
      <x>560</x>
      <y>460</y>
      <width>75</width>
      <height>71</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="text">
     <string>UPDATE</string>
    </property>
   </widget>
   <widget class="QLabel" name="mistake">
    <property name="geometry">
     <rect>
      <x>390</x>
      <y>340</y>
      <width>271</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLineEdit" name="name">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>260</y>
      <width>161</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
    <property name="placeholderText">
     <string>text</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>250</y>
      <width>61</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Name</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class CafeManage(QMainWindow):
    def __init__(self, main):
        super().__init__()
        self.main = main
        con = connect('data//coffee.sqlite')
        c = con.cursor()
        uic.loadUi(io.StringIO(template), self)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CafeManage()
    ex.show()
    sys.exit(app.exec())
