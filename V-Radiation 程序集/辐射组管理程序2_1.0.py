"""def settings(self):
    self.Backgroud.setPixmap(QtGui.QPixmap(self.options[0]))
    self.optionsShow[0].setText("背景图片：" + self.options[0])
    self.optionsShow[1].setText(".SV文件储存位置：" + self.options[1])
    self.optionsShow[2].setCurrentText(self.options[2])
    self.optionsShow[3].setCurrentText(self.options[3])
    self.optionsShow[4].setCurrentText(self.options[4])
def data_update_loading(self):
    with open("plan/data.json", "r", encoding="utf-8") as f:
        data1 = js.load(f)
        data = QDate(data1[0], data1[1], data1[2])
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDateTime(QDateTime(data))
        self.comboBox.setCurrentIndex(data1[3])
        self.listWidget.setFont(QFont("汉仪文黑-85W", 15))
        self.listWidget.clear()
        with open("plan/plan_date.json", "r", encoding="utf-8") as f:
            self.data2 = js.load(f)        for i in self.data2:
                self.listWidget.addItem(i[0] + f"\t{i[1]}-{i[2]}-{i[3]}")
                def data_update_setting(self):
                    data_list = [self.dateEdit.date(), self.dateEdit_2.date()]
                    data_list_ok = []
                    for i in data_list:
                        data_list_ok.append([i.year(), i.month(), i.day()])
                        print(data_list_ok)
                        for jk in range(len(data_list_ok)):
                            try:
                                if jk == 1:
                                    self.data2: List
                                    data_list_ok[jk].insert(0, self.lineEdit.text())
                                    self.data2.append(data_list_ok[jk])
                                    data_list_ok[jk] = self.data2
                                    else:
                                    data_list_ok[jk].append(self.comboBox.currentIndex())
                                    with open(self.file_name_date[jk], "w", encoding="utf-8") as f:
                                        js.dump(data_list_ok[jk], f)
                            except Exception as e:
                                print(e)
                                self.data_update_loading()
                                if __name__ == "__main__":    app = QApplication(sys.argv)    sc = V_Rt2()    sc.show()    app.exec_()"""

from typing import Optional, List

from PyQt5.QtCore import QDateTime, QDate
from PyQt5.QtGui import QFont

from 辐射组管理程序2ui import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
import sys
import data_update as du
import sv_file as sv
import json as js
import datetime
from 统计 import 辐射计划6_镜像计划部分


