from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_power.clicked.connect(lambda: self.POWER())
        self.pushButton_chdown.clicked.connect(lambda: self.CHDOWN())
        self.pushButton_chup.clicked.connect(lambda: self.CHUP())
        self.pushButton_mute.clicked.connect(lambda: self.MUTE())
        self.pushButton_voldown.clicked.connect(lambda: self.VOLDOWN())
        self.pushButton_volup.clicked.connect(lambda: self.VOLUP())

        self.CHANNEL_LIST = ['images/abc.jpg', 'images/cartoonnetwork.jpg', 'images/cnn.jpg', 'images/disney.jpg',
                             'images/fox.jpg', 'images/history.jpg', 'images/nick.jpg', 'images/weatherchannel.jpg',
                             'images/blackstatic.jpg']
        self.MIN_VOLUME = 0
        self.MAX_VOLUME = 50
        self.MIN_CHANNEL = 0
        self.MAX_CHANNEL = len(self.CHANNEL_LIST) - 2
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

        self.UPDATE(8,self.__volume)

    def UPDATE(self, channel, volume):
        self.lcd_volume.display(volume)
        self.lcd_channel.display(channel%8)
        self.label_screen.setPixmap(QtGui.QPixmap(self.CHANNEL_LIST[channel]))
        self.pushButton_chdown.setEnabled(self.__status)
        self.pushButton_chup.setEnabled(self.__status)
        self.pushButton_mute.setEnabled(self.__status)
        self.pushButton_voldown.setEnabled(self.__status)
        self.pushButton_volup.setEnabled(self.__status)

    def POWER(self):
        self.__status = not(self.__status)
        if self.__status:
            self.UPDATE(self.__channel, self.__volume)
        else:
            self.UPDATE(self.MAX_CHANNEL + 1, 0)

    def CHDOWN(self):
        if self.__status and self.__channel > self.MIN_CHANNEL:
            self.__channel -= 1
            self.UPDATE(self.__channel, self.__volume)
        elif self.__status:
            self.__channel = self.MAX_CHANNEL
            self.UPDATE(self.__channel, self.__volume)

    def CHUP(self):
        if self.__status and self.__channel < self.MAX_CHANNEL:
            self.__channel += 1
            self.UPDATE(self.__channel, self.__volume)
        elif self.__status:
            self.__channel = self.MIN_CHANNEL
            self.UPDATE(self.__channel, self.__volume)

    def MUTE(self):
        if self.__status:
            if not self.__muted:
                self.UPDATE(self.__channel, 0)
            elif self.__muted:
                self.UPDATE(self.__channel, self.__volume)
            self.__muted = not(self.__muted)

    def VOLDOWN(self):
        if self.__status and self.__volume > self.MIN_VOLUME:
            self.__muted = False
            self.__volume -= 1
            self.UPDATE(self.__channel, self.__volume)

    def VOLUP(self):
        if self.__status and self.__volume < self.MAX_VOLUME:
            self.__muted = False
            self.__volume += 1
            self.UPDATE(self.__channel, self.__volume)