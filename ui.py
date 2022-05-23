import io
import sys

import folium
from PyQt5.QtWidgets import QMessageBox

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

import db_connector
from db_connector import *


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initWindow()

    def openDialog(self):
        #      pass
        dialog = ClssDialog(self)
        dialog.exec_()

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

        lay.addWidget(self.view)

        # ADDING MAP
        m = folium.Map(
            location=[63.30388759323694, 87.6987889680534], zoom_start=2
        )
        folium.Marker(location=[54.241330, 136.157046], popup="Проектная мощность — 5,5 млрд куб. м газа в год. Телефон 8-499-123-312", tooltip="").add_to(m)
        folium.Marker(location=[62.015284, 166.567203], popup="", tooltip="").add_to(m)
        folium.Marker(location=[69.475530, 115.414859], popup="", tooltip="").add_to(m)
        folium.Marker(location=[66.088831, 73.227359], popup="", tooltip="").add_to(m)
        folium.Marker(location=[60.055010, 29.809390], popup="", tooltip="").add_to(m)
        folium.Marker(location=[66.088831, 73.227359], popup="", tooltip="").add_to(m)
        folium.Marker(location=[63.308500, 114.360171], popup="", tooltip="").add_to(m)
        folium.Marker(location=[66.792137, 90.278140], popup="", tooltip="").add_to(m)
        folium.Marker(location=[69.659777, 159.887515], popup="", tooltip="").add_to(m)

        data = io.BytesIO()
        m.save(data, close_file=False)
        self.view.setHtml(data.getvalue().decode())

        # CHANGING IMG'S
        def btn1_img():
            print("DEBUG TEST: 10")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/1.jpg);")
            db_connector.connect("localhost", "dip_base_10", "root1", "root")

        def btn2_img():
            print("DEBUG TEST: 2")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/2.jpg);")
            db_connector.connect("localhost", "dip_base_2", "root1", "root")

        def btn3_img():
            print("DEBUG TEST: 3")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/3.jpg);")
            db_connector.connect("localhost", "dip_base_3", "root1", "root")

        def btn4_img():
            print("DEBUG TEST: 4")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/4.jpg);")
            db_connector.connect("localhost", "dip_base_4", "root1", "root")

        def btn5_img():
            print("DEBUG TEST: 5")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/5.jpg);")
            db_connector.connect("localhost", "dip_base_5", "root1", "root")

        def btn6_img():
            print("DEBUG TEST: 6")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/6.jpg);")
            db_connector.connect("localhost", "dip_base_6", "root1", "root")

        def btn7_img():
            print("DEBUG TEST: 7")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/7.jpg);")
            db_connector.connect("localhost", "dip_base_7", "root1", "root")

        def btn8_img():
            print("DEBUG TEST: 8")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/8.jpg);")
            db_connector.connect("localhost", "dip_base_8", "root1", "root")

        def btn9_img():
            print("DEBUG TEST: 9")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/9.jpg);")
            db_connector.connect("localhost", "dip_base_9", "root1", "root")

        def btn10_img():
            print("DEBUG TEST: 1")
            self.img.setStyleSheet("background-image: url(C:/Users/malyc/Desktop/diplom/prog/progimg/10.jpg);")
            db_connector.connect("localhost", "dip_base_1", "root1", "root")
            # QMessageBox.critical(self, "Обнаружено превышение значения на датчике", "Датчик - значение")

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
        self.pushButton.clicked.connect(self.openDialog)
        self.pushButton_2.clicked.connect(self.openDialog)
        self.pushButton_3.clicked.connect(self.openDialog)
        self.pushButton_4.clicked.connect(self.openDialog)
        self.pushButton_5.clicked.connect(self.openDialog)
        self.pushButton_6.clicked.connect(self.openDialog)
        self.pushButton_7.clicked.connect(self.openDialog)
        self.pushButton_8.clicked.connect(self.openDialog)
        self.pushButton_9.clicked.connect(self.openDialog)
        self.pushButton_10.clicked.connect(self.openDialog)


stylesheet = """
        QMainWindow {
            background-image: url("C:/Users/malyc/Desktop/diplom/prog/progimg/back.jpg");
        }
     """


class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)



        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Обнаружено превышение значения на датчике: Датчик: gas_detector - 115")
        self.verticalLayout.addWidget(self.label)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButton)
        self.setWindowTitle("Обнаружен датчик с повышенным значением")
        self.pushButton.setText("Ручное управление")

        self.pushButton1 = QtWidgets.QPushButton(self)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButton1)
        self.pushButton1.setText("Сигнал сотрудникам о попытке самостоятельно локально потушить")

        self.pushButton2 = QtWidgets.QPushButton(self)
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.btnClosed)
        self.verticalLayout.addWidget(self.pushButton2)
        self.pushButton2.setText("Вызвать 112")

    def btnClosed(self):
        self.close()


def alerter(self, name_catch, value_catch):
    QMessageBox.critical(self, "Обнаружено превышение значения на датчике", "Датчик", name_catch, " - ", value_catch)


if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    window = Window()
    App.setStyleSheet(stylesheet)
    window.show()
    sys.exit(App.exec())
