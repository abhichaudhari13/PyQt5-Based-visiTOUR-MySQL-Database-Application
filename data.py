from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys,time
import pyodbc
import os
import pandas as pd


class InsertDialog(QDialog):
    def __init__(self):
        super(InsertDialog, self).__init__()

        self.QBtn = QPushButton()   
        self.QBtn.setText("Add")

        self.setWindowTitle("Add Tourist")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.addtourist)

        layout = QVBoxLayout()  
        
        self.uidinput = QLineEdit()
        self.uidinput.setPlaceholderText("Id")
        layout.addWidget(self.uidinput)
        
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)

        self.destinput = QComboBox() 
        self.destinput.addItem("Europe")
        self.destinput.addItem("North-America")
        self.destinput.addItem("Australia")
        self.destinput.addItem("South-America")
        self.destinput.addItem("Asia")
        self.destinput.addItem("Africa")
        layout.addWidget(self.destinput)
        
        
        
        self.costinput=QLineEdit()
        self.costinput.setPlaceholderText("cost")
        layout.addWidget(self.costinput)
        

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Mobile")
        layout.addWidget(self.mobileinput)

        self.emailinput = QLineEdit()
        self.emailinput.setPlaceholderText("Email")
        layout.addWidget(self.emailinput)


        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address")
        layout.addWidget(self.addressinput)
        
        
        layout.addWidget(self.QBtn)
        self.setLayout(layout)



    def addtourist(self):
        uid = -1
        name = ""
        dest=""
        cost=-1
        mobile = -1
        email=""
        address = ""
        
        uid = self.uidinput.text()
        name = self.nameinput.text()
        dest = self.destinput.itemText(self.destinput.currentIndex())
        cost = self.costinput.text()
        mobile = self.mobileinput.text()
        email = self.emailinput.text()
        address = self.addressinput.text()
        
        try:
            self.conn = pyodbc.connect('Driver={MySQL ODBC 8.0 ANSI Driver};'
                                      'Server=127.0.0.1;'
                                      'Uid=root;'
                                      'Pwd=Abhijit@1999;'
                                      'Database=tripdb;'
                                      'Trusted_Connection=yes;')
            self.c = self.conn.cursor()
            self.c.execute("INSERT INTO tour(uid,name,dest,cost,Mobile,email,address) VALUES (?,?,?,?,?,?,?)",(uid,name,dest,cost,mobile,email,address))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Tourist is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not add Tourist to the database.')   





class EditDialog(QDialog):
    def __init__(self):
        super(EditDialog, self).__init__()

        self.QBtn = QPushButton()   
        self.QBtn.setText("Update")

        self.setWindowTitle("Update Tourist")
        self.setFixedWidth(300)
        self.setFixedHeight(250)

        self.QBtn.clicked.connect(self.edittourist)

        layout = QVBoxLayout()  
        
        self.uidinput = QLineEdit()
        self.uidinput.setPlaceholderText("Id to update")
        layout.addWidget(self.uidinput)
        
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)

        self.destinput = QComboBox() 
        self.destinput.addItem("Europe")
        self.destinput.addItem("North-America")
        self.destinput.addItem("Australia")
        self.destinput.addItem("South-America")
        self.destinput.addItem("Asia")
        self.destinput.addItem("Africa")
        layout.addWidget(self.destinput)
        
        
        
        self.costinput=QLineEdit()
        self.costinput.setPlaceholderText("cost")
        layout.addWidget(self.costinput)
        

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Mobile")
        layout.addWidget(self.mobileinput)

        self.emailinput = QLineEdit()
        self.emailinput.setPlaceholderText("Email")
        layout.addWidget(self.emailinput)


        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address")
        layout.addWidget(self.addressinput)
        
        
        layout.addWidget(self.QBtn)
        self.setLayout(layout)



    def edittourist(self):
        euid = -1
        ename = ""
        edest=""
        ecost=-1
        emobile = -1
        eemail=""
        eaddress = ""
        
        euid = self.uidinput.text()
        ename = self.nameinput.text()
        edest = self.destinput.itemText(self.destinput.currentIndex())
        ecost = self.costinput.text()
        emobile = self.mobileinput.text()
        eemail = self.emailinput.text()
        eaddress = self.addressinput.text()
        
        try:
            self.conn = pyodbc.connect('Driver={MySQL ODBC 8.0 ANSI Driver};'
                                      'Server=127.0.0.1;'
                                      'Uid=root;'
                                      'Pwd=Abhijit@1999;'
                                      'Database=tripdb;'
                                      'Trusted_Connection=yes;')
            self.c = self.conn.cursor()
            self.c.execute("UPDATE tour SET name=?,dest=?,cost=?,Mobile=?,email=?,address=? WHERE uid=?",(ename,edest,ecost,emobile,eemail,eaddress,euid))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Tourist is updated successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not update Tourist to the database.')   








