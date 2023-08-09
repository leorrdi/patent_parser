# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import design.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(854, 519)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(24,24,36);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_container = QFrame(self.centralwidget)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        self.slide_menu_container.setMinimumSize(QSize(0, 0))
        self.slide_menu_container.setMaximumSize(QSize(0, 16777215))
        self.slide_menu_container.setStyleSheet(u"background-color:rgb(9,5,13);")
        self.slide_menu_container.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.slide_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(198, 0))
        self.slide_menu.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(24,24,36);\n"
"	border-radius:5px;\n"
"}")
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.frame_3 = QFrame(self.slide_menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/icons/chrome.svg"))

        self.horizontalLayout_5.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_4 = QFrame(self.slide_menu)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 20, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.search_widget_button = QPushButton(self.frame_6)
        self.search_widget_button.setObjectName(u"search_widget_button")
        self.search_widget_button.setMinimumSize(QSize(0, 32))
        icon = QIcon()
        icon.addFile(u":/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.search_widget_button.setIcon(icon)

        self.verticalLayout_5.addWidget(self.search_widget_button)

        self.database_widget_button_2 = QPushButton(self.frame_6)
        self.database_widget_button_2.setObjectName(u"database_widget_button_2")
        self.database_widget_button_2.setMinimumSize(QSize(0, 32))
        icon1 = QIcon()
        icon1.addFile(u":/icons/database.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.database_widget_button_2.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.database_widget_button_2)

        self.settings_widget_button = QPushButton(self.frame_6)
        self.settings_widget_button.setObjectName(u"settings_widget_button")
        self.settings_widget_button.setMinimumSize(QSize(0, 32))
        icon2 = QIcon()
        icon2.addFile(u":/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_widget_button.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.settings_widget_button)


        self.verticalLayout_4.addWidget(self.frame_6, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.slide_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.exit_button = QPushButton(self.frame_5)
        self.exit_button.setObjectName(u"exit_button")
        font1 = QFont()
        font1.setPointSize(9)
        self.exit_button.setFont(font1)
        self.exit_button.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/icons/log-out (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_button.setIcon(icon3)
        self.exit_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.exit_button)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.slide_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color:rgb(9,5,13);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu_button = QPushButton(self.frame_2)
        self.menu_button.setObjectName(u"menu_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.menu_button.sizePolicy().hasHeightForWidth())
        self.menu_button.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon4)
        self.menu_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.menu_button, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.searchPatent_page = QWidget()
        self.searchPatent_page.setObjectName(u"searchPatent_page")
        self.stackedWidget.addWidget(self.searchPatent_page)
        self.database_page = QWidget()
        self.database_page.setObjectName(u"database_page")
        self.stackedWidget.addWidget(self.database_page)

        self.verticalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.main_body_contents)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0410\u0420\u0421\u0415\u0420\n"
"\u041f\u0410\u0422\u0415\u041d\u0422\u041e\u0412", None))
        self.label_3.setText("")
        self.search_widget_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u0438\u043a", None))
        self.database_widget_button_2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.settings_widget_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.exit_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.menu_button.setText("")
    # retranslateUi

