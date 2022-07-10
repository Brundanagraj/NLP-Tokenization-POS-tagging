# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yes.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
import qt_rc
import qt_rc_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1301, 688)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"background-image: url(:/back/images/nlp.jpeg);\n"
"\n"
"border-color: rgb(0, 0, 0);\n"
"selection-color: rgb(255, 0, 127);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 180, 151, 61))
        self.label.setStyleSheet(u"font: 12pt \"Algerian\";")
        self.input = QTextEdit(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(400, 170, 601, 71))
        self.input.setStyleSheet(u"font: 18pt \"Algerian\";\n"
    "background-image: url(:/back/images/download.jfif);")

        self.tokenize = QPushButton(self.centralwidget)
        self.tokenize.setObjectName(u"tokenize")
        self.tokenize.setGeometry(QRect(180, 320, 161, 61))
        self.tokenize.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 16pt \"Algerian\";")
        self.parsing = QPushButton(self.centralwidget)
        self.parsing.setObjectName(u"parsing")
        self.parsing.setGeometry(QRect(700, 320, 171, 61))
        self.parsing.setStyleSheet(u"background-color: rgb(170, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 255);\n"
"\n"
"font: 16pt \"Algerian\";\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.tokenizeresponse = QLabel(self.centralwidget)
        self.tokenizeresponse.setObjectName(u"tokenizeresponse")
        self.tokenizeresponse.setGeometry(QRect(60, 410, 1101, 61))
        self.tokenizeresponse.setStyleSheet(u"font: 16pt \"Algerian\";\n"
"background-image: url(:/back/images/download.jfif);\n"
"background-color: rgb(0, 255, 255);")
        self.parsingresponse = QTextEdit(self.centralwidget)
        self.parsingresponse.setObjectName(u"parsingresponse")
        self.parsingresponse.setGeometry(QRect(60, 500, 1101, 71))
        self.parsingresponse.setStyleSheet(u"font: 16pt \"Algerian\";\n"
"background-image: url(:/back/images/download.jfif);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 10, 561, 81))
        self.label_2.setStyleSheet(u"font: 20pt \"Algerian\";\n"
"color: rgb(85, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1301, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"    Enter Sentence:", None))
        self.tokenize.setText(QCoreApplication.translate("MainWindow", u"Tokenize", None))
        self.parsing.setText(QCoreApplication.translate("MainWindow", u"Parsing", None))
        self.tokenizeresponse.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"SENTENCE TOKENIZATION AND PARSING", None))
    # retranslateUi

