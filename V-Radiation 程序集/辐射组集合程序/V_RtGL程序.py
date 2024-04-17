import sys
import time

from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication
import V_RtGL_米戏聚合启动器部分 as GM
import V_RtGL_辐射组管理程序部分 as RM
from V_RtGL import *
from Setting import Ui_Form as Su
from open import Ui_Dialog as op
import enum


class V_RtGL_enum(enum.Enum):
    GM = 0
    RM = 1


class Open_view(QDialog, op):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.SplashScreen)
        self.label_5.setText("")
        self.show()

    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton:
                self.isPress = True
                self.before_pos = event.globalPos() - self.pos()
                event.accept()
        except Exception as e:
            pass

    def mouseMoveEvent(self, event2):
        if self.isPress and Qt.LeftButton and self.underMouse():
            self.move(event2.globalPos() - self.before_pos)
            event2.accept()

    def mouseReleaseEvent(self, event3):
        self.isPress = False


class setting(QDialog, Su):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.SplashScreen)
        self.close_1.clicked.connect(self.quit1)
        self.tuodongtiao.setPageStep(500)
        self.tuodongtiao.setMaximum(self.setting_page.height() - self.main.height())
        self.tuodongtiao.valueChanged.connect(self.change_position)
        self.setting_button = [self.usy, self.file, self.gst, self.vt_s, self.about]
        self.usy.clicked.connect(lambda: self.set_position(sd=0))
        self.file.clicked.connect(lambda: self.set_position(sd=self.main.height() * 1))
        self.gst.clicked.connect(lambda: self.set_position(sd=self.main.height() * 5))
        self.vt_s.clicked.connect(lambda: self.set_position(sd=self.main.height() * 6))
        self.about.clicked.connect(lambda: self.set_position(sd=self.main.height() * 7))
        self.page = 0
        self.setting_button[self.page].setCheckable(True)
        self.setting_button[self.page].setChecked(True)
        self.main.installEventFilter(self)
        self.灵敏度 = 2.4
        self.setWindowModality(Qt.ApplicationModal)  # 当对话框显示时，主窗口的所有控件都不可用

    def quit1(self):
        self.close()

    def change_position(self):
        self.setting_page.setGeometry(0, -self.tuodongtiao.value(), self.setting_page.width(),
                                      self.setting_page.height())
        if (-self.setting_page.pos().y()) + self.main.height() > self.setting_page.height():
            self.setting_page.setGeometry(0, self.setting_page.height() - self.main.height(), 581, 2541)
        for i in self.setting_button:
            i.setChecked(False)
            i.setCheckable(False)
        try:
            if 1 <= (-self.setting_page.pos().y()) // self.main.height() <= 4:
                self.page = 1
            elif (-self.setting_page.pos().y()) // self.main.height() > 4:
                self.page = (-self.setting_page.pos().y()) // self.main.height() - 3
            else:
                self.page = (-self.setting_page.pos().y()) // self.main.height()
            self.setting_button[self.page].setCheckable(True)
            self.setting_button[self.page].setChecked(True)
        except Exception as e:
            print(e)

    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton:
                self.isPress = True
                self.before_pos = event.globalPos() - self.pos()
                event.accept()
        except Exception as e:
            pass

    def mouseMoveEvent(self, event2):
        if self.isPress and Qt.LeftButton and self.pos_c.underMouse():
            self.move(event2.globalPos() - self.before_pos)
            event2.accept()

    def mouseReleaseEvent(self, event3):
        self.isPress = False

    def eventFilter(self, wt: 'QObject', event: 'QEvent'):
        if wt == self.main:
            if event.type() == QEvent.Wheel:
                event: QWheelEvent
                self.tuodongtiao.setValue(self.tuodongtiao.value() - int(event.angleDelta().y() / self.灵敏度))
            return False
        else:
            return True

    def set_position(self, sd: int = 0):
        self.tuodongtiao.setValue(sd)


