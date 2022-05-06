import io
import sys

import folium

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.tr("MAP PROJECT"))
        self.setFixedSize(958, 661)
        self.buttonUI()

    def buttonUI(self):
        shortPathButton = QtWidgets.QPushButton(self.tr(""))
        shortPathButton.setFixedSize(210, 10)
        shortPathButton.setFlat(False)



        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QHBoxLayout(central_widget)

        self.view = QtWebEngineWidgets.QWebEngineView(central_widget)
        self.view.setContentsMargins(300, 50, 50, 50)
        # self.view.setGeometry(QtCore.QRect(10, 70, 280, 171))
        # self.view.setBaseSize(100, 250)

        self.scrollArea = QtWidgets.QScrollArea(central_widget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 280, 171))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")


        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 228, 540))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setBaseSize(100, 250)

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
        self.pushButton_2.setFlat(False)
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
        self.pushButton_4.setFlat(False)
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
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(central_widget)
        self.label.setGeometry(QtCore.QRect(60, 10, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.img = QtWidgets.QLabel(central_widget)
        self.img.setEnabled(False)
        self.img.setGeometry(QtCore.QRect(10, 270, 280, 351))
        self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/no_photo.jpg);")
        self.img.setText("")
        self.img.setObjectName("img")


        # NAMES TO BUTTONS
        self.pushButton_2.setText(" 8. Бованенковское месторождение")
        self.pushButton_4.setText(" 7. Заполярное месторождение")
        self.pushButton_5.setText(" 6. Каменномысское-море")
        self.pushButton.setText(" 1. Камчатка")
        self.pushButton_3.setText(" 2. Ковыктинское месторождение")
        self.pushButton_8.setText(" 4. Приразломное месторождение")
        self.pushButton_6.setText(" 3. «Сахалин-3»")
        self.pushButton_7.setText(" 5. Уренгойское месторождение")
        self.pushButton_9.setText(" 9. Харасавэйское месторождение")
        self.pushButton_10.setText(" 10. Южно-Русское месторождение")
        self.label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Выбор объекта</span></p></body></html>")

        # button_container = QtWidgets.QWidget()
        # vlay = QtWidgets.QVBoxLayout(button_container)
        #
        # vlay.setSpacing(20)
        # vlay.addStretch()
        # vlay.addWidget(shortPathButton)
        # # vlay.addWidget(self.pushButton_2)
        # # vlay.addWidget(self.pushButton_3)
        # # vlay.addWidget(self.pushButton_4)
        # # vlay.addWidget(self.pushButton_5)
        # # vlay.addWidget(self.pushButton_6)
        # # vlay.addWidget(self.pushButton_7)
        # # vlay.addWidget(self.pushButton_8)
        #
        # vlay.addStretch()
        # lay.addWidget(button_container)
        # lay.addWidget(self.scrollArea, stretch=1)
        # lay.addWidget(self.scrollAreaWidgetContents, stretch=100)
        # lay.setSpacing(20)
        lay.addWidget(self.view)


        # ADDING MAP
        m = folium.Map(
            location=[63.30388759323694, 87.6987889680534], zoom_start=2
        )
        #marker1 = folium.features.CustomIcon("C:/Users/malyc/Desktop/diplom/prog/progimg/marker1.png)", icon_size=(100, 100))
        #folium.Marker(location=[14,14], icon=marker1).add_to(m)
        #.Mafoliumrker(location=[63.30, 87.69], popup="", tooltip="").add_to(m)
        folium.Marker(location=[14, 14], popup="", tooltip="").add_to(m)
        folium.Marker(location=[123, 14], popup="", tooltip="").add_to(m)
        folium.Marker(location=[354, 334], popup="", tooltip="").add_to(m)
        folium.Marker(location=[123, 321], popup="", tooltip="").add_to(m)
        # folium.Marker(location=[14, 14], popup="", tooltip="").add_to(m)
        # folium.Marker(location=[14, 14], popup="", tooltip="").add_to(m)
        # folium.Marker(location=[14, 14], popup="", tooltip="").add_to(m)
        # folium.Marker(location=[14, 14], popup="", tooltip="").add_to(m)


        data = io.BytesIO()
        m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())

        # CHANGING IMG'S
        def btn1_img():
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
        }
     """

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = Window()
    App.setStyleSheet(stylesheet)
    window.show()
    sys.exit(App.exec())