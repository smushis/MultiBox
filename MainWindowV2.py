# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultiBox.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(580, 150, 621, 321))
        self.label1.setBaseSize(QtCore.QSize(531, 261))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label1.setFont(font)
        self.label1.setStyleSheet("")
        self.label1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label1.setWordWrap(True)
        self.label1.setObjectName("label1")
        self.Photo = QtWidgets.QLabel(self.centralwidget)
        self.Photo.setGeometry(QtCore.QRect(310, 180, 201, 201))
        self.Photo.setStyleSheet("")
        self.Photo.setText("")
        self.Photo.setPixmap(QtGui.QPixmap("img/Twitter/Smushis.png"))
        self.Photo.setObjectName("Photo")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(330, 390, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 170, 291, 281))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/twitter.png"))
        self.label.setObjectName("label")
        self.cadreTweet = QtWidgets.QLabel(self.centralwidget)
        self.cadreTweet.setGeometry(QtCore.QRect(530, -150, 761, 921))
        self.cadreTweet.setText("")
        self.cadreTweet.setPixmap(QtGui.QPixmap("img/bkgnd.png"))
        self.cadreTweet.setObjectName("cadreTweet")
        self.Twitch_Title = QtWidgets.QLabel(self.centralwidget)
        self.Twitch_Title.setGeometry(QtCore.QRect(580, 270, 361, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Twitch_Title.setFont(font)
        self.Twitch_Title.setObjectName("Twitch_Title")
        self.cadreTweet.raise_()
        self.Photo.raise_()
        self.username.raise_()
        self.label1.raise_()
        self.label.raise_()
        self.Twitch_Title.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Results XXXXXXXX d"))
        self.username.setText(_translate("MainWindow", "TextLabel"))
        self.Twitch_Title.setText(_translate("MainWindow", "TextLabel"))
import ressources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