class V_Rt2(QtWidgets.QWidget, Ui_app):
    sv_all: object
    sv_q: List[Optional[List[str]]]

    def __init__(self):
        self.Signing = False
        self.myDream = 100
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("辐射组管理程序2")
        icon1 = QtGui.QIcon('../logo.ico')
        self.setWindowIcon(icon1)
        self.plan_data = [self.label_16, self.label_17, self.label_18, self.label_20, self.label_21, self.label_22]
        self.subject = ["语文", "数学", "英语", "物理", "生物", "化学"]
        self.bar = [[self.progressBar, self.progressBar_4], [self.progressBar_2, self.progressBar_5],
                    [self.progressBar_3, self.progressBar_6], [self.progressBar_7, self.progressBar_8],
                    [self.progressBar_9, self.progressBar_10], [self.progressBar_11, self.progressBar_12]]
        self.optionsShow = [self.label_69, self.label_70, self.comboBox_3, self.comboBox_4, self.comboBox_5]
        self.sv_check = [self.checkBox, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
                         self.checkBox_6]
        with open("./setting/options.json", "r", encoding="utf-8") as f:
            self.options = js.load(f)
        self.update_plan()
        self.settings()
        self.svUpdate()
        self.Plan.hide()
        self.Game.hide()
        self.Data.hide()
        self.FrApp.hide()
        self.SV.hide()
        self.SignUp.hide()
        self.label_3.setText("今天是 %s年%s月%s日" % (
            datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day))
        self.LogUp.hide()
        self.Setting.hide()
        self.pushButton_16.clicked.connect(self.setting)
        self.pushButton_13.clicked.connect(self.Sign_Up)
        self.Backward_6.clicked.connect(self.ToHome)
        self.Backward_8.clicked.connect(self.save)
        self.verticalScrollBar.valueChanged.connect(self.change_position)
        self.commandLinkButton_2.clicked.connect(self.update_plan)
        self.Backward_8.clicked.connect(self.saveSetting)
        self.pushButton_24.clicked.connect(self.change_backgroundImage)
        self.pushButton_14.clicked.connect(self.sv_image)
        self.pushButton_12.clicked.connect(self.data_update_setting)
        self.data_update_loading()

    def Sign_Up(self):
        self.hide_all()
        self.VIP.hide()
        self.label_8.hide()
        self.label_3.hide()
        self.Home.hide()
        self.SignUp.show()

    def ToHome(self):
        self.VIP.show()
        self.label_8.show()
        self.label_3.show()
        self.Home.show()
        self.SignUp.hide()

    def changePictor(self):
        filename = QFileDialog.getOpenFileName()
        self.label.setPixmap(filename)

    def setting(self):
        self.Home.hide()
        self.Setting.show()
        self.VIP.hide()
        self.label_8.hide()
        self.label_3.hide()

    def save(self):
        self.VIP.show()
        self.label_8.show()
        self.label_3.show()

    def change_position(self):
        self.widget_2.move(80, 33 - self.verticalScrollBar.value())

    def hide_all(self):
        self.Plan.hide()
        self.Game.hide()
        self.Data.hide()
        self.FrApp.hide()
        self.SV.hide()

    def update_plan(self):
        dp = du.Data_Update().plan(way=self.options[2])
        for i in range(len(self.plan_data)):
            self.plan_data[i].setText(f"{self.subject[i]}:{dp[0][i]}/{dp[1][i]}/{dp[2][i]}")
            for j in range(len(self.bar[i])):
                self.bar[i][0].setMaximum(int(dp[1][i]))
                self.bar[i][1].setMaximum(int(dp[2][i]))
                if float(dp[0][i]) / self.bar[i][j].maximum() < 0.65:
                    self.bar[i][j].setStyleSheet(
                        "QProgressBar::chunk{background-color:red; border-radius: 10px;} QProgressBar{text-align:center; border-radius: 10px;}")
                else:
                    self.bar[i][j].setStyleSheet(
                        "QProgressBar::chunk{background-color:green; border-radius: 10px;} QProgressBar{text-align:center; border-radius: 10px;}")
                self.bar[i][j].setValue(int(dp[0][i]))

    def svUpdate(self):
        sv_data = sv.SV_File("./sv30/data2.sv")
        self.sv_q = [sv_data.getData("ch"), sv_data.getData("mt"), sv_data.getData("en"), sv_data.getData("ph"),
                     sv_data.getData("ob"), sv_data.getData("chs"), sv_data.getData("date")]
        self.sv_all = sv_data.getAllScore()
        data_all = sv_data.getData("ch")[-1] + sv_data.getData("mt")[-1] + sv_data.getData("en")[-1] + \
                   sv_data.getData("ph")[-1] + sv_data.getData("ob")[-1] + sv_data.getData("chs")[-1]
        data_all_before = sv_data.getData("ch")[-2] + sv_data.getData("mt")[-2] + sv_data.getData("en")[-2] + \
                          sv_data.getData("ph")[-2] \
                          + sv_data.getData("ob")[-2] + sv_data.getData("chs")[-2]
        cha = data_all - data_all_before
        major = [sv_data.getData("ch")[-1] + sv_data.getData("mt")[-1] + sv_data.getData("en")[-1],
                 sv_data.getData("ch")[-2] + sv_data.getData("mt")[-2] + sv_data.getData("en")[-2]]
        science = [sv_data.getData("ph")[-1] + sv_data.getData("ob")[-1] + sv_data.getData("chs")[-1],
                   sv_data.getData("ph")[-2] + sv_data.getData("ob")[-2] + sv_data.getData("chs")[-2]]
        cha_m = major[0] - major[1]
        cha_s = science[0] - science[1]
        first_university = sv_data.getData('pl')[-1]
        cha_1st = data_all - first_university
        self.label_33.setText(f"自己总分:{data_all}")
        self.label_34.setText(f"本次一本线:{first_university}")
        self.label_36.setText(f"超一本线:{cha_1st} [还差 {self.myDream-cha_1st} ]")
        self.label_37.setText(f"主三科总分:{major[0]}({cha_m})")
        self.label_49.setText(f"理综总分:{science[0]}({cha_s})")
        self.label_35.setText(
            f"离Rp-6目标还差:{sv_data.getData('rtpl')[0] - data_all}({round(data_all / sv_data.getData('rtpl')[0] * 100, 1)}%)")
        self.label_38.setText(
            f"语文:{sv_data.getData('ch')[-1]}({sv_data.getData('ch')[-1] - sv_data.getData('ch')[-2]})")
        self.label_39.setText(
            f"数学:{sv_data.getData('mt')[-1]}({sv_data.getData('mt')[-1] - sv_data.getData('mt')[-2]})")
        self.label_40.setText(
            f"鸟语:{sv_data.getData('en')[-1]}({sv_data.getData('en')[-1] - sv_data.getData('en')[-2]})")
        self.label_50.setText(
            f"物理:{sv_data.getData('ph')[-1]}({sv_data.getData('ph')[-1] - sv_data.getData('ph')[-2]})")
        self.label_51.setText(
            f"生物:{sv_data.getData('ob')[-1]}({sv_data.getData('ob')[-1] - sv_data.getData('ob')[-2]})")
        self.label_52.setText(
            f"化学:{sv_data.getData('chs')[-1]}({sv_data.getData('chs')[-1] - sv_data.getData('chs')[-2]})")
        if cha_1st < 0:
            self.label_53.setText("综合评级:F(一本都没上去大专吧！)")
            self.label_53.setStyleSheet("color:red;")
        elif cha < 0:
            self.label_53.setText("综合评级:E(都倒退了就基本寄了)")
            self.label_53.setStyleSheet("color:red;")
        elif sv_data.getData('rtpl')[0] - data_all > 40:
            self.label_53.setText("综合评级:D(进步了但没有一点进展可不行哟)")
            self.label_53.setStyleSheet("color:red;")
        elif sv_data.getData('rtpl')[0] - data_all < 40:
            self.label_53.setText("综合评级:C(有丁点进展但很难看见)")
            self.label_53.setStyleSheet("color: rgb(255, 145, 19);")
        elif sv_data.getData('rtpl')[0] - data_all < 20:
            self.label_53.setText("综合评级:B(进度肉眼可见增加，加大力度)")
            self.label_53.setStyleSheet("color: yellow;")
        elif sv_data.getData('rtpl')[0] - data_all < 0:
            self.label_53.setText("综合评级:A(进度显著增加撑住！)")
            self.label_53.setStyleSheet("color: green;")
        else:
            self.label_53.setText("综合评级:S(完美完成计划)")
            self.label_53.setStyleSheet("color: rgb(37, 255, 240);")

    def saveSetting(self):
        with open("./setting/options.json", "w", encoding="utf-8") as f:
            js.dump(self.options, f)

    def sv_image(self):
        list1 = []
        sub = []
        if self.checkBox_8.isChecked():
            for i in self.sv_all:
                list1.append(sum(i))
            辐射计划6_镜像计划部分().图表([list1], ["总分"], self.sv_q[-1], 标题="成绩趋势统计-总分")
        elif self.checkBox_7.isChecked():
            for i in self.sv_all:
                list1.append(sum(i[3:6]))
            辐射计划6_镜像计划部分().图表([list1], ["理综"], self.sv_q[-1], 标题="成绩趋势统计-理综")
        else:
            for i in range(len(self.sv_check)):
                if self.sv_check[i].isChecked():
                    list1.append(self.sv_q[i])
                    sub.append(self.subject[i])
            辐射计划6_镜像计划部分().图表(list1, sub, self.sv_q[-1], 标题="成绩趋势统计-单独或多个科目")

    def change_backgroundImage(self):
        self.options[0] = QFileDialog.getOpenFileName()[0]
        self.settings()
        self.saveSetting()

    def settings(self):
        self.Backgroud.setPixmap(QtGui.QPixmap(self.options[0]))
        self.optionsShow[0].setText("背景图片：" + self.options[0])
        self.optionsShow[1].setText(".SV文件储存位置：" + self.options[1])
        self.optionsShow[2].setCurrentText(self.options[2])
        self.optionsShow[3].setCurrentText(self.options[3])
        self.optionsShow[4].setCurrentText(self.options[4])

    def data_update_loading(self):
        with open("plan/data.json", "r", encoding="utf-8") as f:
            data1 = js.load(f)
            data = QDate(data1[0], data1[1], data1[2])
            self.dateEdit.setCalendarPopup(True)
            self.dateEdit.setDateTime(QDateTime(data))
            self.dateEdit_2.setDateTime(QDateTime.currentDateTime())
            self.comboBox.setCurrentIndex(data1[3])
            self.listWidget.setFont(QFont("汉仪文黑-85W", 15))
            self.listWidget.clear()
        with open("plan/plan_date.json", "r", encoding="utf-8") as f:
            self.data2 = js.load(f)
        for i in self.data2:
            self.listWidget.addItem(i[0] + f"\t{i[1]}-{i[2]}-{i[3]}")

    def data_update_setting(self):
        data_list = [self.dateEdit.date(), self.dateEdit_2.date()]
        data_list_ok = []
        for i in data_list:
            data_list_ok.append([i.year(), i.month(), i.day()])
            # print(data_list_ok)
        for jk in range(len(data_list_ok)):
            try:
                # print(data_list_ok[jk])
                if jk == 1:
                    self.data2: List
                    data_list_ok[jk].insert(0, self.lineEdit.text())
                    self.data2.append(data_list_ok[jk])
                    data_list_ok[jk] = self.data2
                    with open("plan/plan_date.json", "w", encoding="utf-8") as f:
                        js.dump(data_list_ok[jk], f)
                else:
                    data_list_ok[jk].append(self.comboBox.currentIndex())
                    with open("plan/date.json", "w", encoding="utf-8") as f:
                        js.dump(data_list_ok[jk], f)
            except Exception as e:
                print(e)
        self.data_update_loading()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sc = V_Rt2()
    sc.show()
    app.exec_()
