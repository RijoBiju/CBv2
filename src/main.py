from controller.login.login import LoginGUI
from controller.mainwindow.window import ImageRetriever, MainWindow
from controller.login import helpers as login_helper
from PySide2.QtWidgets import QApplication
from PySide2.QtGui import QMovie, QColor
from PySide2 import QtCore
import time
import sys
import helpers
import base64
import constants
import pickle

checker = helpers.Setup()

def decode_password(password: bytes) -> str:
    return bytes(base64.b64decode(password.decode('utf-8'))).decode('utf-8')

def auto_login(username: str, password: str) -> None:
    if login_helper.login(username, password):
        pass
    else:
        login_window = LoginGUI()
        login_window.show()

def retrieve_login_details() -> None:
    with open(constants.SETTINGS_FILE_LOCATION, 'rb') as settings_file:
        data = pickle.load(settings_file)
    
    username = data[0]
    password = decode_password(data[1])

    auto_login(username, password)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    checker.create_config_folder()
    
    '''movie = QMovie(constants.SPLASHSCREEN_LOCATION)
    splash = helpers.MovieSplashScreen(movie)
    splash.show()
    splash.showMessage("Loading images", QtCore.Qt.AlignmentFlag.AlignBottom, )
    splash.movie.start()
    start = time.time()
    while movie.state() == QMovie.Running and time.time() < start + 17:
        app.processEvents()'''
    main_window = MainWindow()
    main_window.display_pfp()
    main_window.place_game_buttons()
    image_status = ImageRetriever()
    image_status.request_imageurl()
    main_window.show()
    '''if checker.create_settings_file():
        retrieve_login_details()
    else:
        login_window = LoginGUI()
        login_window.show()'''

    sys.exit(app.exec_())