class SearchDialog(QDialog):
    def __init__(self):
        super(SearchDialog, self).__init__()

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search Tourist")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchtourist)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Enter Uid")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchtourist(self):

        searchuid = ""
        searchuid = self.searchinput.text()
        try:
            self.conn = pyodbc.connect('Driver={MySQL ODBC 8.0 ANSI Driver};'
                                      'Server=127.0.0.1;'
                                      'Uid=root;'
                                      'Pwd=Abhijit@1999;'
                                      'Database=tripdb;'
                                      'Trusted_Connection=yes;')
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from tour WHERE uid="+str(searchuid))
            row = result.fetchone()
            searchresult = "Uid : "+str(row[0])+'\n'+"Name : "+str(row[1])+'\n'+"Destination : "+str(row[2])+'\n'+"Cost : "+str(row[3])+'\n'+"Phone : "+str(row[4])+'\n'+"Email : "+str(row[5])+'\n'+"Address : "+str(row[6])
            QMessageBox.information(QMessageBox(), 'Successful', searchresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find Tourist from the database.')

class DeleteDialog(QDialog):
    def __init__(self):
        super(DeleteDialog, self).__init__()

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete Tourist")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deleteEvent)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("Enter uid")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)
        
    def deleteEvent(self):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you really want to Delete?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.deletetourist()
        else:
            self.close()

    def deletetourist(self):

        deluid = ""
        deluid = self.deleteinput.text()
      
        try:
            self.conn = pyodbc.connect('Driver={MySQL ODBC 8.0 ANSI Driver};'
                                      'Server=127.0.0.1;'
                                      'Uid=root;'
                                      'Pwd=Abhijit@1999;'
                                      'Database=tripdb;'
                                      'Trusted_Connection=yes;')
            self.c = self.conn.cursor()
            self.c.execute("DELETE from tour WHERE uid="+ deluid)
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Tourist Deleted From database Successful')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete Tourist from the database.')

