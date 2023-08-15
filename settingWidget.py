from PySide2 import *
from design.settings_interface import *
from design.selectionTable_dialog import Ui_tableSeletion_dialog
from sql_queries import *
from pymysql import *
import pandas.io.sql as sql 
import xlwt

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


class SettinsWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_settings()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.importToExcel)

        self.show()

    
    def importToExcel(self):
        dig = SelectionTable()
        if dig.exec():
            patents = selectFromTable(dig.getNameTable())
            
            con = connect(user='root', password='2296', host='localhost', database='new_schema')

            nameTable = dig.getNameTable()
            df = sql.read_sql(f""" SELECT * FROM {nameTable} """, con)

            df.to_excel('ds.xlsx')
                
            
            