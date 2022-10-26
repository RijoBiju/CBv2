# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from view import gui_images
#import resources_rc
#import dunno_rc
#import font_rc
#import dunno_rc

class CBLauncher(object):
    def setupUi(self, CBLauncher):
        if not CBLauncher.objectName():
            CBLauncher.setObjectName(u"CB Launcher")
        CBLauncher.resize(1289, 781)
        CBLauncher.setMinimumSize(QSize(940, 560))
        CBLauncher.setStyleSheet(u"border-radius: 10px;\n"
"font: 10pt \"Ubuntu\";\n"
"")

        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.styleSheet = QWidget(CBLauncher)
        self.styleSheet.setObjectName(u"styleSheet")
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 13px \"Ubuntu\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background-c"
                        "olor: rgb(33,33,33);\n"
"	border: 1px solid rgb(33,33,33);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33,33,33);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/logo/CB);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 11px \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 10pt \"Ubuntu\";; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: (33,33,33);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 2"
                        "55, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(12, 117, 203);\n"
"}\n"
"\n"
"/* Title Men"
                        "u */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
""
                        "\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33,33,33);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(33,33,33);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButto"
                        "ns .QPushButton:pressed { background-color: rgb(12, 117, 203); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(33,33,33); }\n"
"#bottomBar QLabel { font-size: 10px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////"
                        "////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	bo"
                        "rder-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEd"
                        "it  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(12,117,203);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(12,117,203);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(12,117,203);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border:"
                        " none;\n"
"    background: rgb(12,117,203);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(12,117,203);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(12,117,203);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub"
                        "-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt"
                        ".png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	b"
                        "order-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(12, 117, 203);\n"
