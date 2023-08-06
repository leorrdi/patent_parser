# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patent_interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(667, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(16777215, 150))
        font = QFont()
        font.setItalic(False)
        font.setUnderline(False)
        Form.setFont(font)
        Form.setStyleSheet(u"background-color:rgb(25,26,31);\n"
"border-radius:5px;")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        font1 = QFont()
        font1.setItalic(True)
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.frame)
        self.checkBox.setObjectName(u"checkBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy1)
        self.checkBox.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.checkBox.setFont(font2)
        self.checkBox.setIconSize(QSize(16, 16))

        self.verticalLayout_3.addWidget(self.checkBox)


        self.horizontalLayout.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.patentName_label = QLabel(self.frame_2)
        self.patentName_label.setObjectName(u"patentName_label")
        font3 = QFont()
        font3.setBold(False)
        self.patentName_label.setFont(font3)
        self.patentName_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.patentName_label, 0, Qt.AlignTop)

        self.patentDescription_label = QLabel(self.frame_2)
        self.patentDescription_label.setObjectName(u"patentDescription_label")
        self.patentDescription_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.patentDescription_label, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, 0, 0)
        self.patentSource_label = QLabel(self.frame_3)
        self.patentSource_label.setObjectName(u"patentSource_label")

        self.verticalLayout.addWidget(self.patentSource_label, 0, Qt.AlignRight)

        self.patentDate_label = QLabel(self.frame_3)
        self.patentDate_label.setObjectName(u"patentDate_label")

        self.verticalLayout.addWidget(self.patentDate_label, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox.setText("")
        self.patentName_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.patentDescription_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.patentSource_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.patentDate_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

