import sys
import os
from PySide2 import *
from design.ui_main_interface import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,92,157,550))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.ui.exit_button.clicked.connect(lambda: self.close())
        self.ui.menu_button.clicked.connect(lambda: self.slideLeftMenu())

        self.show()
    

    def slideLeftMenu(self):
        width = self.ui.slide_menu_container.width()

        if width == 0:
            newWidth = 200
            self.ui.menu_button.setIcon(QtGui.QIcon(u":/icons/arrow-left.svg"))
        else:
            newWidth = 0
            self.ui.menu_button.setIcon(QtGui.QIcon(u":/icons/align-justify.svg"))

        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())