import getpass
from PySide2.QtWidgets import QMainWindow, QCompleter
from view.main_window import CBLauncher
from PySide2.QtCore import QRect, Slot
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QIcon
import json
from controller.mainwindow import helpers
from controller.mainwindow import constants
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt5.QtCore import QUrl

PC_USER = getpass.getuser()
buttons = []
urls = []
game_names = []
counter = 0
gui_status = None

class ImageRetriever:

    def __init__(self) -> None:
        self.get_image = QNetworkAccessManager()
        self.get_image.finished.connect(self.image_final)

    def request_imageurl(self) -> None:
        gui_status.setText(f"Loading Image: {counter} / {len(buttons) - 1}")
        self.current_button = buttons[counter]
        self.start_image(urls[counter])
    
    @Slot(str)
    def start_image(self, url):
        request = QNetworkRequest(QUrl(url))
        self.get_image.get(request)

    @Slot(QNetworkReply)
    def image_final(self, reply):
        global counter, urls

        try:
            target = reply.attribute(QNetworkRequest.RedirectionTargetAttribute)
            if reply.error():
                print("error: {}".format(reply.errorString()))
                return
            elif target:
                newUrl = reply.url().resolved(target)
                self.start_image(newUrl)
                return

            pixmap = QPixmap()
            pixmap.loadFromData(bytes(reply.readAll()))
            icon = QIcon(pixmap)

            self.current_button.setIcon(icon)
            counter += 1

            if counter >= len(buttons):
                del urls, counter
                for button in buttons:
                    button.setVisible(True)
            else:
                self.request_imageurl()
        except:
            pass

class MainWindow(QMainWindow):
    def __init__(self, username=constants.DEFAULT_USERNAME):
        global gui_status

        QMainWindow.__init__(self)
        self.ui = CBLauncher()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.username = username
        gui_status = self.ui.pushButton_5

        self.ui.lineEdit.textChanged.connect(self.update_display)
        self.ui.gamesPushButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.games_page))
        self.ui.closePushButton.clicked.connect(lambda: self.close())
        self.ui.minimizePushButton.clicked.connect(lambda: self.showMinimized())

        helpers.discordrpc()

    def display_pfp(self) -> None:
        if self.username != constants.DEFAULT_USERNAME:
            if constants.PFP_LOCATION.exists() == True:
                imgdata = open(constants.PFP_LOCATION, 'rb').read()
                pixmap = helpers.mask_image(imgdata)
                self.ui.bigpfpLabel.setPixmap(QPixmap(pixmap))
                self.ui.smallpfpLabel.setPixmap(QPixmap(pixmap))
        else:
            self.ui.smallpfpLabel.setGeometry(QRect(-20, 0, 101, 81))
            self.ui.smallpfpLabel.setPixmap(QPixmap(u":/games/cb"))

    def place_game_buttons(self) -> None:
        with open('games_page.json', encoding='utf8') as gamedata_file:
            games_data = json.load(gamedata_file)
        
        xaxis = 0
        yaxis = 0
        for game in games_data.values():
            if game["type"] == 'normal':
                game_name = game["game_name"]
                button = helpers.create_button(button_name=game_name)
                buttons.append(button)
                urls.append(game["image_url"])
                game_names.append(game_name)
                xaxis, yaxis = helpers.determine_xandyaxis(xaxis, yaxis)
                self.ui.gridLayout.addWidget(button, xaxis, yaxis)
                button.setVisible(False)
    
    def set_completer(self):
        completer = QCompleter(game_names)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.lineEdit.setCompleter(completer)

    def update_display(self, text):
        for button in buttons:
            if text in button.objectName():
                button.setVisible(True)
            else:
                button.setVisible(False)