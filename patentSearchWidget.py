from PySide2 import *
from design.main_interface import *
from design.patentSearch_interface import Ui_Form
from yandexParameters import YandexParameters
from design.patent_interface import Ui_patentItem
from design.selectionTable_dialog import Ui_tableSeletion_dialog
from parsers import *
from sql_queries import *
from parsers.Patent import Patent

CustomerObjectRole = QtCore.Qt.UserRole + 1


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


        urlLink= f"<a href=\"{link}\">{name}</a>"
        self.ui.patentDate_label.setOpenExternalLinks(True)

        self.ui.patentName_label.setText(urlLink)
        self.ui.patentDate_label.setText(date)
        self.ui.patentSource_label.setText(source)
        self.ui.patentDescription_label.setText(description)



class PatentSearchWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.requestParameters_button.clicked.connect(lambda: self.slideToptMenu())
        self.ui.parsingStart_button.clicked.connect(self.startParsing)
        self.ui.savePatent_button.clicked.connect(self.savePatents)

        self.ui.comboBox.currentTextChanged.connect(self.onCurrentIndexChanged)

        self.ui.stackedWidget.insertWidget(0, YandexParameters())

        self.show()


    def startParsing(self):
        self.ui.listWidget.clear()

        result = []
        resultGoogle = []
        resultRospatent = []
        resultFips = []
        resultWipo = []
        resultYandex = []
        resultKipris = []

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
            widget = self.ui.stackedWidget.widget(0)
            resultYandex = parseYandex(20, requestName, widget.ui.document_textEdit.toPlainText(), widget.ui.application_textEdit.toPlainText(),
                                       widget.ui.namePatent_textEdit.toPlainText(), widget.ui.authot_textEdit.toPlainText(),
                                       widget.ui.patentHolder_textEdit.toPlainText(), widget.ui.dateStart_textEdit.toPlainText(),
                                       widget.ui.dateEnd_textEdit.toPlainText(), widget.ui.application_checkBox.checkState(),
                                       widget.ui.patent_checkBox.checkState()
                                       )
        if self.ui.kipris_checkBox.checkState():
            resultKipris = parseKipris(20, requestName)
        
        i=0
        numberSources = 6
        while numberSources>0:
            numberSources = 6
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

            if i<len(resultKipris):
                result.append(resultKipris[i])
            else: numberSources-=1
            
            i+=1
        
        for i in result:
            patent = Patent(i.title, i.link, i.date, i.description, i.source )

            item = QListWidgetItem(self.ui.listWidget)
            item.setData(CustomerObjectRole, patent)
            item.setSizeHint(QSize(100,150))
            
            widget = SearchItemWidget(patent.title, patent.description, patent.link, patent.date, patent.source, item, self.ui.listWidget)
            self.ui.listWidget.setItemWidget(item, widget)

    
    def savePatents(self):
        dig = SelectionTable()
        if dig.exec():
            for patent in self.ui.listWidget.selectedItems():
                patent = patent.data(CustomerObjectRole)
                insertIntoTable(patent.title, patent.date, patent.description,
                                patent.link, patent.source, dig.getNameTable())


    def onCurrentIndexChanged(self):
        source = self.ui.comboBox.currentText()
        if source == 'Яндекс.Патенты':
            self.ui.stackedWidget.setCurrentIndex(0)


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