class V_RtGL_app(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        self.time = 0
        self.open = Open_view()
        super().__init__()
        self.SRG = GM.Star_Rail()
        self.GES = GM.Genshin_Impact()
        self.BH3S = GM.BH3()
        self.KSP2 = GM.KSP()
        self.other = GM.Game_launcher()
        self.setting_param = None
        with open("setting.json", "r", encoding="utf-8") as f:
            self.setting_param = GM.js.load(f)
        self.types = V_RtGL_enum.GM
        self.cu_app = None
        self.cos_bg = False
        self.alpha = 0.9
        self.screenSetting = setting()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle("辐射组集合程序")
        self.setWindowOpacity(self.alpha)  # 设置窗口透明度
        self.index_button = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4,
                             self.pushButton_5, self.pushButton_6, self.pushButton_7]
        self.index_banana = [self.banana, self.banana_2, self.banana_3, self.banana_4,
                             self.banana_5, self.banana_6, self.banana_7]
        self.app_list_GM = []
        self.app_list_RM = []
        self.app_list_GM = self.getList(QPushButton, self.widget, self.app_list_GM)
        self.app_list_RM = self.getList(QPushButton, self.widget_3, self.app_list_RM)
        self.pushButton_15.clicked.connect(self.setting_open)
        self.pushButton_12.clicked.connect(self.setting_open)
        self.pushButton_13.clicked.connect(self.quit_app)
        self.pushButton_14.clicked.connect(self.min_window)
        self.pushButton_11.clicked.connect(self.Run)
        self.banana.hide()
        self.banana_2.hide()
        self.banana_3.hide()
        self.banana_4.hide()
        self.banana_5.hide()
        self.banana_6.hide()
        self.banana_7.hide()
        self.progressBar.hide()
        self.Pro.hide()
        for i in self.index_button:
            i.installEventFilter(self)
        """for i2 in self.app_list_GM + self.app_list_RM:
            print(f"self.{i2.objectName()}.clicked.connect(lambda: self.current_button(self.{i2.objectName()}, self.cu_app))")"""
        self.SR.clicked.connect(lambda: self.current_button(self.SR, self.cu_app))
        self.GEN.clicked.connect(lambda: self.current_button(self.GEN, self.cu_app))
        self.HK3.clicked.connect(lambda: self.current_button(self.HK3, self.cu_app))
        self.KSP.clicked.connect(lambda: self.current_button(self.KSP, self.cu_app))
        self.OBSG.clicked.connect(lambda: self.current_button(self.OBSG, self.cu_app))
        self.Kun2.clicked.connect(lambda: self.current_button(self.Kun2, self.cu_app))
        self.RtRES.clicked.connect(lambda: self.current_button(self.RtRES, self.cu_app))
        if self.setting_param['游戏启动器背景']:
            self.screenSetting.checkBox_15.setChecked(True)
        if self.setting_param['统一启动器背景']:
            self.screenSetting.checkBox_14.setChecked(True)
        if self.setting_param['游戏启动器背景'] and self.setting_param['统一启动器背景']:
            self.bg_changes(self.setting_param['游戏启动器背景路径'])
        self.screenSetting.checkBox_15.clicked.connect(self.bg_cus)
        self.screenSetting.checkBox_14.clicked.connect(self.bg_cus_ONES)
        self.screenSetting.pushButton_24.clicked.connect(self.bg_file)
        self.screenSetting.label_51.setText(self.setting_param['游戏启动器背景路径'])
        self.screenSetting.sure.clicked.connect(self.save_setting)
        self.widget_5.hide()
        self.widget_6.hide()
        try:
            self.open.label_5.setText("正在检查游戏文件")
            QApplication.processEvents()
            self.SRG.gameFile_load()
            print(self.open.label_5.text())
            self.GES.gameFile_load()
            self.BH3S.gameFile_load()
            self.KSP2.gameFile_load()
            while self.time < 1000000:
                self.time += 1
                QApplication.processEvents()
            self.time = 0
        except:
            pass
        if self.types == V_RtGL_enum.GM:
            self.cu_app = self.app_list_GM[0]
        else:
            self.cu_app = self.app_list_RM[0]
        self.current_button(self.cu_app)
        self.isPress = False
        try:
            self.open.label_5.setText("正在检查游戏更新")
            self.GES.background_imageUpdate()
            self.GES.game_resourcesUpdate()
            while self.time < 1000000:
                self.time += 1
                QApplication.processEvents()
        except:
            pass

        self.show()
        self.open.close()

    @staticmethod
    def quit_app():
        sys.exit()

    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton:
                self.isPress = True
                self.before_pos = event.globalPos() - self.pos()
                event.accept()
        except Exception as e:
            pass

    def mouseMoveEvent(self, event2):
        if self.isPress and Qt.LeftButton and self.Head.underMouse():
            self.move(event2.globalPos() - self.before_pos)
            event2.accept()

    def mouseReleaseEvent(self, event3):
        self.isPress = False

    def min_window(self):
        self.setWindowState(Qt.WindowMinimized)

    def Run(self):
        if self.pushButton_11.text() == "开始♂游戏":
            if self.cu_app == self.SR:
                self.SRG.gameStart(self.SRG.start_file)
            elif self.cu_app == self.GEN:
                self.GES.gameStart(self.GES.start_file)
            elif self.cu_app == self.HK3:
                self.BH3S.gameStart(self.BH3S.start_file)
            elif self.cu_app == self.KSP:
                self.KSP2.gameStart(self.KSP2.start_file)
        elif self.pushButton_11.text() == "更新♂游戏":
            if self.cu_app == self.SR:
                pass
            elif self.cu_app == self.GEN:
                try:
                    self.progressBar.show()
                    self.Pro.show()
                    self.GES.update_resources(self.progressBar, self.Pro)
                    self.GES.deleteResources()
                    self.progressBar.hide()
                    self.Pro.hide()
                except Exception as e:
                    print(e)
            elif self.cu_app == self.HK3:
                pass
            elif self.cu_app == self.KSP:
                pass

    def eventFilter(self, wt: 'QObject', event: 'QEvent'):
        if wt in self.index_button:
            source = self.index_button.index(wt)
            if event.type() == QEvent.Enter:
                # print(event.type())
                self.index_banana[source].show()
            elif event.type() == QEvent.Leave:
                self.index_banana[source].hide()
            return False
        elif wt in self.app_list_GM + self.app_list_RM:
            self.current_button(wt, self.cu_app)
            return False
        else:
            return True

    @staticmethod
    def getList(types, father: QWidget, rt_list):
        a = father.children()
        for i in a:
            if type(i) is types:
                # print(i.objectName())
                rt_list.append(i)
        return rt_list

    def bg_changes(self, file):
        self.label_3.setPixmap(QPixmap(file))
        self.label_3.setScaledContents(True)

    def current_button(self, isActive: QPushButton, disActive: QPushButton = None):
        if disActive is not None:
            disActive.setCheckable(False)
            disActive.setChecked(False)
            disActive.setEnabled(True)
            self.cu_app = isActive
        isActive.setCheckable(True)
        isActive.setChecked(True)
        isActive.setEnabled(False)
        try:
            if self.pushButton.text() != "开始♂游戏":
                self.pushButton_11.setText("开始♂游戏")
            if isActive == self.SR:
                if self.SRG.head == "":
                    raise ValueError
                if not (self.setting_param['游戏启动器背景'] and self.setting_param['统一启动器背景']):
                    self.bg_changes(self.SRG.bg)
                self.label_4.setText(self.SRG.name)
                self.label_5.setText(self.SRG.ves)
                if self.SRG.isUpdate:
                    self.pushButton_11.setText("更新♂游戏")
            elif isActive == self.GEN:
                if self.GES.head == "":
                    raise ValueError
                if not (self.setting_param['游戏启动器背景'] and self.setting_param['统一启动器背景']):
                    self.bg_changes(self.GES.bg)
                self.label_4.setText(self.GES.name)
                self.label_5.setText(self.GES.ves)
                if self.GES.isUpdate:
                    self.pushButton_11.setText("更新♂游戏")
            elif isActive == self.HK3:
                if self.BH3S.head == "":
                    raise ValueError
                if not (self.setting_param['游戏启动器背景'] and self.setting_param['统一启动器背景']):
                    self.bg_changes(self.BH3S.bg)
                self.label_4.setText(self.BH3S.name)
                self.label_5.setText(self.BH3S.ves)
                if self.BH3S.isUpdate:
                    self.pushButton_11.setText("更新♂游戏")
            elif isActive == self.KSP:
                self.label_4.setText(self.KSP2.name)
                self.label_5.setText("0.12.0")
        except Exception as e:
            print(e)
            if isActive == self.SR:
                self.SRG.gameFile_save(QFileDialog.getExistingDirectory())
                self.SRG.gameFile_load()
                if not (self.setting_param['游戏启动器背景'] and self.setting_param['统一启动器背景']):
                    self.bg_changes(self.SRG.bg)
                self.label_4.setText(self.SRG.name)
            elif isActive == self.GEN:
                self.GES.gameFile_save(QFileDialog.getExistingDirectory())
                self.GES.gameFile_load()
                if not (self.setting_param['游戏启动器背景'] and self.setting_param['统一启动器背景']):
                    self.bg_changes(self.GES.bg)
                self.label_4.setText(self.GES.name)
            elif isActive == self.HK3:
                self.BH3S.gameFile_save(QFileDialog.getExistingDirectory())
                self.BH3S.gameFile_load()
                if not (self.setting_param['游戏启动器背景'] and self.setting_param['统一启动器背景']):
                    self.bg_changes(self.BH3S.bg)
                self.label_4.setText(self.BH3S.name)
            elif isActive == self.KSP:
                self.KSP2.gameFile_save(QFileDialog.getExistingDirectory())
                self.KSP2.gameFile_load()
                self.label_4.setText(self.KSP2.name)

    def setting_open(self):
        self.screenSetting.show()
        self.screenSetting.label_14.setText(self.SRG.start_file)
        self.screenSetting.label_15.setText(self.GES.start_file)
        self.screenSetting.label_17.setText(self.BH3S.start_file)
        self.screenSetting.label_22.setText(self.KSP2.start_file)

    def bg_cus(self):
        if self.screenSetting.checkBox_15.isChecked():
            self.setting_param['游戏启动器背景'] = True
        else:
            self.setting_param['游戏启动器背景'] = False

    def bg_cus_ONES(self):
        if self.screenSetting.checkBox_14.isChecked():
            self.setting_param['统一启动器背景'] = True
        else:
            self.setting_param['统一启动器背景'] = False

    def bg_file(self):
        try:
            self.setting_param['游戏启动器背景路径'] = QFileDialog.getOpenFileName()[0]
            print(self.setting_param['游戏启动器背景路径'])
            self.screenSetting.label_51.setText(self.setting_param['游戏启动器背景路径'])
        except Exception as e:

            print(e)

    def bg_dir(self):
        pass

    def save_setting(self):
        with open("setting.json", "w", encoding="utf-8") as f:
            GM.js.dump(self.setting_param, f)
        self.screenSetting.quit1()
        self.current_button(self.cu_app)
        if self.setting_param['游戏启动器背景'] and self.setting_param['统一启动器背景']:
            self.bg_changes(self.setting_param['游戏启动器背景路径'])


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        sc1 = V_RtGL_app()
        app.exec()
    except Exception as e:
        raise e
