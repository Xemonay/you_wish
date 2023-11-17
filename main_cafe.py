import io
import sys
from sqlite3 import connect

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from choose import CafeManage

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
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>310</x>
      <y>210</y>
      <width>141</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>210</y>
      <width>271</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Choose Your Coffe TODAY!</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>260</y>
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
   <widget class="QLabel" name="fry_str">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>260</y>
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
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>310</y>
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
      <x>20</x>
      <y>360</y>
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
   <widget class="QLabel" name="ground">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>310</y>
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
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="description">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>360</y>
      <width>691</width>
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
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_9">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>410</y>
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
      <x>20</x>
      <y>460</y>
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
   <widget class="QLabel" name="price">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>410</y>
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
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="volume">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>460</y>
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
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>500</x>
      <y>210</y>
      <width>21</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>16</pointsize>
     </font>
    </property>
    <property name="text">
     <string>ID</string>
    </property>
   </widget>
   <widget class="QPushButton" name="edit_t">
    <property name="geometry">
     <rect>
      <x>580</x>
      <y>460</y>
      <width>171</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Microsoft YaHei UI Light</family>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Edit</string>
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


class Cafe(QMainWindow):
    def __init__(self):
        super().__init__()
        con = connect('data//coffee.sqlite')
        c = con.cursor()
        uic.loadUi(io.StringIO(template), self)
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
