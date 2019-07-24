# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentapp.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.framebuttons = QtWidgets.QFrame(self.centralwidget)
        self.framebuttons.setGeometry(QtCore.QRect(241, 180, 351, 231))
        self.framebuttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framebuttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framebuttons.setObjectName("framebuttons")
        self.biodata = QtWidgets.QPushButton(self.framebuttons)
        self.biodata.setGeometry(QtCore.QRect(80, 30, 191, 41))
        self.biodata.setObjectName("biodata")
        self.performance = QtWidgets.QPushButton(self.framebuttons)
        self.performance.setGeometry(QtCore.QRect(80, 90, 191, 41))
        self.performance.setObjectName("performance")
        self.finance = QtWidgets.QPushButton(self.framebuttons)
        self.finance.setGeometry(QtCore.QRect(80, 150, 191, 41))
        self.finance.setObjectName("finance")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(11, 40, 781, 441))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.schnameframe = QtWidgets.QFrame(self.centralwidget)
        self.schnameframe.setGeometry(QtCore.QRect(20, 50, 761, 41))
        self.schnameframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.schnameframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.schnameframe.setObjectName("schnameframe")
        self.schoolname = QtWidgets.QLabel(self.schnameframe)
        self.schoolname.setGeometry(QtCore.QRect(270, 10, 231, 20))
        self.schoolname.setObjectName("schoolname")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.biodata.setText(_translate("MainWindow", "STUDENT BIO DATA"))
        self.performance.setText(_translate("MainWindow", "STUDENT MARKS"))
        self.finance.setText(_translate("MainWindow", "FINANCES"))
        self.schoolname.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">THE SCHOOL NAME</span></p></body></html>"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
