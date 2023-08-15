# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'databaseWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import design.icons_rc

class Ui_databaseWidget(object):
    def setupUi(self, databaseWidget):
        if not databaseWidget.objectName():
            databaseWidget.setObjectName(u"databaseWidget")
        databaseWidget.resize(932, 593)
        databaseWidget.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(24,24,36);\n"
"}\n"
"QDateEdit{\n"
"	background-color:rgb(9,5,13);\n"
"}\n"
"#deleteTable_button{\n"
"	background-color:rgb(24,24,36);\n"
"	border-radius: 5px;\n"
"}\n"
"#createTable_button{\n"
"	background-color:rgb(24,24,36);\n"
"	border-radius: 5px;\n"
"}\n"
"QComboBox{\n"
"	background-color:rgb(9,5,13);\n"
"}\n"
"#deletePatents_button{\n"
"	background-color:rgb(9,5,13);\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(databaseWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(databaseWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sourceSelection_comboBox = QComboBox(self.frame_4)
        self.sourceSelection_comboBox.addItem("")
        self.sourceSelection_comboBox.addItem("")
        self.sourceSelection_comboBox.addItem("")
        self.sourceSelection_comboBox.addItem("")
        self.sourceSelection_comboBox.addItem("")
        self.sourceSelection_comboBox.addItem("")
        self.sourceSelection_comboBox.setObjectName(u"sourceSelection_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceSelection_comboBox.sizePolicy().hasHeightForWidth())
        self.sourceSelection_comboBox.setSizePolicy(sizePolicy)
        self.sourceSelection_comboBox.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_2.addWidget(self.sourceSelection_comboBox)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.label)

        self.startDate_date = QDateEdit(self.frame_4)
        self.startDate_date.setObjectName(u"startDate_date")
        self.startDate_date.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.startDate_date)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.finalDate_date = QDateEdit(self.frame_4)
        self.finalDate_date.setObjectName(u"finalDate_date")
        self.finalDate_date.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.finalDate_date)

        self.deletePatents_button = QPushButton(self.frame_4)
        self.deletePatents_button.setObjectName(u"deletePatents_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.deletePatents_button.sizePolicy().hasHeightForWidth())
        self.deletePatents_button.setSizePolicy(sizePolicy2)
        self.deletePatents_button.setMinimumSize(QSize(130, 30))

        self.horizontalLayout_2.addWidget(self.deletePatents_button)


        self.horizontalLayout.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tableSelection_comboBox = QComboBox(self.frame_5)
        self.tableSelection_comboBox.setObjectName(u"tableSelection_comboBox")
        self.tableSelection_comboBox.setMinimumSize(QSize(150, 30))

        self.horizontalLayout_3.addWidget(self.tableSelection_comboBox)

        self.createTable_button = QPushButton(self.frame_5)
        self.createTable_button.setObjectName(u"createTable_button")
        self.createTable_button.setMinimumSize(QSize(0, 30))
        icon = QIcon()
        icon.addFile(u":/icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.createTable_button.setIcon(icon)
        self.createTable_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.createTable_button)

        self.deleteTable_button = QPushButton(self.frame_5)
        self.deleteTable_button.setObjectName(u"deleteTable_button")
        self.deleteTable_button.setMinimumSize(QSize(0, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/trash-2 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteTable_button.setIcon(icon1)
        self.deleteTable_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.deleteTable_button)


        self.horizontalLayout.addWidget(self.frame_5, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.listWidget = QListWidget(self.frame_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        self.listWidget.setSpacing(10)

        self.verticalLayout_3.addWidget(self.listWidget)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(databaseWidget)

        QMetaObject.connectSlotsByName(databaseWidget)
    # setupUi

    def retranslateUi(self, databaseWidget):
        databaseWidget.setWindowTitle(QCoreApplication.translate("databaseWidget", u"Form", None))
        self.sourceSelection_comboBox.setItemText(0, QCoreApplication.translate("databaseWidget", u"\u0412\u0441\u0435 \u0438\u0441\u0442\u043e\u0447\u043d\u0438\u043a\u0438", None))
        self.sourceSelection_comboBox.setItemText(1, QCoreApplication.translate("databaseWidget", u"\u042f\u043d\u0434\u0435\u043a\u0441.\u041f\u0430\u0442\u0435\u043d\u0442\u044b", None))
        self.sourceSelection_comboBox.setItemText(2, QCoreApplication.translate("databaseWidget", u"\u0413\u0443\u0433\u043b \u043f\u0430\u0442\u0435\u043d\u0442\u044b", None))
        self.sourceSelection_comboBox.setItemText(3, QCoreApplication.translate("databaseWidget", u"\u0420\u043e\u0441\u043f\u0430\u0442\u0435\u043d\u0442", None))
        self.sourceSelection_comboBox.setItemText(4, QCoreApplication.translate("databaseWidget", u"\u0424\u0438\u043f\u0441", None))
        self.sourceSelection_comboBox.setItemText(5, QCoreApplication.translate("databaseWidget", u"\u0412\u0438\u043f\u043e", None))

        self.label.setText(QCoreApplication.translate("databaseWidget", u"C", None))
        self.label_2.setText(QCoreApplication.translate("databaseWidget", u"\u041f\u043e", None))
        self.deletePatents_button.setText(QCoreApplication.translate("databaseWidget", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u0430\u0442\u0435\u043d\u0442\u044b", None))
        self.createTable_button.setText("")
        self.deleteTable_button.setText("")
    # retranslateUi

