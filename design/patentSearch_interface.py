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
        Form.resize(781, 525)
        Form.setStyleSheet(u"*{\n"
"	background-color:rgb(25,26,31);\n"
"}\n"
"QPlainTextEdit{\n"
"	border-radius: 10px;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 5px;\n"
"}\n"
"QListWidget{\n"
"	background-color:rgb(24,24,36);\n"
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
        self.requestName_textEdit.setAutoFillBackground(False)

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
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(21,23,25);\n"
"}")
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
        self.listWidget = QListWidget(self.frame_3)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
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
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u0435 \u0432\u0441\u0435", None))
        self.savePatent_button.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

