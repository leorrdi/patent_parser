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


class Ui_patentItem(object):
    def setupUi(self, patentItem):
        if not patentItem.objectName():
            patentItem.setObjectName(u"patentItem")
        patentItem.resize(989, 293)
        self.horizontalLayout = QHBoxLayout(patentItem)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(patentItem)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color:rgb(20,20,27);\n"
"border-radius:10px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 2, 10, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.patentName_label = QLabel(self.frame_2)
        self.patentName_label.setObjectName(u"patentName_label")
        self.patentName_label.setMinimumSize(QSize(0, 0))
        self.patentName_label.setWordWrap(True)
        self.patentName_label.setOpenExternalLinks(True)

        self.verticalLayout.addWidget(self.patentName_label, 0, Qt.AlignTop)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 863, 68))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.patentDescription_label = QLabel(self.scrollAreaWidgetContents_3)
        self.patentDescription_label.setObjectName(u"patentDescription_label")
        sizePolicy.setHeightForWidth(self.patentDescription_label.sizePolicy().hasHeightForWidth())
        self.patentDescription_label.setSizePolicy(sizePolicy)
        self.patentDescription_label.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.patentDescription_label, 0, Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout.addWidget(self.scrollArea)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(100, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.patentSource_label = QLabel(self.frame_3)
        self.patentSource_label.setObjectName(u"patentSource_label")

        self.verticalLayout_2.addWidget(self.patentSource_label, 0, Qt.AlignTop)

        self.patentDate_label = QLabel(self.frame_3)
        self.patentDate_label.setObjectName(u"patentDate_label")
        sizePolicy1.setHeightForWidth(self.patentDate_label.sizePolicy().hasHeightForWidth())
        self.patentDate_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.patentDate_label, 0, Qt.AlignTop)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(patentItem)

        QMetaObject.connectSlotsByName(patentItem)
    # setupUi

    def retranslateUi(self, patentItem):
        patentItem.setWindowTitle(QCoreApplication.translate("patentItem", u"Form", None))
        self.patentName_label.setText(QCoreApplication.translate("patentItem", u"TextLabel", None))
        self.patentDescription_label.setText(QCoreApplication.translate("patentItem", u"TextLabel", None))
        self.patentSource_label.setText(QCoreApplication.translate("patentItem", u"TextLabel", None))
        self.patentDate_label.setText(QCoreApplication.translate("patentItem", u"TextLabel", None))
    # retranslateUi

