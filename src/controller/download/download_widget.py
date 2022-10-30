import psutil
import pickle
from PySide2.QtWidgets import QWidget, QGraphicsDropShadowEffect, QFileDialog, QPushButton
from view.download_window import Download_Widget
from PySide2.QtGui import QIcon, QColor, QCursor, QPixmap
from PySide2.QtCore import Qt, QCoreApplication, QProcess, QTimer, QSize
from PySide2 import QtCore
from controller.download import helpers
import os
import win32com.client
from controller.download import constants

class DownloadWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Download_Widget()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.frame.setGraphicsEffect(self.shadow)

        self.ui.loadsave.setVisible(False)
        self.ui.nosave.setVisible(False)
        self.ui.download_progress_2.setVisible(False)
        self.ui.pushButton.setVisible(False)
        self.ui.minimizeAppBtn_2.setVisible(False)
        self.ui.minimizeAppBtn_3.setVisible(False)
        self.ui.minimizeAppBtn_4.setVisible(False)

        icon = QIcon(':/icons/images/icons/cil-media-pause')
        self.ui.close_download_5.setIcon(icon)

        self.rclone_process = QProcess()
        self.rclone_process.finished.connect(self.finish_download)
        self.rclone_process.readyReadStandardOutput.connect(self.handle_stdout)

        self.ui.minimizeAppBtn_4.clicked.connect(lambda: self.showMinimized())
        self.ui.minimizeAppBtn_2.clicked.connect(lambda: self.showMinimized())
        self.ui.minimizeAppBtn_3.clicked.connect(lambda: self.showMinimized())

        self.ui.filedialog.clicked.connect(self.findlocation)
        self.ui.start.clicked.connect(self.download_game)
        self.ui.download_location.textChanged.connect(self.disk_free)
        self.ui.close_download_5.clicked.connect(self.pause_or_resume)
        #self.ui.close_download_2.clicked.connect(self.shutit)
        #self.ui.close_download_3.clicked.connect(self.shutit)
        #self.ui.close_download_4.clicked.connect(self.shutit)

    def display_free_space(self):
        free_space = psutil.disk_usage("C:").free
        free_space_converted = helpers.convert_size(free_space)
        self.ui.available_space.setText(f'Available Disk Space: {free_space_converted}')

    def place_game_details(self, game_name, game_size, game_download, exepath):
        self.game_name = game_name
        self.game_download = game_download
        self.exepath = exepath
        self.ui.game_name.setText(QCoreApplication.translate("Form", u"{}".format(game_name), None))
        self.ui.label_2.setText(game_size)

    def findlocation(self):
        filelocation = QFileDialog.getExistingDirectory()
        self.ui.download_location.setText(filelocation)

    def disk_free(self, text):
        try:
            file_location = text[0:2]
            free_space = psutil.disk_usage(file_location).free
            free_space_converted = helpers.convert_size(free_space)

            self.ui.available_space.setText(f'Available Disk Space: {free_space_converted}')
        except:
            self.ui.available_space.setText('Unknown')

    def verify_download_location(self):
        download_location = self.ui.download_location.text()
        if download_location.endswith("\\"):
            self.ui.label_8.setText('Remove backslash from the end to continue')
        elif download_location.isalpha == False:
            self.ui.label_8.setText('Input download location')
        else:
            return True

    def download_progress(self):
        with open('config/progress.txt', 'w') as progress_file:
            progress_file.write('1') 

    def download_game(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_6)
        self.download_progress()
        try:
            download_location = self.ui.download_location.text()
            self.rclone_process.start(f'CBDownloader copy -P --stats-one-line --fast-list --transfers=20 "{self.game_download}" "{download_location}\\{self.game_name}"')
            self.rcloneprocess_id = self.rclone_process.pid()
            self.counter = 0
        except:
            pass

    def update_download_details(self, percentage, transferred, speed, eta):
        self.ui.download_progress.setValue(int(percentage[0:percentage.index('%')]))
        self.ui.ETA_2.setText(transferred)
        self.ui.label_3.setText(speed)
        self.ui.ETA.setText(eta)

    def handle_stdout(self):
        try:
            data = self.rclone_process.readAllStandardOutput()
            stdout = bytes(data).decode("utf8")
            stats = stdout.split(',')
            transferred = stats[0]
            percentage = stats[1]
            speed = stats[2]
            eta = stats[3]
            slash = transferred.index('/')
            before = transferred[:slash - 1]
            after = transferred[slash + 2:]
            self.update_download_details(percentage, transferred, speed, eta)
            if before == after and int(percentage[0:percentage.index('%')]) == 100:
                QTimer.singleShot(3000, self.end_rcloneprocess)
                self.ui.close_download_5.setVisible(False)
                self.download_finished()
        except:
            pass

    def pause_or_resume(self):
        process = psutil.Process(self.rcloneprocess_id)
        if self.counter == 0:
            process.suspend()
            icon = QIcon(':/icons/images/icons/cil-media-play')
            self.ui.close_download_5.setIcon(icon)
            self.ui.status.setText("Paused")
            self.counter += 1
        elif self.counter == 1:
            process.resume()
            icon = QIcon(':/icons/images/icons/cil-media-pause')
            self.ui.close_download_5.setIcon(icon)
            self.ui.status.setText("Downloading...")
            self.counter -= 1

    def finish_download(self):
        self.ui.close_download_5.setVisible(False)
        self.download_finished()

    def download_finished(self):
        try:
            os.remove('config\\progress.txt')
        except:
            pass
        self.ui.status.setText("Finalizing...")
        self.desktopshortcut()
        self.startmenushortcut()
        self.ui.status.setText("Downloaded")
        self.ui.pushButton.setVisible(True)
        self.ui.label_2.setText(" ")
        self.ui.ETA.setText(" ")
        self.ui.ETA_2.setText(" ")

    def desktopshortcut(self):
        if self.ui.create_shortcut.isChecked():
            try:
                desktop = constants.DESKTOP_LOCATION
                download_location = self.ui.download_location.text()
                path = os.path.join(desktop, f"{self.game_name}.lnk")
                target = f"{download_location}\\{self.game_name}{self.exepath}"
                wDir = f"{download_location}\\{self.game_name}"
                icon = f"{download_location}\\{self.game_name}{self.exepath}"

                shell = win32com.client.Dispatch('WScript.Shell')
                shortcut = shell.CreateShortcut(path)
                shortcut.Targetpath = target
                shortcut.WorkingDirectory = wDir
                shortcut.IconLocation = icon
                shortcut.save()
            except:
                pass

    def startmenushortcut(self):
        if self.ui.create_shortcut_2.isChecked():
            try:
                start_menu = constants.START_MENU_LOCATION
                download_location = self.ui.download_location.text()
                path = os.path.join(start_menu, f"{self.game_name}.lnk")
                target = f"{download_location}\\{self.game_name}{self.exepath}"
                wDir = f"{download_location}\\{self.game_name}"
                icon = f"{download_location}\\{self.game_name}{self.exepath}"

                shell = win32com.client.Dispatch('WScript.Shell')
                shortcut = shell.CreateShortcut(path)
                shortcut.Targetpath = target
                shortcut.WorkingDirectory = wDir
                shortcut.IconLocation = icon
                shortcut.save()
            except:
                pass

    def end_rcloneprocess(self):
        self.rclone_process.kill()