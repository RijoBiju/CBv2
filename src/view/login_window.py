from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

#import dunno_rc
#import resources_rc

class LoginPage(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(650, 222)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 632, 204))
        self.frame.setStyleSheet(u"background-color: rgb(33, 33, 33);\n"
"border-radius: 10px;")

        self.logoLabel = QLabel(self.frame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(0, 20, 221, 171))
        self.logoLabel.setPixmap(QPixmap(u":/games/cb"))
        self.logoLabel.setScaledContents(True)

        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.invaliddetailsPlainTextEdit = QPlainTextEdit(self.frame)
        self.invaliddetailsPlainTextEdit.setObjectName(u"invaliddetailsPlainTextEdit")
        self.invaliddetailsPlainTextEdit.setGeometry(QRect(20, 110, 201, 21))
        self.invaliddetailsPlainTextEdit.setFont(font)
        self.invaliddetailsPlainTextEdit.setLayoutDirection(Qt.LeftToRight)
        self.invaliddetailsPlainTextEdit.setStyleSheet(u"background-color: rgba(225, 225, 225, 0);\n"
"color: rgb(255, 0, 4);\n"
"font: 12px;")
        self.invaliddetailsPlainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.invaliddetailsPlainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.invaliddetailsPlainTextEdit.setReadOnly(True)

        self.accountcreationLabel = QLabel(self.frame)
        self.accountcreationLabel.setObjectName(u"accountcreationLabel")
        self.accountcreationLabel.setText("Create an account")
        self.accountcreationLabel.setGeometry(QRect(480, 115, 121, 20))
        self.accountcreationLabel.setFont(font)
        self.accountcreationLabel.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 13px \"Ubuntu\";")

        self.usernameLineEdit = QLineEdit(self.frame)
        self.usernameLineEdit.setObjectName(u"usernameLineEdit")
        self.usernameLineEdit.setPlaceholderText("Username")
        self.usernameLineEdit.setGeometry(QRect(260, 30, 341, 31))
        self.usernameLineEdit.setFont(font)
        self.usernameLineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(225, 225, 225, 20);\n"
"font: 13px \"Ubuntu\";")

        self.passwordLineEdit = QLineEdit(self.frame)
        self.passwordLineEdit.setObjectName(u"passwordLineEdit")
        self.passwordLineEdit.setPlaceholderText("Password")
        self.passwordLineEdit.setGeometry(QRect(260, 70, 341, 31))
        self.passwordLineEdit.setFont(font)
        self.passwordLineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(225, 225, 225, 20);\n"
"font: 13px \"Ubuntu\";")

        self.loginPushButton = QPushButton(self.frame)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setText("Login")
        self.loginPushButton.setGeometry(QRect(330, 160, 91, 21))
        self.loginPushButton.setFont(font)
        self.loginPushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12px \"Ubuntu\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.skipPushButton = QPushButton(self.frame)
        self.skipPushButton.setObjectName(u"skipPushButton")
        self.skipPushButton.setText("Skip")
        self.skipPushButton.setGeometry(QRect(450, 160, 91, 21))
        self.skipPushButton.setFont(font)
        self.skipPushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12px \"Ubuntu\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")

        self.remembermeCheckBox = QCheckBox(self.frame)
        self.remembermeCheckBox.setObjectName(u"remembermeCheckBox")
        self.remembermeCheckBox.setText("Keep me logged in")
        self.remembermeCheckBox.setGeometry(QRect(260, 120, 171, 17))
        self.remembermeCheckBox.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12px \"Ubuntu\";")

        self.statusLineEdit = QLineEdit(self.frame)
        self.statusLineEdit.setFont(font)
        self.statusLineEdit.setAlignment(Qt.AlignCenter)
        self.statusLineEdit.setGeometry(155, 70, 341, 31)
        self.statusLineEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12px \"Ubuntu\";")
        self.statusLineEdit.setVisible(False)