"	padding: 10px;\n"
"	background-color: rgb(12, 117, 203);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
""
                        "	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-rad"
                        "ius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")

        self.verticalLayout_17 = QVBoxLayout(self.styleSheet)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(10, 10, 10, 10)

        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")

        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)

        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))

        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))

        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))

        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        
        self.titleLeftApp.setFont(font)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        self.titleLeftDescription.setFont(font)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.smallpfpLabel = QLabel(self.topLogoInfo)
        self.smallpfpLabel.setObjectName(u"smallpfpLabel")
        self.smallpfpLabel.setGeometry(QRect(10, 5, 38, 38))
        self.smallpfpLabel.setPixmap(QPixmap(u":/images/images/logo/CB"))
        self.smallpfpLabel.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMinimumSize(QSize(0, 0))

        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)

        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))

        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())

        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 225))

        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.homePushButton = QPushButton(self.topMenu)
        self.homePushButton.setObjectName(u"homePushButton")
        sizePolicy.setHeightForWidth(self.homePushButton.sizePolicy().hasHeightForWidth())
        self.homePushButton.setSizePolicy(sizePolicy)
        self.homePushButton.setMinimumSize(QSize(0, 45))
        self.homePushButton.setFont(font)
        self.homePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.homePushButton.setLayoutDirection(Qt.LeftToRight)
        self.homePushButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.homePushButton)

        self.gamesPushButton = QPushButton(self.topMenu)
        self.gamesPushButton.setObjectName(u"gamesPushButton")
        sizePolicy.setHeightForWidth(self.gamesPushButton.sizePolicy().hasHeightForWidth())
        self.gamesPushButton.setSizePolicy(sizePolicy)
        self.gamesPushButton.setMinimumSize(QSize(0, 45))
        self.gamesPushButton.setFont(font)
        self.gamesPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.gamesPushButton.setLayoutDirection(Qt.LeftToRight)
        self.gamesPushButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-gamepad.png);")

        self.verticalLayout_8.addWidget(self.gamesPushButton)

        self.pushButton_2 = QPushButton(self.topMenu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())

        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(0, 45))
        self.pushButton_2.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-data-transfer-down.png);")

        self.verticalLayout_8.addWidget(self.pushButton_2)

        self.emulatorsPushButton = QPushButton(self.topMenu)
        self.emulatorsPushButton.setObjectName(u"emulatorsPushButton")
        sizePolicy.setHeightForWidth(self.emulatorsPushButton.sizePolicy().hasHeightForWidth())
        self.emulatorsPushButton.setSizePolicy(sizePolicy)
        self.emulatorsPushButton.setMinimumSize(QSize(0, 45))
        self.emulatorsPushButton.setFont(font)
        self.emulatorsPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.emulatorsPushButton.setLayoutDirection(Qt.LeftToRight)
        self.emulatorsPushButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-medical-cross.png);")

        self.verticalLayout_8.addWidget(self.emulatorsPushButton)

        self.downloadsPushButton = QPushButton(self.topMenu)
        self.downloadsPushButton.setObjectName(u"downloadsPushButton")
        sizePolicy.setHeightForWidth(self.downloadsPushButton.sizePolicy().hasHeightForWidth())
        self.downloadsPushButton.setSizePolicy(sizePolicy)
        self.downloadsPushButton.setMinimumSize(QSize(0, 45))
        self.downloadsPushButton.setFont(font)
        self.downloadsPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.downloadsPushButton.setLayoutDirection(Qt.LeftToRight)
        self.downloadsPushButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.downloadsPushButton)

        self.rclonePushButton = QPushButton(self.topMenu)
        self.rclonePushButton.setObjectName(u"rclonePushButton")
        sizePolicy.setHeightForWidth(self.rclonePushButton.sizePolicy().hasHeightForWidth())
        self.rclonePushButton.setSizePolicy(sizePolicy)
        self.rclonePushButton.setMinimumSize(QSize(0, 45))
        self.rclonePushButton.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-rss.png)")

        self.verticalLayout_8.addWidget(self.rclonePushButton)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.settings = QPushButton(self.bottomMenu)
        self.settings.setObjectName(u"settings")
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setMinimumSize(QSize(0, 45))
        self.settings.setFont(font)
        self.settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.settings.setLayoutDirection(Qt.LeftToRight)
        self.settings.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.settings)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.rightButtons)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(28, 28))
        self.pushButton.setMaximumSize(QSize(28, 28))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.minimizePushButton = QPushButton(self.rightButtons)
        self.minimizePushButton.setObjectName(u"minimizePushButton")
        self.minimizePushButton.setMinimumSize(QSize(28, 28))
        self.minimizePushButton.setMaximumSize(QSize(28, 28))
        self.minimizePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizePushButton.setIcon(icon1)
        self.minimizePushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizePushButton)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setFont(font)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closePushButton = QPushButton(self.rightButtons)
        self.closePushButton.setObjectName(u"closePushButton")
        self.closePushButton.setMinimumSize(QSize(28, 28))
        self.closePushButton.setMaximumSize(QSize(28, 28))
        self.closePushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.closePushButton.setIcon(icon)
        self.closePushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closePushButton)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShadow(QFrame.Plain)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        sizePolicy4.setHeightForWidth(self.home_page.sizePolicy().hasHeightForWidth())
        self.home_page.setSizePolicy(sizePolicy4)
        self.home_page.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.home_page)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(35)
        self.gridLayout_2.setVerticalSpacing(30)
        self.cyberpunk_2077_download = QPushButton(self.home_page)
        self.cyberpunk_2077_download.setObjectName(u"cyberpunk_2077_download")
        sizePolicy4.setHeightForWidth(self.cyberpunk_2077_download.sizePolicy().hasHeightForWidth())
        self.cyberpunk_2077_download.setSizePolicy(sizePolicy4)
        self.cyberpunk_2077_download.setMaximumSize(QSize(200, 300))
        self.cyberpunk_2077_download.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(12, 100, 203);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/games/images/games/cyberpunk", QSize(), QIcon.Normal, QIcon.Off)
        self.cyberpunk_2077_download.setIcon(icon3)
        self.cyberpunk_2077_download.setIconSize(QSize(200, 295))

        self.gridLayout_2.addWidget(self.cyberpunk_2077_download, 0, 1, 1, 1)

        self.red_dead_redemption_2_download = QPushButton(self.home_page)
        self.red_dead_redemption_2_download.setObjectName(u"red_dead_redemption_2_download")
        sizePolicy4.setHeightForWidth(self.red_dead_redemption_2_download.sizePolicy().hasHeightForWidth())
        self.red_dead_redemption_2_download.setSizePolicy(sizePolicy4)
        self.red_dead_redemption_2_download.setMaximumSize(QSize(200, 300))
        self.red_dead_redemption_2_download.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(12, 100, 203);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/games/images/games/rdr2", QSize(), QIcon.Normal, QIcon.Off)
        self.red_dead_redemption_2_download.setIcon(icon4)
        self.red_dead_redemption_2_download.setIconSize(QSize(200, 295))

        self.gridLayout_2.addWidget(self.red_dead_redemption_2_download, 0, 2, 1, 1)

        self.assassins_creed_valhalla_download = QPushButton(self.home_page)
        self.assassins_creed_valhalla_download.setObjectName(u"assassins_creed_valhalla_download")
        sizePolicy4.setHeightForWidth(self.assassins_creed_valhalla_download.sizePolicy().hasHeightForWidth())
        self.assassins_creed_valhalla_download.setSizePolicy(sizePolicy4)
        self.assassins_creed_valhalla_download.setMaximumSize(QSize(200, 300))
        self.assassins_creed_valhalla_download.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(12, 100, 203);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/games/images/games/valhalla", QSize(), QIcon.Normal, QIcon.Off)
        self.assassins_creed_valhalla_download.setIcon(icon5)
        self.assassins_creed_valhalla_download.setIconSize(QSize(200, 295))

        self.gridLayout_2.addWidget(self.assassins_creed_valhalla_download, 1, 0, 1, 1)

        self.the_medium_download = QPushButton(self.home_page)
        self.the_medium_download.setObjectName(u"the_medium_download")
        sizePolicy4.setHeightForWidth(self.the_medium_download.sizePolicy().hasHeightForWidth())
        self.the_medium_download.setSizePolicy(sizePolicy4)
        self.the_medium_download.setMaximumSize(QSize(200, 300))
        self.the_medium_download.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(12, 100, 203);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/games/images/games/medium", QSize(), QIcon.Normal, QIcon.Off)
        self.the_medium_download.setIcon(icon6)
        self.the_medium_download.setIconSize(QSize(200, 295))

        self.gridLayout_2.addWidget(self.the_medium_download, 1, 4, 1, 1)

        self.pushButton_5 = QPushButton(self.home_page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"border: none;\n"
"font: 16px \"Ubuntu\";")

        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 3)

        self.control_download = QPushButton(self.home_page)
        self.control_download.setObjectName(u"control_download")
        sizePolicy4.setHeightForWidth(self.control_download.sizePolicy().hasHeightForWidth())
        self.control_download.setSizePolicy(sizePolicy4)
        self.control_download.setMaximumSize(QSize(200, 300))
        self.control_download.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(12, 100, 203);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/games/images/games/control", QSize(), QIcon.Normal, QIcon.Off)
        self.control_download.setIcon(icon7)
        self.control_download.setIconSize(QSize(200, 295))

        self.gridLayout_2.addWidget(self.control_download, 0, 4, 1, 1)

        self.detroit_become_human_download = QPushButton(self.home_page)
        self.detroit_become_human_download.setObjectName(u"detroit_become_human_download")
        sizePolicy4.setHeightForWidth(self.detroit_become_human_download.sizePolicy().hasHeightForWidth())
        self.detroit_become_human_download.setSizePolicy(sizePolicy4)
        self.detroit_become_human_download.setMaximumSize(QSize(200, 300))
        self.detroit_become_human_download.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(12, 100, 203);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/games/images/games/detroit", QSize(), QIcon.Normal, QIcon.Off)
        self.detroit_become_human_download.setIcon(icon8)
        self.detroit_become_human_download.setIconSize(QSize(200, 295))

        self.gridLayout_2.addWidget(self.detroit_become_human_download, 0, 0, 1, 1)

        self.forza_horizon_5_download = QPushButton(self.home_page)
        self.forza_horizon_5_download.setObjectName(u"forza_horizon_5_download")
        sizePolicy4.setHeightForWidth(self.forza_horizon_5_download.sizePolicy().hasHeightForWidth())
        self.forza_horizon_5_download.setSizePolicy(sizePolicy4)
        self.forza_horizon_5_download.setMaximumSize(QSize(200, 300))
        self.forza_horizon_5_download.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(12, 100, 203);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/games/images/games/fh5", QSize(), QIcon.Normal, QIcon.Off)
        self.forza_horizon_5_download.setIcon(icon9)
        self.forza_horizon_5_download.setIconSize(QSize(200, 295))

        self.gridLayout_2.addWidget(self.forza_horizon_5_download, 0, 3, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout_2)

        self.stackedWidget.addWidget(self.home_page)
        self.games_page = QWidget()
        self.games_page.setObjectName(u"games_page")
        self.games_page.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat;")
        self.verticalLayout = QVBoxLayout(self.games_page)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.lineEdit = QLineEdit(self.games_page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit)

        self.scrollArea = QScrollArea(self.games_page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"color: rgb(12,117,203);")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setVerticalSpacing(20)

        self.verticalLayout_16.addLayout(self.gridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.stackedWidget.addWidget(self.games_page)
        self.emulators_page = QWidget()
        self.emulators_page.setObjectName(u"emulators_page")
        self.verticalLayout_20 = QVBoxLayout(self.emulators_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.scrollArea_2 = QScrollArea(self.emulators_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QFrame.Plain)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 92, 3018))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 3000))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(30, 490, 821, 41))
        self.label_13.setStyleSheet(u"font: 19px \"Ubuntu\";")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 900, 881, 41))
        self.label_14.setStyleSheet(u"font: 19px \"Ubuntu\";")
        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 1310, 1001, 41))
        self.label_15.setStyleSheet(u"font: 19px \"Ubuntu\";")
        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 1720, 1031, 41))
        self.label_16.setStyleSheet(u"font: 19px \"Ubuntu\";")
        self.progressBar = QProgressBar(self.frame_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(30, 440, 1101, 41))
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.scrollArea_5 = QScrollArea(self.frame_2)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setGeometry(QRect(40, 90, 1091, 331))
        self.scrollArea_5.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 1091, 331))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(25)
        self.gridLayout_5.setVerticalSpacing(20)

        self.verticalLayout_22.addLayout(self.gridLayout_5)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)
        self.label_18 = QLabel(self.frame_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 30, 831, 41))
        self.label_18.setStyleSheet(u"font: 19px \"Ubuntu\";")
        self.scrollArea_4 = QScrollArea(self.frame_2)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setGeometry(QRect(40, 2190, 1101, 321))
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 1101, 321))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(25)
        self.gridLayout_4.setVerticalSpacing(20)

        self.verticalLayout_21.addLayout(self.gridLayout_4)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.scrollArea_6 = QScrollArea(self.frame_2)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setGeometry(QRect(40, 960, 1101, 321))
        self.scrollArea_6.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 1101, 321))
        self.verticalLayout_23 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(25)
        self.gridLayout_7.setVerticalSpacing(20)

        self.verticalLayout_23.addLayout(self.gridLayout_7)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.scrollArea_7 = QScrollArea(self.frame_2)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setGeometry(QRect(40, 1370, 1101, 321))
        self.scrollArea_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 1101, 321))
        self.verticalLayout_24 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(25)
        self.gridLayout_8.setVerticalSpacing(20)

        self.verticalLayout_24.addLayout(self.gridLayout_8)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.scrollArea_8 = QScrollArea(self.frame_2)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setGeometry(QRect(40, 1780, 1101, 321))
        self.scrollArea_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 1101, 321))
        self.verticalLayout_25 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(25)
        self.gridLayout_9.setVerticalSpacing(20)

        self.verticalLayout_25.addLayout(self.gridLayout_9)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.label_19 = QLabel(self.frame_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(30, 2130, 1031, 41))
        self.label_19.setStyleSheet(u"font: 19px \"Ubuntu\";")
        self.scrollArea_9 = QScrollArea(self.frame_2)
        self.scrollArea_9.setObjectName(u"scrollArea_9")
        self.scrollArea_9.setGeometry(QRect(40, 550, 1101, 321))
        self.scrollArea_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollAreaWidgetContents_9 = QWidget()
        self.scrollAreaWidgetContents_9.setObjectName(u"scrollAreaWidgetContents_9")
        self.scrollAreaWidgetContents_9.setGeometry(QRect(0, 0, 1101, 321))
        self.verticalLayout_26 = QVBoxLayout(self.scrollAreaWidgetContents_9)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(25)
        self.gridLayout_10.setVerticalSpacing(20)

        self.verticalLayout_26.addLayout(self.gridLayout_10)

        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.lineEdit_2 = QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(740, 37, 381, 30))
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.lineEdit_3 = QLineEdit(self.frame_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(740, 497, 381, 30))
        self.lineEdit_3.setMinimumSize(QSize(0, 30))
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(740, 907, 381, 30))
        self.lineEdit_4.setMinimumSize(QSize(0, 30))
        self.lineEdit_4.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(740, 1317, 381, 30))
        self.lineEdit_5.setMinimumSize(QSize(0, 30))
        self.lineEdit_5.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(740, 1727, 381, 30))
        self.lineEdit_6.setMinimumSize(QSize(0, 30))
        self.lineEdit_6.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.lineEdit_7 = QLineEdit(self.frame_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(740, 2137, 381, 30))
        self.lineEdit_7.setMinimumSize(QSize(0, 30))
        self.lineEdit_7.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(255, 255, 255, 20);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.listView = QListView(self.frame_2)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(50, 2540, 991, 361))

        self.verticalLayout_14.addWidget(self.frame_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_20.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.emulators_page)
        self.downloads_page = QWidget()
        self.downloads_page.setObjectName(u"downloads_page")
        self.horizontalLayout_7 = QHBoxLayout(self.downloads_page)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_5 = QFrame(self.downloads_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy4)
        self.frame_5.setMinimumSize(QSize(781, 501))
        self.frame_5.setMaximumSize(QSize(781, 501))
        self.frame_5.setLayoutDirection(Qt.LeftToRight)
        self.frame_5.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgba(255, 255, 255, 20);\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.comboBox = QComboBox(self.frame_5)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(210, 30, 371, 41))
        self.comboBox.setMinimumSize(QSize(371, 41))
        self.comboBox.setMaximumSize(QSize(371, 41))
        self.comboBox.setStyleSheet(u"font: 13px \"Ubuntu\";")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 90, 200, 300))
        self.label_3.setMinimumSize(QSize(200, 300))
        self.label_3.setMaximumSize(QSize(200, 300))
        self.label_3.setStyleSheet(u"border-radius: 10px;")
        self.pushButton_3 = QPushButton(self.frame_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(350, 430, 111, 31))
        self.pushButton_3.setMinimumSize(QSize(111, 31))
        self.pushButton_3.setMaximumSize(QSize(111, 31))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font: 12px \"Ubuntu\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.plainTextEdit = QPlainTextEdit(self.frame_5)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(540, 210, 211, 41))
        self.plainTextEdit.setMinimumSize(QSize(211, 41))
        self.plainTextEdit.setMaximumSize(QSize(211, 41))
        self.plainTextEdit.setLayoutDirection(Qt.LeftToRight)
        self.plainTextEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13px \"Ubuntu\";")
        self.plainTextEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.downloads_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.horizontalLayout_8 = QHBoxLayout(self.settings_page)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(25)
        self.gridLayout_3.setVerticalSpacing(20)
        self.widget_5 = QWidget(self.settings_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(591, 251))
        self.widget_5.setMaximumSize(QSize(591, 251))
        self.frame_9 = QFrame(self.widget_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(70, 20, 461, 221))
        self.frame_9.setMinimumSize(QSize(461, 221))
        self.frame_9.setMaximumSize(QSize(461, 221))
        self.frame_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 20);\n"
