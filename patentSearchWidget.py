from PySide2 import *
from design.main_interface import *
from design.patentSearch_interface import Ui_Form
from design.patent_interface import Ui_patentItem
from design.selectionTable_dialog import Ui_tableSeletion_dialog
from parsers import *
from sql_queries import *


CustomerObjectRole = QtCore.Qt.UserRole + 1
resultItemWidgets = []


class SelectionTable(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_tableSeletion_dialog()
        self.ui.setupUi(self)

        self.ui.selectTable_box.clear()
        tables = showTables()
        for table in tables:
            self.ui.selectTable_box.addItem(table[0])
        
    def getNameTable(self):
        return self.ui.selectTable_box.currentText()


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


class PatentSearchWidget(QWidget):
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
        resultItemWidgets.clear()

        result = []
        resultGoogle = []
        resultRospatent = []
        resultFips = []
        resultWipo = []
        resultYandex = []

        requestName = self.ui.requestName_textEdit.toPlainText()

        if self.ui.rospatent_checkBox.checkState():
            resultRospatent = parseRospatent(20, requestName)
        if self.ui.google_checkBox.checkState():
            resultGoogle = parseGoogle(20, requestName)
        if self.ui.fips_checkBox.checkState():
            resultFips = parseFips(20, requestName)
        if self.ui.wipo_checkBox.checkState():
            resultWipo = parseWipo(20, requestName)
        if self.ui.yandex_checkBox.checkState():
            resultYandex = parseYandex(20, requestName)
        
        i=0
        numberSources = 5
        while numberSources>0:
            numberSources = 5
            if i<len(resultGoogle):
                result.append(resultGoogle[i])
            else: numberSources-=1

            if i<len(resultRospatent):
                result.append(resultRospatent[i])
            else: numberSources-=1
            
            if i<len(resultFips):
                result.append(resultFips[i])
            else: numberSources-=1

            if i<len(resultWipo):
                result.append(resultWipo[i])
            else: numberSources-=1

            if i<len(resultYandex):
                result.append(resultYandex[i])
            else: numberSources-=1
            
            i+=1
        
        for i in result:
            item = QListWidgetItem(self.ui.listWidget)
            item.setData(CustomerObjectRole, i)
            item.setSizeHint(QSize(100,150))

            resultItemWidgets.append(item)
            
            widget = SearchItemWidget(i.title, i.description, i.link, i.date, i.source, item, self.ui.listWidget)
            self.ui.listWidget.setItemWidget(item, widget)

    
    def savePatents(self):
        dig = SelectionTable()
        if dig.exec():
            for item in resultItemWidgets:
                if item.data(CustomerObjectRole).itemSelected:
                    print(item.data(CustomerObjectRole).title)
                    insertIntoTable(item.data(CustomerObjectRole).title, item.data(CustomerObjectRole).date, item.data(CustomerObjectRole).description,
                                    item.data(CustomerObjectRole).link, item.data(CustomerObjectRole).source, dig.getNameTable())
       

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