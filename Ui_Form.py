# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui05.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(558, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 551, 691))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_main = QtWidgets.QWidget()
        self.tab_main.setObjectName("tab_main")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_main)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 470, 441, 171))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_hum = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label_hum.setFont(font)
        self.label_hum.setObjectName("label_hum")
        self.gridLayout.addWidget(self.label_hum, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_wsdata = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label_wsdata.setFont(font)
        self.label_wsdata.setText("")
        self.label_wsdata.setObjectName("label_wsdata")
        self.gridLayout.addWidget(self.label_wsdata, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_raindata = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label_raindata.setFont(font)
        self.label_raindata.setText("")
        self.label_raindata.setObjectName("label_raindata")
        self.gridLayout.addWidget(self.label_raindata, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_ws = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_ws.setFont(font)
        self.label_ws.setObjectName("label_ws")
        self.gridLayout.addWidget(self.label_ws, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_humdata = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label_humdata.setFont(font)
        self.label_humdata.setText("")
        self.label_humdata.setObjectName("label_humdata")
        self.gridLayout.addWidget(self.label_humdata, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_rain = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(24)
        self.label_rain.setFont(font)
        self.label_rain.setObjectName("label_rain")
        self.gridLayout.addWidget(self.label_rain, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_wspix = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_wspix.setText("")
        self.label_wspix.setPixmap(QtGui.QPixmap("../../../Farm/风机.png"))
        self.label_wspix.setObjectName("label_wspix")
        self.gridLayout.addWidget(self.label_wspix, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_rainpix = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_rainpix.setText("")
        self.label_rainpix.setPixmap(QtGui.QPixmap("../../../Farm/极端降雨.png"))
        self.label_rainpix.setObjectName("label_rainpix")
        self.gridLayout.addWidget(self.label_rainpix, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_humpix = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_humpix.setText("")
        self.label_humpix.setPixmap(QtGui.QPixmap("../../../Farm/wenshidu.png"))
        self.label_humpix.setObjectName("label_humpix")
        self.gridLayout.addWidget(self.label_humpix, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_main)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 340, 511, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_warn_rain = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_warn_rain.setObjectName("label_warn_rain")
        self.horizontalLayout.addWidget(self.label_warn_rain, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_warn_wind = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_warn_wind.setObjectName("label_warn_wind")
        self.horizontalLayout.addWidget(self.label_warn_wind, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_warn_temp = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_warn_temp.setObjectName("label_warn_temp")
        self.horizontalLayout.addWidget(self.label_warn_temp, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.line = QtWidgets.QFrame(self.tab_main)
        self.line.setGeometry(QtCore.QRect(-10, 420, 571, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_main)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 19, 531, 284))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_weather = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_weather.setFont(font)
        self.label_weather.setObjectName("label_weather")
        self.verticalLayout.addWidget(self.label_weather, 0, QtCore.Qt.AlignHCenter)
        self.label_tips = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_tips.setObjectName("label_tips")
        self.verticalLayout.addWidget(self.label_tips, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.label_tempdata = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_tempdata.setFont(font)
        self.label_tempdata.setObjectName("label_tempdata")
        self.gridLayout_2.addWidget(self.label_tempdata, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_wdpix = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_wdpix.setText("")
        self.label_wdpix.setPixmap(QtGui.QPixmap("../../../Farm/风向.png"))
        self.label_wdpix.setObjectName("label_wdpix")
        self.gridLayout_2.addWidget(self.label_wdpix, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_wddata = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label_wddata.setFont(font)
        self.label_wddata.setObjectName("label_wddata")
        self.gridLayout_2.addWidget(self.label_wddata, 1, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_wind_direction = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_wind_direction.setFont(font)
        self.label_wind_direction.setObjectName("label_wind_direction")
        self.gridLayout_2.addWidget(self.label_wind_direction, 2, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_pmpix = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_pmpix.setText("")
        self.label_pmpix.setPixmap(QtGui.QPixmap("../../../Farm/a-PM25-2-Outlined.png"))
        self.label_pmpix.setObjectName("label_pmpix")
        self.gridLayout_2.addWidget(self.label_pmpix, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_city = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_city.setFont(font)
        self.label_city.setObjectName("label_city")
        self.gridLayout_2.addWidget(self.label_city, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_pmdata_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setItalic(False)
        self.label_pmdata_2.setFont(font)
        self.label_pmdata_2.setObjectName("label_pmdata_2")
        self.gridLayout_2.addWidget(self.label_pmdata_2, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.tabWidget.addTab(self.tab_main, "")
        self.tab_data_analize = QtWidgets.QWidget()
        self.tab_data_analize.setObjectName("tab_data_analize")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_data_analize)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(0, 10, 541, 651))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_chart = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_chart.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_chart.setObjectName("gridLayout_chart")
        self.v_ws = QtWidgets.QVBoxLayout()
        self.v_ws.setObjectName("v_ws")
        self.gridLayout_chart.addLayout(self.v_ws, 0, 1, 1, 1)
        self.v_rain = QtWidgets.QVBoxLayout()
        self.v_rain.setObjectName("v_rain")
        self.gridLayout_chart.addLayout(self.v_rain, 0, 0, 1, 1)
        self.v_temp = QtWidgets.QVBoxLayout()
        self.v_temp.setObjectName("v_temp")
        self.gridLayout_chart.addLayout(self.v_temp, 1, 0, 1, 1)
        self.v_hum = QtWidgets.QVBoxLayout()
        self.v_hum.setObjectName("v_hum")
        self.gridLayout_chart.addLayout(self.v_hum, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_data_analize, "")
        self.tab_data_json = QtWidgets.QWidget()
        self.tab_data_json.setObjectName("tab_data_json")
        self.textEdit = QtWidgets.QTextEdit(self.tab_data_json)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 531, 631))
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_data_json, "")
        self.tab_data_search = QtWidgets.QWidget()
        self.tab_data_search.setObjectName("tab_data_search")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_data_search)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(110, 510, 331, 141))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.comboBox_seneorName = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_seneorName.setObjectName("comboBox_seneorName")
        self.comboBox_seneorName.addItem("")
        self.comboBox_seneorName.addItem("")
        self.comboBox_seneorName.addItem("")
        self.comboBox_seneorName.addItem("")
        self.comboBox_seneorName.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_seneorName, 1, 0, 1, 1)
        self.comboBox_typeID = QtWidgets.QComboBox(self.gridLayoutWidget_4)
        self.comboBox_typeID.setObjectName("comboBox_typeID")
        self.comboBox_typeID.addItem("")
        self.comboBox_typeID.addItem("")
        self.comboBox_typeID.addItem("")
        self.comboBox_typeID.addItem("")
        self.comboBox_typeID.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_typeID, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget_4)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 1, 2, 1)
        self.tableView = QtWidgets.QTableView(self.tab_data_search)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 531, 481))
        self.tableView.setObjectName("tableView")
        self.tabWidget.addTab(self.tab_data_search, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_hum.setText(_translate("MainWindow", "温湿度"))
        self.label_ws.setText(_translate("MainWindow", "风速"))
        self.label_rain.setText(_translate("MainWindow", "降雨量"))
        self.label_warn_rain.setText(_translate("MainWindow", "暴雨预警"))
        self.label_warn_wind.setText(_translate("MainWindow", "大风预警"))
        self.label_warn_temp.setText(_translate("MainWindow", "温度预警"))
        self.label_weather.setText(_translate("MainWindow", "天气"))
        self.label_tips.setText(_translate("MainWindow", "提示"))
        self.label_tempdata.setText(_translate("MainWindow", "室外温度"))
        self.label_wddata.setText(_translate("MainWindow", "风向"))
        self.label_wind_direction.setText(_translate("MainWindow", "东北风"))
        self.label_city.setText(_translate("MainWindow", "成都市"))
        self.label_pmdata_2.setText(_translate("MainWindow", "pm"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_main), _translate("MainWindow", "主界面"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data_analize), _translate("MainWindow", "数据分析"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data_json), _translate("MainWindow", "原始数据"))
        self.comboBox_seneorName.setItemText(0, _translate("MainWindow", "温湿度传感器"))
        self.comboBox_seneorName.setItemText(1, _translate("MainWindow", "PM2.5"))
        self.comboBox_seneorName.setItemText(2, _translate("MainWindow", "风速传感器"))
        self.comboBox_seneorName.setItemText(3, _translate("MainWindow", "风向传感器"))
        self.comboBox_seneorName.setItemText(4, _translate("MainWindow", "降雨量传感器"))
        self.comboBox_typeID.setItemText(0, _translate("MainWindow", "101"))
        self.comboBox_typeID.setItemText(1, _translate("MainWindow", "103"))
        self.comboBox_typeID.setItemText(2, _translate("MainWindow", "106"))
        self.comboBox_typeID.setItemText(3, _translate("MainWindow", "107"))
        self.comboBox_typeID.setItemText(4, _translate("MainWindow", "108"))
        self.pushButton.setText(_translate("MainWindow", "查询"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_data_search), _translate("MainWindow", "数据查询"))

