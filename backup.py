# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(958, 661)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.StrongFocus)
        MainWindow.setAutoFillBackground(False)
        # MainWindow.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/back.jpg)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setEnabled(True)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 261, 181))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.scrollArea.setFont(font)
        self.scrollArea.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -361, 242, 540))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 16, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 9, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 14, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 12, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 8, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 17, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 22, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 6, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 13, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 11, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 10, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem6, 7, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 20, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem8, 3, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 19, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 5, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 15, 0, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setItalic(False)
        font.setUnderline(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 21, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(True)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(50, 10, 151, 41))
        palette = QtGui.QPalette()
        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setEnabled(False)
        self.img.setGeometry(QtCore.QRect(10, 270, 261, 351))
        self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/no_photo.jpg);")
        self.img.setText("")
        self.img.setObjectName("img")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "???????????????????????????? ??????????????????????????"))
        self.pushButton_4.setText(_translate("MainWindow", "???????????????????? ??????????????????????????"))
        self.pushButton_5.setText(_translate("MainWindow", "????????????????????????????-????????"))
        self.pushButton.setText(_translate("MainWindow", "????????????????"))
        self.pushButton_3.setText(_translate("MainWindow", "???????????????????????? ??????????????????????????"))
        self.pushButton_8.setText(_translate("MainWindow", "???????????????????????? ??????????????????????????"))
        self.pushButton_6.setText(_translate("MainWindow", "????????????????-3??"))
        self.pushButton_7.setText(_translate("MainWindow", "?????????????????????? ??????????????????????????"))
        self.pushButton_9.setText(_translate("MainWindow", "?????????????????????????? ??????????????????????????"))
        self.pushButton_10.setText(_translate("MainWindow", "????????-?????????????? ??????????????????????????"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">?????????? ??????????????</span></p></body></html>"))

        def btn1_img():
            print("ez test1")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/1.jpg);")

        def btn2_img():
            print("ez test2")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/2.jpg);")

        def btn3_img():
            print("ez test3")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/3.jpg);")

        def btn4_img():
            print("ez test4")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/4.jpg);")

        def btn5_img():
            print("ez test5")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/5.jpg);")

        def btn6_img():
            print("ez test6")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/6.jpg);")

        def btn7_img():
            print("ez test7")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/7.jpg);")

        def btn8_img():
            print("ez test8")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/8.jpg);")

        def btn9_img():
            print("ez test9")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/9.jpg);")

        def btn10_img():
            print("ez test10")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/10.jpg);")

        self.pushButton_2.clicked.connect(btn1_img)
        self.pushButton_3.clicked.connect(btn2_img)
        self.pushButton_4.clicked.connect(btn3_img)
        self.pushButton_5.clicked.connect(btn4_img)
        self.pushButton_6.clicked.connect(btn5_img)
        self.pushButton_7.clicked.connect(btn6_img)
        self.pushButton_8.clicked.connect(btn7_img)
        self.pushButton_9.clicked.connect(btn8_img)
        self.pushButton_10.clicked.connect(btn9_img)
        self.pushButton.clicked.connect(btn10_img)


stylesheet = """
    QMainWindow {
        background-image: url("C:/Users/malyc/Desktop/diplom/prog/progimg/back.jpg");
        background-repeat: no-repeat; 
        background-position: center;
    }
"""
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    app.setStyleSheet(stylesheet)
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
