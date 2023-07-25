# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.setWindowModality(Qt.NonModal)
        Login.setEnabled(True)
        Login.resize(400, 400)
        Login.setMaximumSize(QSize(400, 400))
        Login.setStyleSheet(u"\n"
"background-color: rgba(0,80,121,0.58);")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 150, 311, 201))
        self.frame.setStyleSheet(u"background-color: rgba(0,0, 0,0.41);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(70, 90, 151, 20))
        font = QFont()
        font.setPointSize(11)
        self.txt_senha.setFont(font)
        self.txt_senha.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(80, 140, 121, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"\n"
"	background-color: rgb(217, 217, 217);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"	border-radius:10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	\n"
"	color: rgb(217, 217, 217);\n"
"	\n"
"	\n"
"}")
        self.txt_usuario = QLineEdit(self.frame)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(70, 40, 151, 20))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_usuario.sizePolicy().hasHeightForWidth())
        self.txt_usuario.setSizePolicy(sizePolicy)
        self.txt_usuario.setFont(font)
        self.txt_usuario.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.txt_usuario.setAlignment(Qt.AlignCenter)
        self.img_login = QLabel(Login)
        self.img_login.setObjectName(u"img_login")
        self.img_login.setGeometry(QRect(130, 20, 141, 141))
        self.img_login.setStyleSheet(u"background-color: rgba(0,80,121,0.10);")
        self.img_login.setPixmap(QPixmap(u"imagens/logo_2optica.png"))
        self.img_login.setScaledContents(True)
        self.img_login.raise_()
        self.frame.raise_()
        QWidget.setTabOrder(self.txt_usuario, self.txt_senha)
        QWidget.setTabOrder(self.txt_senha, self.btn_login)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("Login", u"SENHA", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"USUARIO", None))
        self.img_login.setText("")
    # retranslateUi

