import constants
import os
from PySide2.QtGui import QPixmap, QPainter
from PySide2.QtWidgets import QSplashScreen

class Setup:

    def create_config_folder(self) -> None:
        if constants.CONFIG_FOLDER_LOCATION.exists() == False:
            os.mkdir(constants.CONFIG_FOLDER_LOCATION)

    def create_settings_file(self) -> bool:
        if constants.SETTINGS_FILE_LOCATION.exists() == False:
            return False
        else:
            return True

class MovieSplashScreen(QSplashScreen):

    def __init__(self, movie, parent=None):
        movie.jumpToFrame(0)
        pixmap = QPixmap(movie.frameRect().size())

        QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)