"border-radius: 10px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.bigpfpLabel = QLabel(self.frame_9)
        self.bigpfpLabel.setObjectName(u"bigpfpLabel")
        self.bigpfpLabel.setGeometry(QRect(40, 60, 81, 81))
        self.bigpfpLabel.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.bigpfpLabel.setScaledContents(True)
        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(270, 140, 271, 31))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"font: 16px \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0)")
        self.label_21.setIndent(5)
        self.pushButton_4 = QPushButton(self.frame_9)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(210, 70, 211, 41))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font: 12px \"Ubuntu\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.settings_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(591, 251))
        self.widget_3.setMaximumSize(QSize(591, 251))
        self.frame_7 = QFrame(self.widget_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(90, 10, 431, 221))
        self.frame_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 20);\n"
"border-radius: 10px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 60, 271, 31))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font: 16px \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0)")
        self.label_6.setIndent(5)
        self.label_8 = QLabel(self.frame_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 90, 391, 31))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"font: 16px \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0)")
        self.label_8.setIndent(5)
        self.label_9 = QLabel(self.frame_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 130, 271, 31))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"font: 16px \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0)")
        self.label_9.setIndent(5)
        self.label_10 = QLabel(self.frame_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 160, 271, 31))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"font: 16px \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0)")
        self.label_10.setIndent(5)
        self.parallel_label_2 = QLabel(self.widget_3)
        self.parallel_label_2.setObjectName(u"parallel_label_2")
        self.parallel_label_2.setGeometry(QRect(30, 20, 201, 41))
        self.parallel_label_2.setFont(font)
        self.parallel_label_2.setStyleSheet(u"font: 15px \"Ubuntu\";\n"
"background-color: rgb(12, 100, 203);\n"
"border-radius: 10px;")
        self.parallel_label_2.setIndent(7)

        self.gridLayout_3.addWidget(self.widget_3, 0, 1, 1, 1)

        self.widget = QWidget(self.settings_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(571, 281))
        self.widget.setMaximumSize(QSize(571, 281))
        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(70, 40, 461, 221))
        self.frame_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 20);\n"
