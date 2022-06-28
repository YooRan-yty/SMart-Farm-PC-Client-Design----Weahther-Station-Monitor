import sys
import json
import threading
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableView
from PyQt5.QtCore import *
from Ui_Form import Ui_MainWindow
from PyQt5.QtGui import QTransform, QPixmap, QImage, QTextCursor
import time
import datetime
import paho.mqtt.client as mqtt_client
import queue
from mqtt import Mqtt
from sqlite_demo import DB
import sqlite3
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis, QDateTimeAxis, QSplineSeries
from ChartView import *
import random
import requests
import re
g_queue = queue.Queue(maxsize=20) #设定先进先出的队列
q2 = queue.Queue(maxsize=20)#更新原始数据的队列
q3 = queue.Queue(maxsize=20)#更新数据库的队列

conn = sqlite3.connect("weather.db")
c = conn.cursor()

def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except ValueError as e:
        return False
    return True

def on_connect(client,userdata,flags,rc):
    print("连接服务器结果 : "+str(rc))
    client.subscribe("testtopic/1")

def on_message(client,userdata,msg):
    print(msg.topic + "  " + str(msg.payload))
    dispatch_msg(g_queue,str(msg.payload.decode()))
    dispatch_msg(q2,str(msg.payload.decode()))
    dispatch_msg(q3,str(msg.payload.decode()))

