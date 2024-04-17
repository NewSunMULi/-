import os
import time
from PyQt5.Qt import *
import sys
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from k2ui import *
import list_download as ld
import json
import Rt_slider as rs
from PyQt5.QtWebEngineWidgets import QWebEngineView


class k2(QThread):
    sign = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.mode1 = None
        self.url_v = None
        self.url_a = None
        self.filename = None
        self.QB = None
        self.QL_list = []
        self.hd2 = {
            'referer': 'https://www.bilibili.com/video',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        }

    def run1(self):
        try:
            if (self.mode1 == "V" or self.mode1 == "VA") or self.url_v is not None:
                with rs.rt.get(self.url_v, headers=self.hd2, stream=True) as s, open(self.filename[:-1] + ".mp4",
                                                                                     'wb') as file:
                    dt = 0
                    total = int(s.headers.get("content-length", 0))
                    self.QB.setMinimum(0)
                    self.QB.setMaximum(total)
                    times = 0
                    now = 0
                    d_byte = 0
                    for data in s.iter_content(chunk_size=1024):
                        if times == 0:
                            dt = time.time()
                        times += 1
                        size = file.write(data)
                        now += size
                        d_byte += size
                        self.QB.setValue(now)
                        if time.time() - dt >= 0.1:
                            if total / 1024 / 1024 > 1024 and now / 1024 / 1024 > 1024:
                                self.QL_list[2].setText(
                                    f"{round(now / (1024 ** 3), 1)}GB/{round(total / (1024 ** 3), 1)}GB")
                            elif total / 1024 / 1024 > 1024:
                                self.QL_list[2].setText(
                                    f"{round(now / (1024 ** 2), 1)}MB/{round(total / (1024 ** 3), 1)}GB")
                            else:
                                self.QL_list[2].setText(
                                    f"{round(now / (1024 ** 2), 1)}MB/{round(total / (1024 ** 2), 1)}MB")
                            v = round(d_byte / (time.time() - dt) / 1024 / 1024, 1)
                            if v != 0:
                                self.QL_list[1].setText(f"{v}MB/s")
                                self.QL_list[0].setText(f"视频---剩余时间:{round((total - now) / 1024 / 1024 / v)}s")
                            times = 0
                            d_byte = 0
                        QApplication.processEvents()
            if (self.mode1 == "A" or self.mode1 == "VA") or self.url_a is not None:
                with rs.rt.get(self.url_a, headers=self.hd2, stream=True) as s, open(self.filename[:-1] + ".mp3",
                                                                                     'wb') as file:
                    dt = 0
                    total = int(s.headers.get("content-length", 0))
                    self.QB.setMinimum(0)
                    self.QB.setMaximum(total)
                    times = 0
                    now = 0
                    d_byte = 0
                    for data in s.iter_content(chunk_size=1024):
                        if times == 0:
                            dt = time.time()
                        times += 1
                        size = file.write(data)
                        now += size
                        d_byte += size
                        self.QB.setValue(now)
                        if time.time() - dt >= 0.1:
                            self.QL_list[2].setText(
                                f"{round(now / (1024 ** 2), 1)}MB/{round(total / (1024 ** 2), 1)}MB")
                            v = round(d_byte / (time.time() - dt) / 1024 / 1024, 2)
                            if v != 0:
                                self.QL_list[1].setText(f"{v}MB/s")
                                self.QL_list[0].setText(f"音频---剩余时间:{round((total - now) / 1024 / 1024 / v, 1)}s")
                            times = 0
                            d_byte = 0
                        QApplication.processEvents()
            self.QL_list[0].setText("视频处理中")
            self.QL_list[1].setText("——")
            self.QL_list[2].setText("——")
            self.QB.setMaximum(0)
            self.QB.setValue(0)
        except Exception as e:
            pass

    def run(self) -> None:
        while True:
            try:
                if self.mode1 == "VA":
                    ad = AudioFileClip(self.filename[:-1] + ".mp3")
                    vd = VideoFileClip(self.filename[:-1] + ".mp4")
                    MP42 = vd.set_audio(ad)
                    MP42.write_videofile(f'{self.filename}.mp4')
                    try:
                        os.remove(self.filename[:-1] + ".mp3")
                        os.remove(self.filename[:-1] + ".mp4")
                    except:
                        time.sleep(10)
                        os.remove(self.filename[:-1] + ".mp3")
                        os.remove(self.filename[:-1] + ".mp4")
                self.QL_list[0].setText("完成")
                break
            except:
                pass


