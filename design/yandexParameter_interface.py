# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yandexParameter_interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_yandexParameter_widget(object):
    def setupUi(self, yandexParameter_widget):
        if not yandexParameter_widget.objectName():
            yandexParameter_widget.setObjectName(u"yandexParameter_widget")
        yandexParameter_widget.resize(911, 225)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(yandexParameter_widget.sizePolicy().hasHeightForWidth())
        yandexParameter_widget.setSizePolicy(sizePolicy)
        yandexParameter_widget.setMaximumSize(QSize(16777215, 16777215))
        yandexParameter_widget.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(24,24,36);\n"
"}\n"
"QPlainTextEdit{\n"
"	background-color:rgb(9,5,13);\n"
"	border-radius: 5px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(yandexParameter_widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(yandexParameter_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_31 = QFrame(self.frame)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(100, 16777215))
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_31)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.application_checkBox = QCheckBox(self.frame_31)
        self.application_checkBox.setObjectName(u"application_checkBox")

        self.verticalLayout_33.addWidget(self.application_checkBox)

        self.patent_checkBox = QCheckBox(self.frame_31)
        self.patent_checkBox.setObjectName(u"patent_checkBox")

        self.verticalLayout_33.addWidget(self.patent_checkBox)


        self.horizontalLayout_2.addWidget(self.frame_31)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.label)

        self.document_textEdit = QPlainTextEdit(self.frame_5)
        self.document_textEdit.setObjectName(u"document_textEdit")
        self.document_textEdit.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_3.addWidget(self.document_textEdit)


        self.verticalLayout.addWidget(self.frame_5)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_5.addWidget(self.label_2)

        self.application_textEdit = QPlainTextEdit(self.frame_7)
        self.application_textEdit.setObjectName(u"application_textEdit")
        self.application_textEdit.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_5.addWidget(self.application_textEdit)


        self.verticalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_8)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_9)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_9)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)

        self.verticalLayout_31.addWidget(self.label_14)

        self.frame_30 = QFrame(self.frame_9)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setMinimumSize(QSize(0, 0))
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.dateStart_textEdit = QPlainTextEdit(self.frame_30)
        self.dateStart_textEdit.setObjectName(u"dateStart_textEdit")
        self.dateStart_textEdit.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_3.addWidget(self.dateStart_textEdit)

        self.dateEnd_textEdit = QPlainTextEdit(self.frame_30)
        self.dateEnd_textEdit.setObjectName(u"dateEnd_textEdit")
        self.dateEnd_textEdit.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_3.addWidget(self.dateEnd_textEdit)


        self.verticalLayout_31.addWidget(self.frame_30)


        self.verticalLayout_32.addWidget(self.frame_9)


        self.verticalLayout_8.addWidget(self.frame_8)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_16 = QFrame(self.frame_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_16)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_17)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_17)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.verticalLayout_17.addWidget(self.label_7)

        self.namePatent_textEdit = QPlainTextEdit(self.frame_17)
        self.namePatent_textEdit.setObjectName(u"namePatent_textEdit")
        self.namePatent_textEdit.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_17.addWidget(self.namePatent_textEdit)


        self.verticalLayout_16.addWidget(self.frame_17)


        self.verticalLayout_15.addWidget(self.frame_16)

        self.frame_18 = QFrame(self.frame_3)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_18)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_19)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)

        self.verticalLayout_19.addWidget(self.label_8)

        self.authot_textEdit = QPlainTextEdit(self.frame_19)
        self.authot_textEdit.setObjectName(u"authot_textEdit")
        self.authot_textEdit.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_19.addWidget(self.authot_textEdit)


        self.verticalLayout_18.addWidget(self.frame_19)


        self.verticalLayout_15.addWidget(self.frame_18)

        self.frame_20 = QFrame(self.frame_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_20)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_21)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)

        self.verticalLayout_21.addWidget(self.label_9)

        self.patentHolder_textEdit = QPlainTextEdit(self.frame_21)
        self.patentHolder_textEdit.setObjectName(u"patentHolder_textEdit")
        self.patentHolder_textEdit.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_21.addWidget(self.patentHolder_textEdit)


        self.verticalLayout_20.addWidget(self.frame_21)


        self.verticalLayout_15.addWidget(self.frame_20)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(yandexParameter_widget)

        QMetaObject.connectSlotsByName(yandexParameter_widget)
    # setupUi

    def retranslateUi(self, yandexParameter_widget):
        yandexParameter_widget.setWindowTitle(QCoreApplication.translate("yandexParameter_widget", u"Form", None))
        self.application_checkBox.setText(QCoreApplication.translate("yandexParameter_widget", u"\u0417\u0430\u044f\u0432\u043a\u0430", None))
        self.patent_checkBox.setText(QCoreApplication.translate("yandexParameter_widget", u"\u041f\u0430\u0442\u0435\u043d\u0442", None))
        self.label.setText(QCoreApplication.translate("yandexParameter_widget", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.label_2.setText(QCoreApplication.translate("yandexParameter_widget", u"\u0417\u0430\u044f\u0432\u043a\u0430", None))
        self.label_14.setText(QCoreApplication.translate("yandexParameter_widget", u"\u0414\u0430\u0442\u044b", None))
        self.dateStart_textEdit.setPlainText("")
        self.dateStart_textEdit.setPlaceholderText(QCoreApplication.translate("yandexParameter_widget", u"\u0413\u0413\u0413\u0413.\u041c\u041c.\u0414\u0414", None))
        self.dateEnd_textEdit.setPlaceholderText(QCoreApplication.translate("yandexParameter_widget", u"\u0413\u0413\u0413\u0413.\u041c\u041c.\u0414\u0414", None))
        self.label_7.setText(QCoreApplication.translate("yandexParameter_widget", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_8.setText(QCoreApplication.translate("yandexParameter_widget", u"\u0410\u0432\u0442\u043e\u0440\u044b", None))
        self.label_9.setText(QCoreApplication.translate("yandexParameter_widget", u"\u041f\u0430\u0442\u0435\u043d\u0442\u043e\u043e\u0431\u043b\u0430\u0434\u0430\u0442\u0435\u043b\u0438", None))
    # retranslateUi

