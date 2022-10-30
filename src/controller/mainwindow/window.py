import getpass
from PySide2.QtWidgets import QMainWindow, QCompleter
from view.main_window import CBLauncher
from PySide2.QtCore import QRect, Slot
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap, QIcon, QMovie
import json
from controller.mainwindow import helpers
from controller.mainwindow import constants
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest
from PyQt5.QtCore import QUrl
from controller.download.download_widget import DownloadWindow

PC_USER = getpass.getuser()
buttons = []
urls = []
game_names = []
labels = []
links = []
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
                del urls
                counter = 0
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
        self.ui.pushButton_6.clicked.connect(self.play_trailer)
        self.ui.pushButton_7.clicked.connect(self.set_download_window)

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
                button.clicked.connect(self.prepare_gamepage)
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

    def play_trailer(self):
        pressed_button = self.sender()

        with open('games_page.json', encoding='utf8') as gamedata_file:
            games_data = json.load(gamedata_file)

        trailer_link = games_data[pressed_button.objectName().lower().replace(' ', '_') + '_download']["trailer"]
        helpers.video(trailer_link)

    def prepare_gamepage(self):
        self.pressed_button = self.sender()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
        self.ui.rclonePushButton.setVisible(True)
        self.ui.pushButton_6.setObjectName(self.pressed_button.objectName())
        self.ui.pushButton_7.setObjectName(self.pressed_button.objectName())

        self.loading_screen()

    def loading_screen(self):
        movie = QMovie(constants.MOVIE_LOCATION)
        self.ui.label_23.setMovie(movie)
        movie.start()

        self.downloadedgame_check()

    def downloadedgame_check(self):
        if constants.DOWNLOADED_GAMES_LOCATION.exists() == False:
            self.ui.pushButton_7.setVisible(True)
            self.ui.pushButton_8.setVisible(False)  
            self.ui.pushButton_9.setVisible(False)
        else:
            self.ui.pushButton_7.setVisible(False)
            self.ui.pushButton_8.setVisible(True)
            self.ui.pushButton_9.setVisible(True)

        self.retrieve_image_links()

    def retrieve_image_links(self):
        global labels, links
        with open('games_page.json', encoding='utf8') as gamedata_file:
            games_data = json.load(gamedata_file)

        game_detail = None
        game = games_data[self.pressed_button.objectName().lower().replace(' ', '_') + '_download']
        maturity_rating_link = game["maturity"]

        if '17' in maturity_rating_link:
            maturityrating_image_link = "https://store-images.microsoft.com/image/global.53975.image.32437939-2f27-4e79-8431-5f5866f32908.3dc74b18-4153-423c-b367-bdcfd34ac658"
        elif 'EVERYONE' in maturity_rating_link:
            maturityrating_image_link = "https://store-images.microsoft.com/image/global.23456.image.87f616db-3cfc-4611-b3b8-c57bbb87de71.7e7baf95-3edb-4b7c-a960-75e7537b07c9"
        elif 'TEEN' in maturity_rating_link:
            maturityrating_image_link = "https://store-images.microsoft.com/image/global.17268.image.4cc004ee-a56d-4f11-ae99-67a89379b743.13d51d69-d3ba-4760-8fdf-f996abafa50a"

        game_detail = game
        links = [game["image_url"], game["image_widget"], game["screenshot_1"], game["screenshot_2"], maturityrating_image_link]
        labels = [self.ui.label, self.ui.label_11, self.ui.label_17, self.ui.label_20, self.ui.label_22]

        self.place_game_details(game_detail)

    def place_game_details(self, game_detail):
        self.ui.label.setScaledContents(True)
        self.ui.label.setFixedSize(177, 265)
        self.ui.label_5.setText(game_detail["game_name"])
        self.ui.textEdit_2.setText(game_detail["description"])
        self.ui.textEdit_3.setText(f'{game_detail["developer"]}   �    {game_detail["genre"]}   �    {game_detail["release_date"]}   �    {game_detail["game_size"]}    �    {game_detail["rating"]}')

        self.place_game_images()

    def place_game_images(self):
        self.get_backgroundimage = QNetworkAccessManager()
        self.get_backgroundimage.finished.connect(self.backgroundimage_final)
        self.request_backgroundimage()

    def request_backgroundimage(self) -> None:
        if counter == 5:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
        else:
            self.current_label = labels[counter]
            self.start_backgroundimage(links[counter])        

    def start_backgroundimage(self, url):
        request = QNetworkRequest(QUrl(url))
        self.get_backgroundimage.get(request)

    @Slot(QNetworkReply)
    def backgroundimage_final(self, reply):
        global counter

        try:
            target = reply.attribute(QNetworkRequest.RedirectionTargetAttribute)
            if reply.error():
                print("error: {}".format(reply.errorString()))
                return
            elif target:
                newUrl = reply.url().resolved(target)
                self.start_backgroundimage(newUrl)
                return

            pixmap = QPixmap()
            pixmap.loadFromData(bytes(reply.readAll()))
            
            self.current_label.setPixmap(pixmap)

            if counter == 1:
                self.ui.label_24.setPixmap(pixmap)

            counter += 1
            self.request_backgroundimage()
        except:
            pass

    def adjust_stacked_widget(self):
        try:
            self.stackedwidget_count = self.ui.stackedWidget_2.count()
            if self.stackedwidget_count > 1:
                self.ui.stackedWidget_2.removeWidget(self.stackedwidget_count - 1)
        except:
            pass

    def set_download_window(self):
        download_window = DownloadWindow()
        download_window.display_free_space()
        with open('games_page.json', encoding='utf8') as gamedata_file:
            games_data = json.load(gamedata_file)
        game = games_data[self.pressed_button.objectName().lower().replace(' ', '_') + '_download']
        download_window.place_game_details(game["game_name"], game["game_size"], game["game_download"], game["exepath"])
        self.open_download_window(download_window)

    def open_download_window(self, download_window):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.adjust_stacked_widget()
        self.ui.stackedWidget_2.addWidget(download_window)
        self.ui.stackedWidget_2.setCurrentIndex(self.stackedwidget_count)