class LoginDialog(QDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()

        self.setFixedWidth(320)
        self.setFixedHeight(200)

        layout = QVBoxLayout()

        self.passinput = QLineEdit()
        self.passinput.setEchoMode(QLineEdit.Password)
        self.passinput.setPlaceholderText("Enter Password.")
        self.QBtn = QPushButton()
        self.QBtn.setText("Login")
        self.setWindowTitle('Login')
        self.QBtn.clicked.connect(self.login)

        title = QLabel("Login")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        layout.addWidget(title)
        layout.addWidget(self.passinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def login(self):
        if(self.passinput.text() == "12345"):
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Wrong Password')





class AboutDialog(QDialog):
    def __init__(self):
        super(AboutDialog, self).__init__()
        self.setWindowTitle("visiTOUR")
        self.setFixedWidth(400)
        self.setFixedHeight(350)

        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("visiTOUR")
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        labelpic = QLabel()
        pixmap = QPixmap('icon/logo.png')
        pixmap = pixmap.scaledToWidth(100)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(100)

        layout.addWidget(title)
        layout.addWidget(QLabel("Version 1.0.0.1 (Beta)(64 bit)"))
        layout.addWidget(QLabel("Copyright 2019 visiTOUR All Rights reserved"))
        layout.addWidget(labelpic)


        layout.addWidget(self.buttonBox)

        self.setLayout(layout)
        
        
class HelpDialog(QDialog):
    def __init__(self):
        super(HelpDialog, self).__init__()
        self.setWindowTitle("visiTOUR")
        self.setFixedWidth(400)
        self.setFixedHeight(350)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Help")
        title.setAlignment(Qt.AlignCenter)
        font = title.font()
        font.setPointSize(16)
        title.setFont(font)

        labelpic = QLabel()
        labelpic.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap('icon/mid.jpg')
        pixmap = pixmap.scaledToWidth(150)
        labelpic.setPixmap(pixmap)
        labelpic.setFixedHeight(160)

        layout.addWidget(title)
        layout.addWidget(labelpic)
        layout.addWidget(QLabel("Contact the Developer"))
        

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)
     
        
        
        

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        

        self.conn = pyodbc.connect('Driver={MySQL ODBC 8.0 ANSI Driver};'
                                      'Server=127.0.0.1;'
                                      'Uid=root;'
                                      'Pwd=Abhijit@1999;'
                                      'Database=tripdb;'
                                      'Trusted_Connection=yes;')
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS tour(uid BIGINT PRIMARY KEY,name TEXT,dest TEXT,cost INTEGER,mobile INTEGER,email TEXT,address TEXT)")
        self.c.close()
        self.winsplit()
        self.setWindowIcon(QIcon('icon/logo.png'))
        self.setMinimumSize(800, 600)
        
        
        ''' self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.blue)
        self.setPalette(p)'''
        
        
        #file_menu = self.menuBar().addMenu("&File")
        about_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("visiTOUR")
        help_menu = self.menuBar().addMenu("&Help")
        
        
        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
    
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
    
        btn_ac_adduser = QAction(QIcon("icon/add.png"),"Add", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add tourist")
        toolbar.addAction(btn_ac_adduser)
    
        btn_ac_refresh = QAction(QIcon("icon/refresh.png"),"Refresh",self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh")
        toolbar.addAction(btn_ac_refresh)
        
        btn_ac_edit = QAction(QIcon("icon/edit"),"edit", self)
        btn_ac_edit.triggered.connect(self.edit)
        btn_ac_edit.setStatusTip("Edit Tourist")
        toolbar.addAction(btn_ac_edit)
        
        btn_ac_delete = QAction(QIcon("icon/Delete"),"Delete", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Delete Tourist")
        toolbar.addAction(btn_ac_delete)
        
        
        btn_ac_search = QAction(QIcon("icon/search.png"), "Search", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search Tourist")
        
        spacer =QWidget(self)
        spacer.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        toolbar.addWidget(spacer)
        toolbar.addAction(btn_ac_search)
        
        
    
    
    
        #dragdown
    
    
        about_action = QAction("Developer", self)
        about_action.triggered.connect(self.about)
        about_menu.addAction(about_action)
        
        help_action = QAction("Help",self)
        help_action.triggered.connect(self.help_)
        help_menu.addAction(help_action)
          
        
        

    def loaddata(self):
        self.connection = pyodbc.connect('Driver={MySQL ODBC 8.0 ANSI Driver};'
                                      'Server=127.0.0.1;'
                                      'Uid=root;'
                                      'Pwd=Abhijit@1999;'
                                      'Database=tripdb;'
                                      'Trusted_Connection=yes;')
        query = "SELECT * FROM tour"
        result = self.connection.execute(query)

        self.tableWidget.setRowCount(0)
        
        
        
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
                
        self.connection.close()



   
    
    
    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)


    def winsplit(self):      
        i=0
        left_frame = QFrame()
        left_frame.setFrameShape(QFrame.StyledPanel)
        left_frame.setMinimumWidth(200)
        left_frame.setMaximumWidth(200)
        left_frame_lay = QFormLayout()
        f_label = QLabel('Navigation Pane')
        left_frame_lay.addRow(f_label)
        left_frame.setLayout(left_frame_lay)


        right_frame = QFrame()
        right_frame.setFrameShape(QFrame.StyledPanel)
        right_box = QVBoxLayout()
        
        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(("U_Id", "Name", "Destination", "Cost", "Mobile","Email","Address"))
        right_box.addWidget(self.tableWidget)
        right_frame.setLayout(right_box)
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_frame)
        splitter.addWidget(right_frame)
        
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(splitter)
        self.setCentralWidget(splitter)
        
    
    


    def insert(self):
        dlg = InsertDialog()
        dlg.exec()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec()

    def search(self):
        dlg = SearchDialog()
        dlg.exec()

    def about(self):
        dlg = AboutDialog()
        dlg.exec()
    def help_(self):
        dlg = HelpDialog()
        dlg.exec()
    def edit(self):
        dlg = EditDialog()
        dlg.exec()
        
        
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()      


app = QApplication(sys.argv)

window = MainWindow()
window.show()
window.loaddata()
sys.exit(app.exec())