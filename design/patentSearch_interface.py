# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patentSearch_interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import design.icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(949, 706)
        Form.setStyleSheet(u"QPlainTextEdit{\n"
"	background-color:rgb(9,5,13);\n"
"	border-radius: 15px;\n"
"}\n"
"#parsingStart_button{\n"
"	background-color:rgb(9,5,13);\n"
"}\n"
"#requestName_textEdit{\n"
"	background-color:rgb(9,5,13);\n"
"}\n"
"#frame{\n"
"	background-color:rgb(9,5,13);\n"
"	border-radius: 10px;\n"
"}\n"
"#listWidget{\n"
"	background-color:rgb(24,24,36);\n"
"	border-radius: 5px;\n"
"}\n"
"#savePatent_button{\n"
"	background-color:rgb(9,5,13);\n"
"	border-radius: 5px;\n"
"}\n"
"#slide_menu{\n"
"	background-color:rgb(9,5,13);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 35))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.requestName_textEdit = QPlainTextEdit(self.frame)
        self.requestName_textEdit.setObjectName(u"requestName_textEdit")
        font = QFont()
        font.setPointSize(11)
        self.requestName_textEdit.setFont(font)
        self.requestName_textEdit.setAutoFillBackground(False)
        self.requestName_textEdit.setTextInteractionFlags(Qt.TextEditable|Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.requestName_textEdit)

        self.parsingStart_button = QPushButton(self.frame)
        self.parsingStart_button.setObjectName(u"parsingStart_button")
        self.parsingStart_button.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.parsingStart_button.setIcon(icon)
        self.parsingStart_button.setIconSize(QSize(20, 20))
        self.parsingStart_button.setFlat(True)

        self.horizontalLayout.addWidget(self.parsingStart_button)

        self.requestParameters_button = QPushButton(self.frame)
        self.requestParameters_button.setObjectName(u"requestParameters_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/sliders.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.requestParameters_button.setIcon(icon1)
        self.requestParameters_button.setIconSize(QSize(20, 20))
        self.requestParameters_button.setFlat(True)

        self.horizontalLayout.addWidget(self.requestParameters_button)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(250, 30))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame_2)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)

        self.savePatent_button = QPushButton(self.frame_2)
        self.savePatent_button.setObjectName(u"savePatent_button")
        self.savePatent_button.setMinimumSize(QSize(0, 30))
        self.savePatent_button.setMaximumSize(QSize(16777215, 16777215))
        icon2 = QIcon()
        icon2.addFile(u":/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.savePatent_button.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.savePatent_button)


        self.verticalLayout.addWidget(self.frame_2, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu_container = QFrame(self.frame_3)
        self.slide_menu_container.setObjectName(u"slide_menu_container")
        self.slide_menu_container.setMinimumSize(QSize(0, 0))
        self.slide_menu_container.setMaximumSize(QSize(16777215, 0))
        self.slide_menu_container.setStyleSheet(u"#frame_4{\n"
"	background-color:rgb(9,5,13);\n"
"}\n"
"#frame_5{\n"
"	background-color:rgb(9,5,13);\n"
"}\n"
"QPushButton{\n"
"	border-radius:5px;\n"
"	background-color:rgb(24,24,36);\n"
"}\n"
"QComboBox{\n"
"	border-radius:5px;\n"
"	background-color:rgb(24,24,36);\n"
"}")
        self.slide_menu_container.setFrameShape(QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.slide_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.slide_menu)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 5, 0, 5)
        self.comboBox = QComboBox(self.frame_4)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(150, 25))

        self.verticalLayout_4.addWidget(self.comboBox, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.stackedWidget = QStackedWidget(self.slide_menu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(9,5,13);\n"
"}")
        self.googlePatent_widget = QWidget()
        self.googlePatent_widget.setObjectName(u"googlePatent_widget")
        sizePolicy2.setHeightForWidth(self.googlePatent_widget.sizePolicy().hasHeightForWidth())
        self.googlePatent_widget.setSizePolicy(sizePolicy2)
        self.verticalLayout_8 = QVBoxLayout(self.googlePatent_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_6 = QFrame(self.googlePatent_widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_7.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_7.addWidget(self.pushButton_4)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.googlePatent_widget)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_5 = QPushButton(self.frame_7)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_6.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_7)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_6.addWidget(self.pushButton_6)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.googlePatent_widget)
        self.rospatent_widget = QWidget()
        self.rospatent_widget.setObjectName(u"rospatent_widget")
        sizePolicy2.setHeightForWidth(self.rospatent_widget.sizePolicy().hasHeightForWidth())
        self.rospatent_widget.setSizePolicy(sizePolicy2)
        self.stackedWidget.addWidget(self.rospatent_widget)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.frame_5 = QFrame(self.slide_menu)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setMinimumSize(QSize(0, 40))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 5, 15, 10)
        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy4)
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_5)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy4.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.slide_menu)


        self.verticalLayout_2.addWidget(self.slide_menu_container, 0, Qt.AlignTop)

        self.listWidget = QListWidget(self.frame_3)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy2.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy2)
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        self.listWidget.setFont(font1)
        self.listWidget.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.listWidget)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.parsingStart_button.setText("")
        self.requestParameters_button.setText("")
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u0432\u0441\u0435", None))
        self.savePatent_button.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u0420\u043e\u0441\u043f\u0430\u0442\u0435\u043d\u0442", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Google Patents", None))

        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