"border-radius: 10px;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.parallel_text = QLineEdit(self.frame_6)
        self.parallel_text.setObjectName(u"parallel_text")
        self.parallel_text.setGeometry(QRect(10, 70, 201, 41))
        self.parallel_text.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 20);")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 130, 271, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font: 16px \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0)")
        self.label_2.setIndent(5)
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 170, 431, 31))
        self.label_4.setStyleSheet(u"font: 16px \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0)")
        self.label_4.setIndent(5)
        self.parallel_label = QLabel(self.widget)
        self.parallel_label.setObjectName(u"parallel_label")
        self.parallel_label.setGeometry(QRect(10, 50, 201, 41))
        self.parallel_label.setFont(font)
        self.parallel_label.setStyleSheet(u"font: 15px \"Ubuntu\";\n"
"background-color: rgb(12, 100, 203);\n"
"border-radius: 10px;")
        self.parallel_label.setIndent(7)

        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)

        self.widget_4 = QWidget(self.settings_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(581, 291))
        self.widget_4.setMaximumSize(QSize(581, 291))
        self.frame_8 = QFrame(self.widget_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(90, 40, 431, 221))
        self.frame_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 20);\n"
"border-radius: 10px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.plainTextEdit_2 = QPlainTextEdit(self.frame_8)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(10, 60, 411, 141))
        self.plainTextEdit_2.setStyleSheet(u"font: 16px \"Ubuntu\";\n"
"background-color: rgba(255, 255, 255, 0);")
        self.plainTextEdit_2.setReadOnly(True)
        self.parallel_label_3 = QLabel(self.widget_4)
        self.parallel_label_3.setObjectName(u"parallel_label_3")
        self.parallel_label_3.setGeometry(QRect(30, 50, 201, 41))
        self.parallel_label_3.setFont(font)
        self.parallel_label_3.setStyleSheet(u"font: 15px \"Ubuntu\";\n"
"background-color: rgb(12, 100, 203);\n"
"border-radius: 10px;")
        self.parallel_label_3.setIndent(7)

        self.gridLayout_3.addWidget(self.widget_4, 1, 1, 1, 1)


        self.horizontalLayout_8.addLayout(self.gridLayout_3)

        self.stackedWidget.addWidget(self.settings_page)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frameo = QFrame(self.page)
        self.frameo.setObjectName(u"frameo")
        self.frameo.setGeometry(QRect(243, 141, 701, 381))
        self.frameo.setMinimumSize(QSize(701, 381))
        self.frameo.setMaximumSize(QSize(701, 381))
        self.frameo.setStyleSheet(u"border-radius: 10px;")
        self.frameo.setFrameShape(QFrame.StyledPanel)
        self.frameo.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(-10, 0, 1191, 671))
        self.frame_10.setStyleSheet(u"background-color: rgba(33, 33, 33, 150);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_10)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(260, 150, 701, 381))
        self.frame.setMinimumSize(QSize(701, 381))
        self.frame.setMaximumSize(QSize(0, 0))
        self.frame.setStyleSheet(u"background: transparent;\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget_2 = QStackedWidget(self.frame)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(0, 0, 701, 381))
        self.stackedWidget_2.setStyleSheet(u"background: transparent;\n"
"border-radius: 10px;")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setStyleSheet(u"background: transparent;\n"
"border-radius: 10px;")
        self.stackedWidget_2.addWidget(self.page_6)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_18 = QVBoxLayout(self.page_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.scrollArea_3 = QScrollArea(self.page_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.NoFrame)
        self.scrollArea_3.setFrameShadow(QFrame.Sunken)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 100, 30))
        self.verticalLayout_19 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(15)
        self.gridLayout_6.setVerticalSpacing(20)

        self.verticalLayout_19.addLayout(self.gridLayout_6)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_18.addWidget(self.scrollArea_3)

        self.stackedWidget.addWidget(self.page_2)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_11 = QLabel(self.page_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 1191, 661))
        self.label_11.setScaledContents(True)
        self.frame_3 = QFrame(self.page_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-10, 0, 1191, 671))
        self.frame_3.setStyleSheet(u"background-color: rgba(33, 33, 33, 150);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 90, 177, 265))
        self.label.setStyleSheet(u"border: 0px;\n"
"background-color: rgba(33, 33, 33, 0);")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 75, 781, 51))
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(33, 33, 33, 0);\n"
"font: 25px \"Ubuntu\";")
        self.textEdit_2 = QTextEdit(self.frame_3)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(320, 155, 781, 131))
        self.textEdit_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(33, 33, 33, 0);")
        self.textEdit_2.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textEdit_2.setReadOnly(True)
        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(80, 450, 301, 161))
        self.pushButton_6.setStyleSheet(u"border: none;\n"
"background-color: rgb(0, 0, 0);")
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 380, 251, 61))
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(33, 33, 33, 0);\n"
"font: 20px \"Ubuntu\";")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(450, 380, 251, 61))
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(33, 33, 33, 0);\n"
"font: 20px \"Ubuntu\";")
        self.label_17 = QLabel(self.frame_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(450, 450, 301, 161))
        self.label_17.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgba(33, 33, 33, 0);")
        self.label_17.setScaledContents(True)
        self.label_20 = QLabel(self.frame_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(790, 450, 301, 161))
        self.label_20.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgba(33, 33, 33, 0);")
        self.label_20.setScaledContents(True)
        self.textEdit_3 = QTextEdit(self.frame_3)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(320, 125, 781, 41))
        self.textEdit_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(33, 33, 33, 0);")
        self.textEdit_3.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textEdit_3.setReadOnly(True)
        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(940, 315, 161, 41))
        self.pushButton_7.setMinimumSize(QSize(111, 31))
        self.pushButton_7.setMaximumSize(QSize(9999, 9999))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font: 12px \"Ubuntu\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.label_22 = QLabel(self.frame_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(320, 310, 51, 51))
        self.label_22.setScaledContents(True)
        self.textEdit_4 = QTextEdit(self.frame_3)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(380, 304, 531, 71))
        self.textEdit_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(33, 33, 33, 0);")
        self.textEdit_4.setLineWrapMode(QTextEdit.WidgetWidth)
        self.textEdit_4.setReadOnly(True)
        self.frame333 = QFrame(self.frame_3)
        self.frame333.setObjectName(u"frame333")
        self.frame333.setGeometry(QRect(260, 140, 701, 381))
        self.frame333.setMinimumSize(QSize(701, 381))
        self.frame333.setMaximumSize(QSize(0, 0))
        self.frame333.setStyleSheet(u"background: transparent;\n"
"border-radius: 10px;")
        self.frame333.setFrameShape(QFrame.StyledPanel)
        self.frame333.setFrameShadow(QFrame.Raised)
        self.stackedWidget_29 = QStackedWidget(self.frame333)
        self.stackedWidget_29.setObjectName(u"stackedWidget_29")
        self.stackedWidget_29.setGeometry(QRect(0, 0, 701, 381))
        self.stackedWidget_29.setStyleSheet(u"background: transparent;\n"
"border-radius: 10px;")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"background: transparent;\n"
"border-radius: 10px;")
        self.stackedWidget_29.addWidget(self.page_3)
        self.pushButton_8 = QPushButton(self.frame_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(770, 315, 161, 41))
        self.pushButton_8.setMinimumSize(QSize(111, 31))
        self.pushButton_8.setMaximumSize(QSize(9999, 9999))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font: 12px \"Ubuntu\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_9 = QPushButton(self.frame_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(940, 315, 161, 41))
        self.pushButton_9.setMinimumSize(QSize(111, 31))
        self.pushButton_9.setMaximumSize(QSize(9999, 9999))
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(12, 100, 203);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font: 12px \"Ubuntu\";\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(12, 117, 225);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(12, 117, 203);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.pushButton_10 = QPushButton(self.frame_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(30, 10, 41, 41))
        self.pushButton_10.setStyleSheet(u"border: none;\n"
"background-color: rgba(0, 0, 0, 50);")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.frame_4 = QFrame(self.page_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 1181, 661))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"border-radius: 10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_23 = QLabel(self.frame_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(380, 160, 400, 300))
        self.stackedWidget.addWidget(self.page_5)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        self.creditsLabel.setFont(font)
        self.creditsLabel.setStyleSheet(u"font: 10px \"Ubuntu\";")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setStyleSheet(u"font: 10px \"Ubuntu\";")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.verticalLayout_17.addWidget(self.bgApp)

        CBLauncher.setCentralWidget(self.styleSheet)

        self.retranslateUi(CBLauncher)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CBLauncher)
    # setupUi

    def retranslateUi(self, CBLauncher):
        CBLauncher.setWindowTitle(QCoreApplication.translate("CBLauncher", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("CBLauncher", u"CB Launcher", None))
        self.titleLeftDescription.setText("")
        self.smallpfpLabel.setText("")
        self.toggleButton.setText(QCoreApplication.translate("CBLauncher", u"Menu", None))
        self.homePushButton.setText(QCoreApplication.translate("CBLauncher", u"Home", None))
        self.gamesPushButton.setText(QCoreApplication.translate("CBLauncher", u"Games", None))
        self.pushButton_2.setText(QCoreApplication.translate("CBLauncher", u"Downloads", None))
        self.emulatorsPushButton.setText(QCoreApplication.translate("CBLauncher", u"Emulators", None))
        self.downloadsPushButton.setText(QCoreApplication.translate("CBLauncher", u"Save Game", None))
        self.rclonePushButton.setText(QCoreApplication.translate("CBLauncher", u"Downloader", None))
        self.settings.setText(QCoreApplication.translate("CBLauncher", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("CBLauncher", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("CBLauncher", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("CBLauncher", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("CBLauncher", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("CBLauncher", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("CBLauncher", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:13px; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0"
                        "px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margi"
                        "n-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText(QCoreApplication.translate("CBLauncher", u"ilovecotton", None))
        self.pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.minimizePushButton.setToolTip(QCoreApplication.translate("CBLauncher", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizePushButton.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("CBLauncher", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closePushButton.setToolTip(QCoreApplication.translate("CBLauncher", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closePushButton.setText("")
        self.cyberpunk_2077_download.setText("")
        self.red_dead_redemption_2_download.setText("")
        self.assassins_creed_valhalla_download.setText("")
        self.the_medium_download.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("CBLauncher", u"Launcher developed by ilovecotton and Port007\n"
"\n"
"Major contributions by D\u0169ng Ch\u01a1i Mai K\u1eb7c, Armaan, issa, X) and Aech\n"
"\n"
"Thanks to Ezio, Cloud and Harry for their contributions", None))
        self.control_download.setText("")
        self.detroit_become_human_download.setText("")
        self.forza_horizon_5_download.setText("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("CBLauncher", u"Search ", None))
        self.label_13.setText(QCoreApplication.translate("CBLauncher", u"PS3", None))
        self.label_14.setText(QCoreApplication.translate("CBLauncher", u"Switch", None))
        self.label_15.setText(QCoreApplication.translate("CBLauncher", u"Gamecube", None))
        self.label_16.setText(QCoreApplication.translate("CBLauncher", u"Wii", None))
        self.label_18.setText(QCoreApplication.translate("CBLauncher", u"Apps", None))
        self.label_19.setText(QCoreApplication.translate("CBLauncher", u"PS2", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("CBLauncher", u"Search ", None))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("CBLauncher", u"Search ", None))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("CBLauncher", u"Search ", None))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("CBLauncher", u"Search ", None))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("CBLauncher", u"Search ", None))
        self.lineEdit_7.setText("")
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("CBLauncher", u"Search ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("CBLauncher", u"Choose game to save", None))

        self.label_3.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("CBLauncher", u"Save Game", None))
        self.bigpfpLabel.setText("")
        self.label_21.setText(QCoreApplication.translate("CBLauncher", u"discord.gg/kT5rvmvA9a", None))
        self.pushButton_4.setText(QCoreApplication.translate("CBLauncher", u"Edit", None))
        self.label_6.setText(QCoreApplication.translate("CBLauncher", u"Paypal:", None))
        self.label_8.setText(QCoreApplication.translate("CBLauncher", u"barbaramcnair420@gmail.com", None))
        self.label_9.setText(QCoreApplication.translate("CBLauncher", u"Crypto:", None))
        self.label_10.setText(QCoreApplication.translate("CBLauncher", u"Unavailable", None))
        self.parallel_label_2.setText(QCoreApplication.translate("CBLauncher", u"Donations", None))
        self.parallel_text.setText(QCoreApplication.translate("CBLauncher", u"20", None))
        self.label_2.setText(QCoreApplication.translate("CBLauncher", u"Recommended value is 20", None))
        self.label_4.setText(QCoreApplication.translate("CBLauncher", u"*Can go higher if you know what you're doing*", None))
        self.parallel_label.setText(QCoreApplication.translate("CBLauncher", u"Parallel Transfers", None))
        self.plainTextEdit_2.setPlainText("")
        self.parallel_label_3.setText(QCoreApplication.translate("CBLauncher", u"Changelog", None))
        self.label_11.setText("")
        self.label.setText("")
        self.label_5.setText("")
        self.textEdit_2.setHtml(QCoreApplication.translate("CBLauncher", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:13px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:131073;\"><br /></p></body></html>", None))
        self.pushButton_6.setText("")
        self.label_7.setText(QCoreApplication.translate("CBLauncher", u"Trailer", None))
        self.label_12.setText(QCoreApplication.translate("CBLauncher", u"Screenshots", None))
        self.label_17.setText("")
        self.label_20.setText("")
        self.textEdit_3.setHtml(QCoreApplication.translate("CBLauncher", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:13px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:131073;\"><br /></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("CBLauncher", u"Download", None))
        self.label_22.setText("")
        self.textEdit_4.setHtml(QCoreApplication.translate("CBLauncher", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:13px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:131073;\"><br /></p></body></html>", None))
        self.pushButton_8.setText(QCoreApplication.translate("CBLauncher", u"Save Game", None))
        self.pushButton_9.setText(QCoreApplication.translate("CBLauncher", u"Start Game", None))
        self.pushButton_10.setText("")
        self.label_23.setText("")
        self.creditsLabel.setText(QCoreApplication.translate("CBLauncher", u"Special thanks to Cloud and Ezio", None))
        self.version.setText(QCoreApplication.translate("CBLauncher", u"v2.0", None))
    # retranslateUi

