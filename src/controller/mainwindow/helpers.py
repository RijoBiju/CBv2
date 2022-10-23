from pypresence import Presence
from PySide2.QtCore import QRect, Qt, QSize
from PySide2.QtGui import QPixmap, QImage, QPainter, QBrush, QWindow, QCursor
from PySide2.QtWidgets import QPushButton
import time

def discordrpc() -> None:
    try:
        rpc = Presence("840660812724174900")
        rpc.connect()
        rpc.update(state="discord.gg/kT5rvmvA9a", details="Playing CB Launcher", large_image="danewlogoresizedv2", start=time.time())
    except:
        pass

def mask_image(imgdata, imgtype ='png', size = 64):
    image = QImage.fromData(imgdata, imgtype)
  
    image.convertToFormat(QImage.Format_ARGB32)
  
    imgsize = min(image.width(), image.height())
    rect = QRect(
        (image.width() - imgsize) / 2,
        (image.height() - imgsize) / 2,
        imgsize,
        imgsize,
     )
       
    image = image.copy(rect)
  
    out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
    out_img.fill(Qt.transparent)
  
    brush = QBrush(image)
  
    painter = QPainter(out_img)
    painter.setBrush(brush)
  
    painter.setPen(Qt.NoPen)
  
    painter.drawEllipse(0, 0, imgsize, imgsize)
  
    painter.end()
  
    pr = QWindow().devicePixelRatio()
    pm = QPixmap.fromImage(out_img)
    pm.setDevicePixelRatio(pr)
    size *= pr
    pm = pm.scaled(size, size, Qt.KeepAspectRatio, 
                               Qt.SmoothTransformation)
  
    return pm

def create_button(sub='', width=177, height=265, iconw=177, iconh=260, button_name='name',):
    button = QPushButton(sub)
    button.setObjectName(u"{}".format(button_name))
    button.setMinimumSize(QSize(width, height))
    button.setMaximumSize(QSize(width, height))
    button.setIconSize(QSize(iconw, iconh))
    button.setStyleSheet("QPushButton"
    "{"
    "border: 0px;"
    "}"
    "QPushButton::hover"
    "{"
    "background-color: rgb(12, 100, 203);"
    "}")
    button.setCursor(QCursor(Qt.PointingHandCursor))

    return button

def determine_xandyaxis(xaxis, yaxis):
    yaxis += 1
    if yaxis % 6 == 0:
        yaxis = 0
        xaxis += 1
    return xaxis, yaxis