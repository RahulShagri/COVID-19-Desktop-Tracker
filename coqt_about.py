# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coqt_about.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about_window(object):
    def setupUi_about(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(481, 444)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(9)
        about_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/app_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        about_window.setWindowIcon(icon)
        about_window.setWindowOpacity(0.94)
        about_window.setDocumentMode(False)
        about_window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(about_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 221, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 281, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 100, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 150, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 240, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setWordWrap(True)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 260, 261, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setOpenExternalLinks(False)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 290, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 310, 381, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(50, 210, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.line.setFont(font)
        self.line.setStyleSheet("color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 370, 331, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 390, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 340, 391, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setBold(False)
        font.setWeight(50)
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(-690, -50, 1191, 621))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap())
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_11.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.line.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.line_2.raise_()
        about_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "About COVID-19 Desktop Tracker"))
        self.label.setText(_translate("about_window", "Version 1.1"))
        self.label_2.setText(_translate("about_window", "COVID-19 Desktop Tracker"))
        self.label_3.setText(_translate("about_window", "COVID-19 Desktop Tracker is a Graphical User Interface to retrieve data related to COVID-19 (SARS-CoV-2)."))
        self.label_4.setText(_translate("about_window", "This software enables the user to retrieve data, and visualize the data in the form of graphs."))
        self.label_5.setText(_translate("about_window", "The latest data is retrieved from:"))
        self.label_6.setText(_translate("about_window", "https://github.com/NovelCOVID/API"))
        self.label_7.setText(_translate("about_window", "The data for the plots is retrieved from:"))
        self.label_8.setText(_translate("about_window", "https://github.com/AlaeddineMessadi/COVID-19-REPORT-API"))
        self.label_9.setText(_translate("about_window", "Desgined and maintained by Rahul Shagrithaya"))
        self.label_10.setText(_translate("about_window", "https://github.com/RahulShagri"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    about_window = QtWidgets.QMainWindow()
    ui = Ui_about_window()
    ui.setupUi(about_window)
    about_window.show()
    sys.exit(app.exec_())