from PySide2 import *
from design.databaseWidget import *
from design.patentDatabase_interface import *
from parsers.Patent import Patent
from sql_queries import *


CustomerObjectRole = QtCore.Qt.UserRole + 1
resultItemWidgets = []
class DatabaseItemWidget(QWidget):
    def __init__(self, name, description, link, date, source, recordingDate, item, *args, **kwargs):
        QWidget.__init__(self)
        self._item = item
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.checkBox.stateChanged.connect(self.stateChange)

        urlLink= f"<a href=\"{link}\">{name}</a>"
        self.ui.patentName_label.setOpenExternalLinks(True)

        self.ui.patentName_label.setText(urlLink)
        self.ui.patentDate_label.setText(date)
        self.ui.patentSource_label.setText(source)
        self.ui.patentDescription_label.setText(description)
        self.ui.patentDateAdded_label.setText(recordingDate)
        

    def stateChange(self):
        if self.ui.checkBox.checkState():
            self._item.data(CustomerObjectRole).itemSelected = True
        else: self._item.data(CustomerObjectRole).itemSelected = False


class DatabaseWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_databaseWidget()
        self.ui.setupUi(self)

        self.ui.tableSelection_comboBox.currentIndexChanged.connect(self.onCurrentIndexChanged)
        self.ui.sourceSelection_comboBox.currentIndexChanged.connect(self.onCurrentIndexChanged)

        self.ui.deleteTable_button.clicked.connect(self.deleteTable)
        self.ui.createTable_button.clicked.connect(self.createTable)
        

        self.show()

    
    def onCurrentIndexChanged(self, index):
        self.ui.listWidget.clear()
        nameTable = self.ui.tableSelection_comboBox.currentText()
        source = self.ui.sourceSelection_comboBox.currentText()

        if source =='Все источники':
            result = selectFromTable(nameTable)
        else: result = SelectFromTableSource(nameTable, source)

        for i in result:
            item = QListWidgetItem(self.ui.listWidget)
            item.setSizeHint(QSize(100,150))
            patent = Patent(i[1], i[4], i[2].strftime("%Y-%m-%d"), i[3], i[5])
            item.setData(CustomerObjectRole, i)
            
            widget = DatabaseItemWidget(patent.title, patent.description, patent.link, patent.date, patent.source, str(i[6]), item, self.ui.listWidget)
            self.ui.listWidget.setItemWidget(item, widget)


    def deleteTable(self):
        nameTable = self.ui.tableSelection_comboBox.currentText()
        deletingTable(nameTable)
        self.ui.tableSelection_comboBox.clear()
        tables = showTables()
        for table in tables:
            self.ui.tableSelection_comboBox.addItem(table[0])


    def createTable(self):
        text, ok = QInputDialog.getText(self, 'Создание таблицы', 'Введите название таблицы')        
        if ok:
            createTable(text)
            self.ui.tableSelection_comboBox.clear()
            tables = showTables()
            for table in tables:
                self.ui.tableSelection_comboBox.addItem(table[0])