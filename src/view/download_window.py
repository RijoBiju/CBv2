# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download_widgetgEuVMg.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *  

from view import gui_images

class Download_Widget(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(721, 402)
        Form.setStyleSheet(u"QWidget{\n"
"	border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 203);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;\n"
"border-radius: 10px;")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"background: transparent;\n"
"border-radius: 10px;")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(120, 60, 481, 241))
        self.frame_2.setStyleSheet(u"background-color: rgba(33, 33, 33, 225);\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.create_shortcut = QCheckBox(self.frame_2)
        self.create_shortcut.setObjectName(u"create_shortcut")
        self.create_shortcut.setGeometry(QRect(20, 190, 291, 17))
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.create_shortcut.setFont(font)
        self.create_shortcut.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 13px \"Ubuntu\";\n"
"border: none;")
        self.location_label = QLabel(self.frame_2)
        self.location_label.setObjectName(u"location_label")
        self.location_label.setGeometry(QRect(10, 10, 461, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.location_label.sizePolicy().hasHeightForWidth())
        self.location_label.setSizePolicy(sizePolicy)
        self.location_label.setFont(font)
        self.location_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 16px \"Ubuntu\";\n"
"")
        self.location_label.setAlignment(Qt.AlignCenter)
        self.download_location = QLineEdit(self.frame_2)
        self.download_location.setObjectName(u"download_location")
        self.download_location.setGeometry(QRect(20, 80, 351, 31))
        self.download_location.setFont(font)
        self.download_location.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 20);\n"
"font: 15px \"Ubuntu\";")
        self.start = QPushButton(self.frame_2)
        self.start.setObjectName(u"start")
        self.start.setCursor(QCursor(Qt.PointingHandCursor))
        self.start.setGeometry(QRect(360, 190, 101, 31))
        self.start.setFont(font)
        self.start.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font: 12px \"Ubuntu\";\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.available_space = QLabel(self.frame_2)
        self.available_space.setObjectName(u"available_space")
        self.available_space.setGeometry(QRect(170, 123, 281, 21))
        self.available_space.setFont(font)
        self.available_space.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 13px \"Ubuntu\";\n"
"")
        self.filedialog = QPushButton(self.frame_2)
        self.filedialog.setObjectName(u"filedialog")
        self.filedialog.setCursor(QCursor(Qt.PointingHandCursor))
        self.filedialog.setGeometry(QRect(380, 80, 81, 31))
        font1 = QFont()
        font1.setFamily(u"Ubuntu")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.filedialog.setFont(font1)
        self.filedialog.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font: 10pt \"Ubuntu\";\n"
"	image: url(:/icons/images/icons/cil-folder-open.png);\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 125, 61, 16))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 13px \"Ubuntu\";\n"
"")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 125, 71, 16))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 13px \"Ubuntu\";\n"
"")
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 50, 311, 20))
        self.label_8.setStyleSheet(u"color: rgb(255, 93, 0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_8.setAlignment(Qt.AlignCenter)
        self.minimizeAppBtn_2 = QPushButton(self.frame_2)
        self.minimizeAppBtn_2.setObjectName(u"minimizeAppBtn_2")
        self.minimizeAppBtn_2.setGeometry(QRect(420, 10, 28, 28))
        self.minimizeAppBtn_2.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn_2.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeAppBtn_2.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0);")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn_2.setIcon(icon)
        self.minimizeAppBtn_2.setIconSize(QSize(20, 20))
        self.close_download_2 = QPushButton(self.frame_2)
        self.close_download_2.setObjectName(u"close_download_2")
        self.close_download_2.setGeometry(QRect(450, 10, 28, 28))
        self.close_download_2.setMinimumSize(QSize(28, 28))
        self.close_download_2.setMaximumSize(QSize(28, 28))
        self.close_download_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_download_2.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_download_2.setIcon(icon1)
        self.close_download_2.setIconSize(QSize(20, 20))
        self.create_shortcut_2 = QCheckBox(self.frame_2)
        self.create_shortcut_2.setObjectName(u"create_shortcut_2")
        self.create_shortcut_2.setGeometry(QRect(20, 210, 291, 17))
        self.create_shortcut_2.setFont(font)
        self.create_shortcut_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 13px \"Ubuntu\";\n"