def dispatch_msg(q,msg):
    q.put(msg)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.y_rain = 0
        self.y_ws = 0
        self.y_temp = 0
        self.y_hum = 0

        # 启动接受订阅线程
        self.mqtt_client = Mqtt(on_connect=on_connect,on_message=on_message)
        self.mqtt_client.start_thread()
        self.q = g_queue

        # 启动显示消息线程,start_msg_thread
        self.thread = None
        self.run_flag = False
        self.start_msg_thread()

        #更新tabWidget的原始数据
        self.dis_json = display_json()
        self.dis_json.start()
        self.dis_json.trigger.connect(self.display_json)

        #数据库插入数据
        self.db = DateBase()
        self.db.start()
        self.db.trigger.connect(self.dis_db_insert)

        #comboBox关联
        self.ui.comboBox_seneorName.activated.connect(lambda :self.to_combox2(self.ui.comboBox_seneorName.currentText()))
        self.ui.comboBox_typeID.activated.connect(lambda: self.to_combox1(self.ui.comboBox_typeID.currentText()))

        #数据库查询数据
        self.ui.pushButton.clicked.connect(self.db_select)

        #数据可视化
        self.draw_rain()
        self.draw_ws()
        self.draw_temp()
        self.draw_hum()
        self.timer_init()

        self.weather_get()


    def db_select(self):
        sqlDemo.connect_db(self)
        sqlDemo.show_db(self)
        sqlDemo.close_db(self)
        print("clicked")


    def draw_rain(self):
        self.chart_rain = QChart()
        self.series_rain = QSplineSeries()
        # 设置曲线名称
        self.series_rain.setName("降雨量")
        # 把曲线添加到QChart的实例中
        self.chart_rain.addSeries(self.series_rain)
        # 声明并初始化X轴，Y轴
        self.dtaxisX_rain = QDateTimeAxis()
        self.vlaxisY_rain = QValueAxis()
        # 设置坐标轴显示范围
        self.dtaxisX_rain.setMin(QDateTime.currentDateTime().addSecs(-3))
        self.dtaxisX_rain.setMax(QDateTime.currentDateTime().addSecs(0))
        self.vlaxisY_rain.setMin(0)
        self.vlaxisY_rain.setMax(20)
        # 设置X轴时间样式
        self.dtaxisX_rain.setFormat("hh:mm:ss")
        # 设置坐标轴名称
        self.dtaxisX_rain.setTitleText("时间")
        self.vlaxisY_rain.setTitleText("数据")
        # 设置网格不显示
        self.dtaxisX_rain.setTickCount(2)
        self.vlaxisY_rain.setTickCount(4)
        self.vlaxisY_rain.setGridLineVisible(False)
        # 把坐标轴添加到chart中
        self.chart_rain.addAxis(self.dtaxisX_rain, Qt.AlignBottom)
        self.chart_rain.addAxis(self.vlaxisY_rain, Qt.AlignLeft)
        # 把曲线关联到坐标轴
        self.series_rain.attachAxis(self.dtaxisX_rain)
        self.series_rain.attachAxis(self.vlaxisY_rain)

        chart_view = QChartView(self.chart_rain)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.v_rain.addWidget(chart_view)

    def draw_ws(self):
        self.chart_ws = QChart()
        self.series_ws = QSplineSeries()
        # 设置曲线名称
        self.series_ws.setName("风速")
        # 把曲线添加到QChart的实例中
        self.chart_ws.addSeries(self.series_ws)
        # 声明并初始化X轴，Y轴
        self.dtaxisX_ws = QDateTimeAxis()
        self.vlaxisY_ws = QValueAxis()
        # 设置坐标轴显示范围
        self.dtaxisX_ws.setMin(QDateTime.currentDateTime().addSecs(-3))
        self.dtaxisX_ws.setMax(QDateTime.currentDateTime().addSecs(0))
        self.vlaxisY_ws.setMin(0)
        self.vlaxisY_ws.setMax(20)
        # 设置X轴时间样式
        self.dtaxisX_ws.setFormat("hh:mm:ss")
        # 设置坐标轴名称
        self.dtaxisX_ws.setTitleText("时间")
        self.vlaxisY_ws.setTitleText("数据")
        # 设置网格不显示
        self.dtaxisX_ws.setTickCount(2)
        self.vlaxisY_ws.setTickCount(4)
        self.vlaxisY_ws.setGridLineVisible(False)
        # 把坐标轴添加到chart中
        self.chart_ws.addAxis(self.dtaxisX_ws, Qt.AlignBottom)
        self.chart_ws.addAxis(self.vlaxisY_ws, Qt.AlignLeft)
        # 把曲线关联到坐标轴
        self.series_ws.attachAxis(self.dtaxisX_ws)
        self.series_ws.attachAxis(self.vlaxisY_ws)

        chart_view = QChartView(self.chart_ws)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.v_ws.addWidget(chart_view)

    def draw_temp(self):
        self.chart_temp = QChart()
        self.series_temp = QSplineSeries()
        # 设置曲线名称
        self.series_temp.setName("温度")
        # 把曲线添加到QChart的实例中
        self.chart_temp.addSeries(self.series_temp)
        # 声明并初始化X轴，Y轴
        self.dtaxisX_temp = QDateTimeAxis()
        self.vlaxisY_temp = QValueAxis()
        # 设置坐标轴显示范围
        self.dtaxisX_temp.setMin(QDateTime.currentDateTime().addSecs(-3))
        self.dtaxisX_temp.setMax(QDateTime.currentDateTime().addSecs(0))
        self.vlaxisY_temp.setMin(0)
        self.vlaxisY_temp.setMax(60)
        # 设置X轴时间样式
        self.dtaxisX_temp.setFormat("hh:mm:ss")
        # 设置坐标轴名称
        self.dtaxisX_temp.setTitleText("时间")
        self.vlaxisY_temp.setTitleText("数据")
        # 设置网格不显示
        self.dtaxisX_temp.setTickCount(2)
        self.vlaxisY_temp.setTickCount(4)
        self.vlaxisY_temp.setGridLineVisible(False)
        # 把坐标轴添加到chart中
        self.chart_temp.addAxis(self.dtaxisX_temp, Qt.AlignBottom)
        self.chart_temp.addAxis(self.vlaxisY_temp, Qt.AlignLeft)
        # 把曲线关联到坐标轴
        self.series_temp.attachAxis(self.dtaxisX_temp)
        self.series_temp.attachAxis(self.vlaxisY_temp)

        chart_view = QChartView(self.chart_temp)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.v_temp.addWidget(chart_view)

    def draw_hum(self):
        self.chart_hum = QChart()
        self.series_hum = QSplineSeries()
        # 设置曲线名称
        self.series_hum.setName("湿度")
        # 把曲线添加到QChart的实例中
        self.chart_hum.addSeries(self.series_hum)
        # 声明并初始化X轴，Y轴
        self.dtaxisX_hum = QDateTimeAxis()
        self.vlaxisY_hum = QValueAxis()
        # 设置坐标轴显示范围
        self.dtaxisX_hum.setMin(QDateTime.currentDateTime().addSecs(-3))
        self.dtaxisX_hum.setMax(QDateTime.currentDateTime().addSecs(0))
        self.vlaxisY_hum.setMin(0)
        self.vlaxisY_hum.setMax(100)
        # 设置X轴时间样式
        self.dtaxisX_hum.setFormat("hh:mm:ss")
        # 设置坐标轴名称
        self.dtaxisX_hum.setTitleText("时间")
        self.vlaxisY_hum.setTitleText("数据")
        # 设置网格不显示
        self.dtaxisX_hum.setTickCount(2)
        self.vlaxisY_hum.setTickCount(4)
        self.vlaxisY_hum.setGridLineVisible(False)
        # 把坐标轴添加到chart中
        self.chart_hum.addAxis(self.dtaxisX_hum, Qt.AlignBottom)
        self.chart_hum.addAxis(self.vlaxisY_hum, Qt.AlignLeft)
        # 把曲线关联到坐标轴
        self.series_hum.attachAxis(self.dtaxisX_hum)
        self.series_hum.attachAxis(self.vlaxisY_hum)

        chart_view = QChartView(self.chart_hum)
        chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.v_hum.addWidget(chart_view)

    def timer_init(self):
        # 使用QTimer，1秒触发一次，更新数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.drawLine_rain)
        self.timer.timeout.connect(self.drawLine_ws)
        self.timer.timeout.connect(self.drawLine_temp)
        self.timer.timeout.connect(self.drawLine_hum)
        self.timer.start(1000)

    def drawLine_rain(self):
        #获取当前时间
        bjtime = QDateTime.currentDateTime()
        #更新X轴坐标
        self.dtaxisX_rain.setMin(QDateTime.currentDateTime().addSecs(-3))
        self.dtaxisX_rain.setMax(QDateTime.currentDateTime().addSecs(0))
        #当曲线上的点超出X轴的范围时，移除最早的点
        if(self.series_rain.count()>5):
            self.series_rain.removePoints(0,self.series_rain.count()-5)

    #添加数据到曲线末端
        self.series_rain.append(bjtime.toMSecsSinceEpoch(),self.y_rain)

    def drawLine_ws(self):
        #获取当前时间
        bjtime = QDateTime.currentDateTime()
        #更新X轴坐标
        self.dtaxisX_ws.setMin(QDateTime.currentDateTime().addSecs(-3))
        self.dtaxisX_ws.setMax(QDateTime.currentDateTime().addSecs(0))
        #当曲线上的点超出X轴的范围时，移除最早的点
        if(self.series_ws.count()>5):
            self.series_ws.removePoints(0,self.series_ws.count()-5)

        #添加数据到曲线末端
        self.series_ws.append(bjtime.toMSecsSinceEpoch(),self.y_ws)

    def drawLine_temp(self):
        #获取当前时间
        bjtime = QDateTime.currentDateTime()
        #更新X轴坐标
        self.dtaxisX_temp.setMin(QDateTime.currentDateTime().addSecs(-3))
        self.dtaxisX_temp.setMax(QDateTime.currentDateTime().addSecs(0))
        #当曲线上的点超出X轴的范围时，移除最早的点
        if(self.series_temp.count()>5):
            self.series_temp.removePoints(0,self.series_temp.count()-5)

        #添加数据到曲线末端
        self.series_temp.append(bjtime.toMSecsSinceEpoch(),self.y_temp)

    def drawLine_hum(self):
        #获取当前时间
        bjtime = QDateTime.currentDateTime()
        #更新X轴坐标
        self.dtaxisX_hum.setMin(QDateTime.currentDateTime().addSecs(-3))
        self.dtaxisX_hum.setMax(QDateTime.currentDateTime().addSecs(0))
        #当曲线上的点超出X轴的范围时，移除最早的点
        if(self.series_hum.count()>5):
            self.series_hum.removePoints(0,self.series_hum.count()-5)

        #添加数据到曲线末端
        self.series_hum.append(bjtime.toMSecsSinceEpoch(),self.y_hum)



    def to_combox1(self,name):
        if self.ui.comboBox_typeID.currentText() == "101":
            name = "温湿度传感器"
            self.ui.comboBox_seneorName.setCurrentText(name)

        elif self.ui.comboBox_typeID.currentText() == "103":
            name = "PM2.5"
            self.ui.comboBox_seneorName.setCurrentText(name)

        elif self.ui.comboBox_typeID.currentText() == "106":
            name = "风速传感器"
            self.ui.comboBox_seneorName.setCurrentText(name)

        elif self.ui.comboBox_typeID.currentText() == "107":
            name = "风向传感器"
            self.ui.comboBox_seneorName.setCurrentText(name)

        else:
            name = "降雨量传感器"
            self.ui.comboBox_seneorName.setCurrentText(name)


    def to_combox2(self,id):
        if self.ui.comboBox_seneorName.currentText() == "温湿度传感器":
            id = "101"
            self.ui.comboBox_typeID.setCurrentText(id)

        elif self.ui.comboBox_seneorName.currentText() == "PM2.5":
            id = "103"
            self.ui.comboBox_typeID.setCurrentText(id)

        elif self.ui.comboBox_seneorName.currentText() == "风速传感器":
            id = "106"
            self.ui.comboBox_typeID.setCurrentText(id)

        elif self.ui.comboBox_seneorName.currentText() == "风向传感器":
            id = "107"
            self.ui.comboBox_typeID.setCurrentText(id)

        else:
            id = "108"
            self.ui.comboBox_typeID.setCurrentText(id)

    def dis_db_insert(self,dict):
        _in = "insert into test values(?,?,?,?,?,?)"
        MC = str(dict['messageClass'])
        Did = float(dict['deviceID'])
        Tid = float(dict['typeID'])
        Vol = float(dict['voletage'])
        Tim = datetime.datetime.now()      #str(dict['timestamp'])
        if Tid == 103:
            PmData = float(dict['pm2.5'])
            v = (MC, Did, Tid, PmData, Vol, Tim)
            c.execute(_in, v)
            conn.commit()
            print("in complete")

        elif Tid == 101:
            tempData = float(dict['temperature'])
            humData = float(dict['humidity'])
            self.y_temp = tempData
            self.y_hum = humData
            v = (MC, Did, Tid, tempData, Vol, Tim)
            conn.execute(_in, v)
            v = (MC, Did, Tid, humData, Vol, Tim)
            conn.execute(_in,v)
            conn.commit()
            print("in complete")

        elif Tid == 106:
            windspeedData = float(dict['windspeed'])
            self.y_ws = windspeedData
            v = (MC, Did, Tid, windspeedData, Vol, Tim)
            conn.execute(_in, v)
            conn.commit()
            print("in complete")

        elif Tid == 107:
            winddirecData = float(dict['winddirection'])
            v = (MC, Did, Tid, winddirecData, Vol, Tim)
            conn.execute(_in, v)
            conn.commit()
            print("in complete")

        elif Tid == 108:
            rainData = float(dict['rainsnow'])
            self.y_rain = rainData
            v = (MC, Did, Tid, rainData, Vol, Tim)
            conn.execute(_in, v)
            conn.commit()
            print("in complete")

        else:
            print('Not weather message!')

    def display_json(self,str):
        self.ui.textEdit.setLineWrapMode(1)
        self.ui.textEdit.append(str)

    def weather_get(self):
        print("start weather_get")
        url = "https://wis.qq.com/weather/common?source=pc&weather_type=observe|forecast_1h|forecast_24h|index|alarm|limit|tips|rise&province=%E5%9B%9B%E5%B7%9D%E7%9C%81&city=%E6%88%90%E9%83%BD%E5%B8%82&county=&callback=jQuery111306722337658251196_1644226386537&_=1644226386539"

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"
        }

        req = requests.get(url, headers=headers)
        req.encoding = 'utf-8'
        page = req.text

        obj = re.compile(r"jQuery.*?[(](?P<json>.*?)[)]",re.S)
        resp = obj.finditer(page)
        for i in resp:
            str = i.group("json")

        info_json = json.loads(str)
        weather_condition = info_json['data']['observe']['weather']
        wind_direction = info_json['data']['forecast_1h']['0']['wind_direction']
        tips = info_json['data']['tips']['observe']['0']

        self.ui.label_weather.setText(weather_condition)
        self.ui.label_tips.setText(tips)
        self.ui.label_wind_direction.setText(wind_direction)
        req.close()


    def wind_warn_sys(self):
        #wind
        if self.ws_data > 8.0 and self.ws_data <= 10.0:
            self.ui.label_warn_wind.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/wind_blue.png"))
        elif self.ws_data > 10.0 and self.ws_data <= 17.0:
            self.ui.label_warn_wind.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/wind_yellow.png"))
        elif self.ws_data > 17.0 and self.ws_data <= 24.0:
            self.ui.label_warn_wind.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/wind_oren.png"))
        elif self.ws_data > 24:
            self.ui.label_warn_wind.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/wind_red.png"))
        else:
            self.ui.label_warn_wind.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/wu.png"))

    def rain_warn_sys(self):
        #rain
        if self.rain_data * 24 >= 50:
            self.ui.label_warn_rain.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/rain_blue.png"))
        elif self.rain_data * 24 >= 100:
            self.ui.label_warn_rain.setPixmap((QtGui.QPixmap("/Users/tyy/Desktop/Farm/rain_yellow.png")))
        elif self.rain_data * 24 >= 150:
            self.ui.label_warn_rain.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/rain_oren.png"))
        elif self.rain_data * 24 >= 200:
            self.ui.label_warn_rain.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/rain_red.png"))
        else:
            self.ui.label_warn_rain.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/wu.png"))

    def temp_warn_sys(self):
        if self.temp_data >= 37:
            self.ui.label_warn_temp.setPixmap((QtGui.QPixmap("/Users/tyy/Desktop/Farm/temp_oren.png")))

        elif self.temp_data >=35 and self.temp_data < 37:
            self.ui.label_warn_temp.setPixmap((QtGui.QPixmap("/Users/tyy/Desktop/Farm/temp_yellow.png")))

        elif self.temp_data >=40 :
            self.ui.label_warn_temp.setPixmap((QtGui.QPixmap("/Users/tyy/Desktop/Farm/temp_red.png")))

        else:
            self.ui.label_warn_temp.setPixmap((QtGui.QPixmap("/Users/tyy/Desktop/Farm/wu.png")))

    def pix_rotate(self):
        transform = QTransform()
        if self.wd_data >= 0 and self.wd_data <= 90:
            transform.rotate(90 - self.wd_data)
            self.ui.label_wdpix.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/风向.png").transformed(transform))
        else:
            transform.rotate(-(self.wd_data - 90))
            self.ui.label_wdpix.setPixmap(QtGui.QPixmap("/Users/tyy/Desktop/Farm/风向.png").transformed(transform))

       #更新UI主界面
    def display_msg(self):
        obj = json.loads(self.msg) #将已编码的 JSON 字符串解码为 Python 对象
        if obj['typeID'] == "106":
            self.ws_data = float(obj['windspeed'])
            self.ui.label_wsdata.setText(str(self.ws_data))
            self.wind_warn_sys()

        elif obj['typeID'] == "107":
            self.wd_data = float(obj['winddirection'])
            self.ui.label_wddata.setText(str(self.wd_data))
            self.pix_rotate()

        elif  obj['typeID'] == "108":
            self.rain_data = float(obj['rainsnow'])
            self.ui.label_raindata.setText(str(self.rain_data))
            self.rain_warn_sys()

        elif  obj['typeID'] == "103":
            self.pm_data = float(obj['pm2.5'])
            self.ui.label_pmdata_2.setText(str(self.pm_data))

        elif  obj['typeID'] == "101":
            self.temp_data = float(obj['temperature'])
            self.hum_data = float(obj['humidity'])
            self.ui.label_tempdata.setText(str(self.temp_data) + ' ℃')
            self.ui.label_humdata.setText(str(self.hum_data))
            self.temp_warn_sys()

        else:
            print('None weather message!')


    def handle_msg_thread(self):
        while self.run_flag:
            print('start:run_flag')
            self.msg = self.q.get(block=True)
            print('get msg : '+ self.msg)
            if is_json(self.msg) and self.msg.find('messageClass')>=0:
                self.display_msg()
                # self.weather_get()
            else:
                print('msg error :: '+ self.msg)


    def start_msg_thread(self):
        self.run_flag = True
        t = threading.Thread(target = Window.handle_msg_thread,args=(self,))
        self.thread = t
        t.setDaemon(True)
        t.start()



    def closeEvent(self,event):
        reply=QtWidgets.QMessageBox.question(self,u'警告',u'确认退出?',QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
        #QtWidgets.QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
        if reply==QtWidgets.QMessageBox.Yes:
            event.accept()#关闭窗口
            self.run_flag = False
            self.mqtt_client.close()
        else:
            event.ignore()#忽视点击X事件

class display_json(QThread): #更新tabWidget的原始数据
    trigger = pyqtSignal(str)

    def __init__(self):
        super(display_json,self).__init__()
        self.q2 = q2
        self.run_flag2 = True

    def run(self):
        while self.run_flag2:
            json = self.q2.get(block=True)
            if is_json(json) and json.find('messageClass')>=0:
                self.trigger.emit(json)
            else:
                print('msg error :: '+ json)


class DateBase(QThread):
    trigger = pyqtSignal(dict)

    def __init__(self):
        super(DateBase, self).__init__()
        self.run_flag3 = True

    def run(self):
        self.connect_db()
        while self.run_flag3:
            data = q3.get(block=True)
            if is_json(data) and data.find('messageClass')>=0:
                self.dict_json = json.loads(data)
                self.trigger.emit(self.dict_json)
            else:
                print('msg error :: '+ data)


    def connect_db(self):
            conn = sqlite3.connect("weather.db")
            print("open db suc")


    def create_table(self):

        c.execute('''
        CREATE TABLE DATA
        (
        MESSAGECLASS TEXT NOT NULL,
        DEVICEID TEXT NOT NULL,
        TYPEID TEXT NOT NULL,
        DATA TEXT NOT NULL,
        VOLETAGE TEXT NOT NULL,
        TIME TEXT NOT NULL);
        ''')
        conn.commit()
        print("table created")

class sqlDemo(object):
    def __init__(self):
        super().__init__()

    def connect_db(self):
        self.db = QSqlDatabase
        if QSqlDatabase.contains("qt_sql_default_connection"):
            self.db = QSqlDatabase.database("qt_sql_default_connection")
        else:
            self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('./weather.db')
        self.db.open()

    def opreate_db(self):
        query = QSqlQuery()


    def show_db(self):
        tablemodel  = QSqlTableModel()
        tablemodel.setTable('test')
        tablemodel.select()

        text = self.ui.comboBox_typeID.currentText()
        tablemodel.setFilter("typeid= '{}'".format(float(text)))
        tablemodel.select()

        self.ui.tableView.setModel(tablemodel)


    # 关闭数据库
    def close_db(self):
        self.db.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())

