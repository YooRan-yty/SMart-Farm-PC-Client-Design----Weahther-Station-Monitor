import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QTableView, QHBoxLayout
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import Qt


class sqlDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('demo')
        self.resize(600, 600)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)


        # 1连接数据库
        self.connect_db()
        # 操作数据库
        self.opreate_db()
        # 在Pyqt界面显示数据库内容 （相当于查询）
        self.show_db()

    def connect_db(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./weather.db')
        self.db.open()

    def opreate_db(self):
        query = QSqlQuery()


    def show_db(self):
        tableview = QTableView()
        self.layout.addWidget(tableview)

        querymodel = QSqlQueryModel()
        querymodel.setQuery("select * from test where(typeid = {})".format(101))
        tableview.setModel(querymodel)


    # 关闭数据库
    def close_db(self):
        self.db.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = sqlDemo()
    demo.show()
    sys.exit(app.exec_())

