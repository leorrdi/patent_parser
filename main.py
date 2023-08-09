import sys
import os
from PySide2 import *
from design.main_interface import *
from design.patentSearch_interface import Ui_Form
from design.patent_interface import Ui_patentItem
from parsers import *

CustomerObjectRole = QtCore.Qt.UserRole + 1
resultItemWidgets = []

class SearchItemWidget(QWidget):
    def __init__(self, name, description, link, date, source, item, *args, **kwargs):
        QWidget.__init__(self)
        self._item = item
        self.ui = Ui_patentItem()
        self.ui.setupUi(self)

        self.ui.checkBox.stateChanged.connect(self.stateChange)

        urlLink= f"<a href=\"{link}\">{name}</a>"
        self.ui.patentDate_label.setOpenExternalLinks(True)

        self.ui.patentName_label.setText(urlLink)
        self.ui.patentDate_label.setText(date)
        self.ui.patentSource_label.setText(source)
        self.ui.patentDescription_label.setText(description)

    def stateChange(self):
        if self.ui.checkBox.checkState():
            self._item.data(CustomerObjectRole).itemSelected = True
        else: self._item.data(CustomerObjectRole).itemSelected = False


class PatentSearch(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.requestParameters_button.clicked.connect(lambda: self.slideToptMenu())
        self.ui.parsingStart_button.clicked.connect(self.startParsing)
        self.ui.savePatent_button.clicked.connect(self.savePatents)

        self.show()


    def startParsing(self):
        self.ui.listWidget.clear()
        result = []
        resultGoogle = []
        resultRospatent = []

        requestName = self.ui.requestName_textEdit.toPlainText()

        if self.ui.rospatent_checkBox.checkState():
            resultRospatent = parseRospatent(20, requestName)
        if self.ui.google_checkBox.checkState():
            resultGoogle = parseGoogle(20, requestName)
        
        i=0
        numberSources = 2
        while numberSources>0:
            numberSources = 2
            if i<len(resultGoogle):
                result.append(resultGoogle[i])
            else: numberSources-=1

            if i<len(resultRospatent):
                result.append(resultRospatent[i])
            else: numberSources-=1
            i+=1
        
        for i in result:
            item = QListWidgetItem(self.ui.listWidget)
            item.setData(CustomerObjectRole, i)
            item.setSizeHint(QSize(100,150))

            resultItemWidgets.append(item)
            
            widget = SearchItemWidget(i.title, i.descriprion, i.link, i.date, i.source, item, self.ui.listWidget)
            self.ui.listWidget.setItemWidget(item, widget)

    
    def savePatents(self):
        for item in resultItemWidgets:
            if item.data(CustomerObjectRole).itemSelected:
                print(item.data(CustomerObjectRole).title)
                print()
                


    def slideToptMenu(self):
        height = self.ui.slide_menu_container.height()

        if height == 0:
            newHeight = 300
        else:
            newHeight = 0

        self.animation = QPropertyAnimation(self.ui.slide_menu_container, b"maximumHeight")
        self.animation.setDuration(250)
        self.animation.setStartValue(height)
        self.animation.setEndValue(newHeight)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


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
        
        self.ui.stackedWidget.insertWidget(0, PatentSearch())
        self.ui.search_widget_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

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