"border: none;")
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"background: transparent;\n"
"border-radius: 10px;")
        self.frame_6 = QFrame(self.page_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(120, 60, 481, 241))
        self.frame_6.setStyleSheet(u"background-color: rgba(33, 33, 33, 225);\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.loadsave = QPushButton(self.frame_6)
        self.loadsave.setObjectName(u"loadsave")
        self.loadsave.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadsave.setGeometry(QRect(90, 160, 75, 23))
        self.loadsave.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font: 10px \"Ubuntu\";\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.nosave = QPushButton(self.frame_6)
        self.nosave.setObjectName(u"nosave")
        self.nosave.setCursor(QCursor(Qt.PointingHandCursor))
        self.nosave.setGeometry(QRect(320, 160, 75, 23))
        self.nosave.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font:  10px \"Ubuntu\";\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 90, 401, 41))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12px \"Ubuntu\";")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.minimizeAppBtn_3 = QPushButton(self.frame_6)
        self.minimizeAppBtn_3.setObjectName(u"minimizeAppBtn_3")
        self.minimizeAppBtn_3.setGeometry(QRect(420, 10, 28, 28))
        self.minimizeAppBtn_3.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn_3.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeAppBtn_3.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.minimizeAppBtn_3.setIcon(icon)
        self.minimizeAppBtn_3.setIconSize(QSize(20, 20))
        self.close_download_3 = QPushButton(self.frame_6)
        self.close_download_3.setObjectName(u"close_download_3")
        self.close_download_3.setGeometry(QRect(450, 10, 28, 28))
        self.close_download_3.setMinimumSize(QSize(28, 28))
        self.close_download_3.setMaximumSize(QSize(28, 28))
        self.close_download_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_download_3.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.close_download_3.setIcon(icon1)
        self.close_download_3.setIconSize(QSize(20, 20))
        self.download_progress_2 = QProgressBar(self.frame_6)
        self.download_progress_2.setObjectName(u"download_progress_2")
        self.download_progress_2.setGeometry(QRect(30, 160, 431, 31))
        self.download_progress_2.setFont(font)
        self.download_progress_2.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(103, 103, 103);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.download_progress_2.setValue(0)
        self.download_progress_2.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setStyleSheet(u"background: transparent;")
        self.frame_7 = QFrame(self.page_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(120, 60, 481, 241))
        self.frame_7.setStyleSheet(u"background-color: rgba(33, 33, 33, 225);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.download_progress = QProgressBar(self.frame_7)
        self.download_progress.setObjectName(u"download_progress")
        self.download_progress.setGeometry(QRect(20, 161, 431, 31))
        self.download_progress.setFont(font)
        self.download_progress.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(103, 103, 103);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.download_progress.setValue(0)
        self.download_progress.setAlignment(Qt.AlignCenter)
        self.status = QLabel(self.frame_7)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(10, 60, 461, 31))
        font2 = QFont()
        font2.setFamily(u"Ubuntu")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(1)
        self.status.setFont(font2)
        self.status.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:rgba(105,105,105,0);\n"
"font: 15 px \"Ubuntu\";\n"
"")
        self.status.setAlignment(Qt.AlignCenter)
        self.game_name = QLabel(self.frame_7)
        self.game_name.setObjectName(u"game_name")
        self.game_name.setGeometry(QRect(10, 20, 461, 31))
        self.game_name.setFont(font)
        self.game_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:rgba(105,105,105,0);\n"
"font: 16px \"Ubuntu\";")
        self.game_name.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.frame_7)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 205, 431, 21))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font: 10px \"Ubuntu\";\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 135, 261, 20))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:rgba(105,105,105,0);\n"
