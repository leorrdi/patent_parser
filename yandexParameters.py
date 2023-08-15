from design.yandexParameter_interface import *
from PySide2 import *


class YandexParameters(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_yandexParameter_widget()
        self.ui.setupUi(self)
        
        self.show()