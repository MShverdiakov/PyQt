# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 370, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);\n"
"")
        self.label_result.setObjectName("label_result")
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(0, 320, 150, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(150, 320, 150, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(197, 131, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_equal.setObjectName("btn_equal")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 230, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 230, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 230, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 140, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 140, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 140, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 50, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 50, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);\n"
"")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 50, 100, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_9.setObjectName("btn_9")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(300, 50, 70, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(300, 140, 70, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(300, 230, 70, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_multiply.setFont(font)
        self.btn_multiply.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_multiply.setObjectName("btn_multiply")
        self.btn_dev = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dev.setGeometry(QtCore.QRect(300, 320, 70, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.btn_dev.setFont(font)
        self.btn_dev.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(236, 157, 0);")
        self.btn_dev.setObjectName("btn_dev")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_multiply.setText(_translate("MainWindow", "*"))
        self.btn_dev.setText(_translate("MainWindow", "/"))

    def add_functions(self):
        self.btn_zero.clicked.connect(lambda: self.write_number(self.btn_zero.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_multiply.clicked.connect(lambda: self.write_number(self.btn_multiply.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_dev.clicked.connect(lambda: self.write_number(self.btn_dev.text()))

        self.btn_equal.clicked.connect(self.results)

    def write_number(self, number):
        if self.label_result.text() == '0' or self.is_equal:
            self.label_result.setText(number)
            self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text() + number)

    def results(self):
        if not self.is_equal:
            res = eval(self.label_result.text())
            self.label_result.setText(str(res))
            self.is_equal = True
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("2 знака равно подряд")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset | QMessageBox.Ok)
            error.setInformativeText("зачем ты так?")
            error.setDetailedText("Detailed text")
            error.buttonClicked.connect(self.popup_action)
            error.exec_()

    def popup_action(self, btn):
        if btn.text() == "Ok":
            print('error: Ok')
        elif btn.text() == 'Reset':
            self.label_result.setText('0')
            self.is_equal = False


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
