# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'selectionTable_dialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_tableSeletion_dialog(object):
    def setupUi(self, tableSeletion_dialog):
        if not tableSeletion_dialog.objectName():
            tableSeletion_dialog.setObjectName(u"tableSeletion_dialog")
        tableSeletion_dialog.resize(322, 113)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(tableSeletion_dialog.sizePolicy().hasHeightForWidth())
        tableSeletion_dialog.setSizePolicy(sizePolicy)
        tableSeletion_dialog.setStyleSheet(u"background-color:rgb(24,24,36);\n"
"")
        self.verticalLayout_2 = QVBoxLayout(tableSeletion_dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(tableSeletion_dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.selectTable_box = QComboBox(self.frame)
        self.selectTable_box.setObjectName(u"selectTable_box")

        self.verticalLayout.addWidget(self.selectTable_box)


        self.verticalLayout_2.addWidget(self.frame)

        self.buttonBox = QDialogButtonBox(tableSeletion_dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(tableSeletion_dialog)
        self.buttonBox.accepted.connect(tableSeletion_dialog.accept)
        self.buttonBox.rejected.connect(tableSeletion_dialog.reject)

        QMetaObject.connectSlotsByName(tableSeletion_dialog)
    # setupUi

    def retranslateUi(self, tableSeletion_dialog):
        tableSeletion_dialog.setWindowTitle(QCoreApplication.translate("tableSeletion_dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("tableSeletion_dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
    # retranslateUi