"font: 12px \"Ubuntu\";\n"
"border: none;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.minimizeAppBtn_4 = QPushButton(self.frame_7)
        self.minimizeAppBtn_4.setObjectName(u"minimizeAppBtn_4")
        self.minimizeAppBtn_4.setGeometry(QRect(420, 10, 28, 28))
        self.minimizeAppBtn_4.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn_4.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeAppBtn_4.setStyleSheet(u"border: none;")
        self.minimizeAppBtn_4.setIcon(icon)
        self.minimizeAppBtn_4.setIconSize(QSize(20, 20))
        self.close_download_4 = QPushButton(self.frame_7)
        self.close_download_4.setObjectName(u"close_download_4")
        self.close_download_4.setGeometry(QRect(450, 10, 28, 28))
        self.close_download_4.setMinimumSize(QSize(28, 28))
        self.close_download_4.setMaximumSize(QSize(28, 28))
        self.close_download_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_download_4.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.close_download_4.setIcon(icon1)
        self.close_download_4.setIconSize(QSize(20, 20))
        self.ETA = QLineEdit(self.frame_7)
        self.ETA.setObjectName(u"ETA")
        self.ETA.setGeometry(QRect(15, 105, 201, 21))
        self.ETA.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:rgba(105,105,105,0);\n"
"font: 12px \"Ubuntu\";\n"
"border: none;")
        self.ETA.setReadOnly(True)
        self.ETA_2 = QLineEdit(self.frame_7)
        self.ETA_2.setObjectName(u"ETA_2")
        self.ETA_2.setGeometry(QRect(15, 135, 291, 21))
        self.ETA_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color:rgba(105,105,105,0);\n"
"font: 12px \"Ubuntu\";\n"
"border: none;")
        self.ETA_2.setReadOnly(True)
        self.close_download_5 = QPushButton(self.frame_7)
        self.close_download_5.setObjectName(u"close_download_5")
        self.close_download_5.setGeometry(QRect(420, 10, 28, 28))
        self.close_download_5.setMinimumSize(QSize(28, 28))
        self.close_download_5.setMaximumSize(QSize(28, 28))
        self.close_download_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_download_5.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.close_download_5.setIcon(icon1)
        self.close_download_5.setIconSize(QSize(20, 20))
        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	border-radius: 10px;\n"
"}\n"
"QLabel{\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 203);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.create_shortcut.setText(QCoreApplication.translate("Form", u"Create Desktop Shortcut", None))
        self.location_label.setText(QCoreApplication.translate("Form", u"Download Location", None))
        self.download_location.setText(QCoreApplication.translate("Form", u"C:\\CBLauncher\\Games", None))
        self.start.setText(QCoreApplication.translate("Form", u"Continue", None))
        self.available_space.setText(QCoreApplication.translate("Form", u"Available Disk Space: 200 GB", None))
        self.filedialog.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"File Size:", None))
        self.label_2.setText("")
        self.label_8.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn_2.setToolTip(QCoreApplication.translate("Form", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn_2.setText("")
#if QT_CONFIG(tooltip)
        self.close_download_2.setToolTip(QCoreApplication.translate("Form", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_download_2.setText("")
        self.create_shortcut_2.setText(QCoreApplication.translate("Form", u"Create Start Menu Shortcut", None))
        self.loadsave.setText(QCoreApplication.translate("Form", u"Yes", None))
        self.nosave.setText(QCoreApplication.translate("Form", u"No", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"tests", None))
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn_3.setToolTip(QCoreApplication.translate("Form", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn_3.setText("")
#if QT_CONFIG(tooltip)
        self.close_download_3.setToolTip(QCoreApplication.translate("Form", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_download_3.setText("")
        self.status.setText(QCoreApplication.translate("Form", u"Downloading...", None))
        self.game_name.setText(QCoreApplication.translate("Form", u"Red Dead Redemption 2", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Start Game", None))
        self.label_3.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn_4.setToolTip(QCoreApplication.translate("Form", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn_4.setText("")
#if QT_CONFIG(tooltip)
        self.close_download_4.setToolTip(QCoreApplication.translate("Form", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_download_4.setText("")
#if QT_CONFIG(tooltip)
        self.close_download_5.setToolTip(QCoreApplication.translate("Form", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_download_5.setText("")
    # retranslateUi