class kk_s(rs.bilibili_slider):
    sign = pyqtSignal(str)

    def __init__(self):
        super(kk_s, self).__init__()


class V_Rt2(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        self.ves = "Kun-Ⅱ Version 2023 Special Commemorative Edition"
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.pushButton_3.clicked.connect(self.quit_app)
        self.setWindowTitle("鲲鲲2.0 特别纪念版")
        self.sc = DL()
        self.ab_quit.clicked.connect(self.quit_app)
        self.pushButton_16.clicked.connect(self.quit_app)
        self.isPress = False
        self.widget_3.hide()
        self.widget_5.hide()
        self.widget_8.hide()
        self.groupBox.hide()
        self.groupBox_2.hide()
        self.pushButton_15.clicked.connect(self.min_window)
        self.pushButton.clicked.connect(self.min_window)
        self.tip()
        self.comboBox_6.currentIndexChanged.connect(self.tip)
        self.pushButton_12.clicked.connect(self.open_down)
        self.options_list = [self.comboBox, self.comboBox_7, self.comboBox_2, self.label_44, self.label_45,
                             self.label_46, self.comboBox_4]
        self.options = {}
        self.pushButton_9.clicked.connect(self.js_change_options)
        self.js_op_options()
        self.pushButton_5.clicked.connect(self.js_print)
        self.pushButton_2.clicked.connect(lambda: self.file_choice(self.label_44, "更改下载文件夹"))
        self.pushButton_7.clicked.connect(lambda: self.file_choice(self.label_45, "更换背景图片", class_=""))
        self.pushButton_8.clicked.connect(lambda: self.file_choice(self.label_46, "更改插件路径"))
        self.format_v = [self.radioButton_5, self.radioButton_6, self.radioButton_7,
                         self.radioButton_11, self.radioButton_12, self.radioButton_13]
        self.quitly = [self.radioButton_8, self.radioButton_9, self.radioButton_10, self.radioButton_14,
                       self.radioButton, self.radioButton_2, self.radioButton_3, self.radioButton_4]
        self.bi = kk_s()
        """        if self.options[1] == "比尔搜索[B站]":
            self.bi = kk_s()
        else:
            self.bi = None"""
        self.pushButton_4.clicked.connect(self.searches)
        self.pushButton_14.clicked.connect(self.bl_view)
        self.inf = None
        self.mission_number = 0
        if self.options[0]:
            self.max_mission = 3
        else:
            self.max_mission = 1
        self.comboBox_5.currentIndexChanged.connect(self.show_srh)
        self.pushButton_11.clicked.connect(
            lambda: self.down(self.inf[0]["title"], self.inf[0]["time"], self.inf[0]['anchor']))
        self.pushButton_13.clicked.connect(
            lambda: self.down(self.inf[0]["title"], self.inf[0]["time"], self.inf[0]['anchor']))
        self.bl2 = k2()

    def js_op_options(self):
        with open("options.json", "r", encoding="utf-8") as file:
            self.options = json.load(file)
            self.label.setPixmap(QPixmap(self.options[4]))

    def js_print(self):
        for i in range(len(self.options_list)):
            try:
                self.options_list[i].setCurrentText(self.options[i])
            except:
                self.options_list[i].setText(self.options[i])

    def js_change_options(self):
        for i in range(len(self.options_list)):
            try:
                if self.options_list[i].currentText() != self.options[i]:
                    self.options[i] = self.options_list[i].currentText()
            except:
                if self.options_list[i].text() != self.options[i]:
                    self.options[i] = self.options_list[i].text()
                    if self.options_list[i] == self.label_45:
                        self.label.setPixmap(QPixmap(self.options[i]))
            if self.options[1] == "比尔搜索[B站]":
                self.bi = rs.bilibili_slider()
            with open("options.json", "w", encoding="utf-8") as file:
                json.dump(self.options, file)

    @staticmethod
    def file_choice(return_label: QLabel, filename: str = "打开文件", class_="dir"):
        if class_ == "dir":
            try:
                pass
                filename1 = QFileDialog.getExistingDirectory(None, filename)
                return_label.setText(filename1)
            except Exception as e:
                pass
        else:
            try:
                filename1 = QFileDialog.getOpenFileName(None, filename)
                return_label.setText(filename1[0])
            except Exception as e:
                pass

    @staticmethod
    def quit_app():
        sys.exit()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F12 and not self.widget_5.isHidden():
            self.widget_5.hide()
        elif event.key() == QtCore.Qt.Key_F12 and not self.widget_8.isHidden():
            self.widget_8.hide()
        self.widget_2.show()

    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton:
                self.isPress = True
                self.before_pos = event.globalPos() - self.pos()
                event.accept()
        except Exception as e:
            pass

    def mouseMoveEvent(self, event2):
        if self.isPress and Qt.LeftButton and (self.widget.underMouse() or self.widget_6.underMouse() or self.widget_9.underMouse()):
            self.move(event2.globalPos() - self.before_pos)
            event2.accept()

    def mouseReleaseEvent(self, event3):
        self.isPress = False

    def min_window(self):
        self.setWindowState(Qt.WindowMinimized)

    def tip(self):
        if self.comboBox_6.currentText() == "自动":
            self.lineEdit.setPlaceholderText("ID、地址和关键词都行，但搜不搜得出来看搜索算法和老天")
        elif self.comboBox_6.currentText() == "ID":
            self.lineEdit.setPlaceholderText("输入ID[rid/BV/抖音号...]来获取视频或音频")
        elif self.comboBox_6.currentText() == "URL":
            self.lineEdit.setPlaceholderText("输入完整网址来获取视频或音频")
        elif self.comboBox_6.currentText() == "关键词":
            self.lineEdit.setPlaceholderText("输入关键词可查找对应搜索算法下的资源，无须具体网址")
        elif self.comboBox_6.currentText() == "唱片机":
            self.lineEdit.setPlaceholderText("目前只支持rid搜索且只支持老狗搜索算法")

    def open_down(self):
        self.sc.show()

    def searches(self):
        try:
            self.groupBox_2.hide()
            self.groupBox.hide()
            self.bi.final.clear()
            self.bi.title.clear()
            self.bi.keyword = self.lineEdit.text()
            if self.comboBox_6.currentText() == "关键词":
                self.bi.mode = rs.Mode.KWY_WORD
            elif self.comboBox_6.currentText() == "URL":
                self.bi.mode = rs.Mode.URL
            elif self.comboBox_6.currentText() == 'ID':
                self.bi.mode = rs.Mode.BV_TID
            elif self.comboBox_6.currentText() == "唱片机":
                self.bi.mode = rs.Mode.RID
            else:
                self.bi.mode = rs.Mode.AUTO
            self.bi.get()
            pass
            if len(self.bi.title) > 1:
                self.groupBox_2.show()
                self.comboBox_5.clear()
                if len(self.comboBox_5) <= 40:
                    for i in range(len(self.bi.title)):
                        self.comboBox_5.addItem(self.bi.title[i])
                else:
                    for i in range(len(self.bi.title)):
                        self.comboBox_5.setItemText(i, self.bi.title[i])
            else:
                self.groupBox.show()

            self.show_srh()
        except Exception as p:
            QMessageBox.warning(self, "来自鲲鲲的警告", f"搜索算法选择错误，请设置正确的搜索算法后再来搜索获取资源！\n代码错误信息：{p}")

    def show_srh(self):
        if not self.groupBox_2.isHidden():
            self.inf = self.bi.find(self.bi.final[self.comboBox_5.currentIndex()])
            self.label_33.setText(self.bi.final[self.comboBox_5.currentIndex()][-12:-1])
            self.label_35.setText(self.inf[0]["anchor"])
            self.label_37.setText(f'{self.inf[0]["time"] // 60000}min {(self.inf[0]["time"] // 1000 % 60) + 1}s')
        else:
            self.inf = self.bi.find(self.bi.final[0])
            self.label_7.setText("作品名：" + self.inf[0]["title"])
            self.label_8.setText("作者：" + self.inf[0]["anchor"])

    def formats(self):
        if not self.groupBox_2.isHidden():
            x = 0
        else:
            x = 3
        for i in range(x, 3 + x):
            if self.format_v[i].isChecked():
                if i == 0 + x:
                    return "VA"
                elif i == 1 + x:
                    return "A"
                else:
                    return "V"

    def down(self, name, time_v, anchor):
        try:
            format1 = self.formats()
            self.sc.show()
            self.min_window()
            if not self.sc.tip.isHidden():
                self.sc.tip.hide()
            p = self.mission_number
            self.sc.down_list[p].show()
            self.mission_number += 1
            eval(f"self.sc.information{p + 1}.setValue(0)")
            eval(f"self.sc.anchor{p + 1}.setText('anchor:{anchor}')")
            eval(f"self.sc.name{p + 1}.setText('{p + 1}.{name}')")
            eval(f"self.sc.time{p + 1}.setText('时长:{time_v // 60000}min{(time_v // 1000 % 60) + 1}s')")
            if format1 == "V":
                eval(f"self.sc.format{p + 1}.setText('格式:MP4[无声]')")
            elif format1 == "A":
                eval(f"self.sc.format{p + 1}.setText('格式:MP3纯音频')")
            else:
                eval(f"self.sc.format{p + 1}.setText('格式:MP4[有声]')")
            self.bl2.QB = eval(f"self.sc.information{p + 1}")
            self.bl2.QL_list = eval(f"[self.sc.pass_time{p + 1}, self.sc.speed{p + 1}, self.sc.number{p + 1}]")
            if format1 != "A":
                for j in range(0, len(self.inf[2])):
                    pass
                    if not self.groupBox.isHidden():
                        j = 4 + j
                        pass
                    if self.quitly[j].isChecked():
                        if j >= 4:
                            j -= 4
                        pass
                        self.bl2.mode1 = format1
                        self.bl2.url_v = self.inf[2][j]
                        if format1 != "V":
                            self.bl2.url_a = self.inf[1][j]
                        else:
                            self.bl2.url_a = None
                        self.bl2.filename = QFileDialog.getExistingDirectory(self,
                                                                             "保存视频文件") + f"/{self.inf[0]['title']}"
                        if self.bl2.filename == f"/{self.inf[0]['title']}":
                            break
                        time.sleep(3)
                        pass

                        self.bl2.run1()
                        self.bl2.start()
                        self.mission_number = 0
                        break
                else:
                    QMessageBox.warning(self, "警告", "无此画质的视频，请重新选")
                    self.mission_number = 0
                    self.sc.down.hide()
            else:
                self.bl2.mode1 = format1
                self.bl2.url_a = self.inf[1][0]
                self.bl2.filename = QFileDialog.getExistingDirectory(self, "保存视频文件") + f"/{self.inf[0]['title']}"
                self.bl2.run1()
                self.bl2.start()
                self.mission_number = 0
        except Exception as e:
            pass

    def bl_view(self):
        if self.ves == "Kun-Ⅱ Version 2023 Special Commemorative Edition":
            self.widget_2.hide()
            self.widget_8.show()
            self.web = QWebEngineView(self.widget_8)
            self.web.setGeometry(QRect(0, 50, 1280, 720))
            self.web.show()
            self.web.load(QUrl("https://search.bilibili.com"))


class DL(QtWidgets.QWidget, ld.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle("鲲鲲2.0 特别纪念版 下载任务列表")
        self.pushButton_3.clicked.connect(self.quit_app)
        self.pushButton.clicked.connect(self.min_window)
        self.down.hide()
        self.down_2.hide()
        self.down_3.hide()
        self.tip = QLabel(self.groupBox)
        self.tip.setGeometry(QRect(50, 80, 350, 50))
        self.font1 = QtGui.QFont()
        self.font1.setFamily("华光钢铁直黑 可变体 Medium")
        self.font1.setPointSize(30)
        self.tip.setFont(self.font1)
        self.tip.setText("没有下载任务")
        self.tip.setStyleSheet("color:rgba(0, 0, 0, 150)")
        self.down_list = [self.down, self.down_2, self.down_3]

    def quit_app(self):
        self.hide()

    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton:
                self.isPress = True
                self.before_pos = event.globalPos() - self.pos()
                event.accept()
        except Exception as e:
            pass

    def mouseMoveEvent(self, event2):
        if self.isPress and Qt.LeftButton and self.widget_2.underMouse():
            self.move(event2.globalPos() - self.before_pos)
            event2.accept()

    def mouseReleaseEvent(self, event3):
        self.isPress = False

    def min_window(self):
        self.setWindowState(Qt.WindowMinimized)


try:
    app = QApplication(sys.argv)
    sc1 = V_Rt2()
    sc1.show()
    app.exec()
except Exception as e:
    pass
