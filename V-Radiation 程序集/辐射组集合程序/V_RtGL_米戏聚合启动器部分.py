import enum
import json as js
import os
import subprocess
from dataclasses import dataclass
from pprint import pprint
from typing import Optional
import requests as rt
import configparser as cf
from PyQt5.QtWidgets import QProgressBar, QLabel, QApplication
import tqdm as td


class Game_launcher:
    def __init__(self):
        self.bg = None
        self.cof = None
        self.ves = None
        self.isUpdate = False

    @staticmethod
    def gameFile_save(road: str = None, gameName=None):
        with open(f"game_file_{gameName}.vtg", "wb") as f:
            f.write(road.encode('utf-8'))

    @staticmethod
    def gameFile_load(gameName):
        with open(f"game_file_{gameName}.vtg", "rb") as f:
            return (f.read()).decode('utf-8')

    @staticmethod
    def gameStart(road):
        print(road)
        subprocess.Popen(road, shell=True)

    def loadconfig(self, road):
        self.cof = cf.ConfigParser()
        try:
            self.cof.read(road, "utf-8")
        except Exception as error1:
            return "读取失败：" + error1.__str__()


class Mihoyo_Setting(enum.Enum):
    official = 1
    bilibili = 14


@dataclass
class Genshin_params_res:
    """key: 键\n
        launcher_id: 语言代码默认18\n
        channel_id:服务器参数 官服1 B站服14 国际服18\n
        sub_channel_id: 子渠道可选 没啥用
        """
    key: str
    launcher_id: float
    channel_id: Optional[float] = None
    sub_channel_id: Optional[float] = None


@dataclass
class Genshin_params_content:
    """key: 键\n
    language: 语言，默认中文zh-cn\n
    launcher_id: 语言代码默认18\n
    filter_adv:可选参数默认false
    """
    key: str
    language: str
    launcher_id: float
    filter_adv: Optional[str] = None


class Star_Rail(Game_launcher):
    def __init__(self):
        super().__init__()
        self.start_file = "/Game/StarRail.exe"
        self.head = ""
        self.name = "蕉坏：性穷铁蛋"

    @staticmethod
    def gameFile_save(road: str = None, **kwargs):
        """

        :param road:
        :param kwargs:
        :return:
        """
        with open(f"game_file_SR.vtg", "wb") as f:
            f.write(road.encode('utf-8'))

    def gameFile_load(self, **kwargs):
        with open(f"game_file_SR.vtg", "rb") as f:
            self.head = (f.read()).decode('utf-8')
            self.start_file = self.head + self.start_file
            self.bg = self.head + "/bg/" + os.listdir(self.head + "/bg")[0]
            self.loadconfig(self.head + "/Game/config.ini")
            self.ves = self.cof.get('General', 'game_version')


class BH3(Game_launcher):
    def __init__(self):
        super().__init__()
        self.start_file = "/Games/BH3.exe"
        self.head = ""
        self.name = "蕉♂坏三 2"

    @staticmethod
    def gameFile_save(road: str = None, **kwargs):
        with open(f"game_file_BH3.vtg", "wb") as f:
            f.write(road.encode('utf-8'))

    def gameFile_load(self, **kwargs):
        with open(f"game_file_BH3.vtg", "rb") as f:
            self.head = (f.read()).decode('utf-8')
            self.start_file = self.head + self.start_file
            self.bg = self.head + "/bg/" + os.listdir(self.head + "/bg")[0]
            self.loadconfig(self.head + "/Games/config.ini")
            self.ves = self.cof.get('General', 'game_version')


class Genshin_Impact(Game_launcher):
    def __init__(self):
        super().__init__()
        self.start_file = "/Genshin Impact Game/YuanShen.exe"
        self.head = ""
        self.name = "蕉♂神"
        self.mifayo_api = "https://sdk-static.mihoyo.com/hk4e_cn/mdk/launcher/api/"
        self.key = "eYd89JmJ"
        self.resData = None
        self.postDate = None

    @staticmethod
    def gameFile_save(road: str = None, **kwargs):
        with open(f"game_file_GE.vtg", "wb") as f:
            f.write(road.encode('utf-8'))

    def gameFile_load(self, **kwargs):
        with open(f"game_file_GE.vtg", "rb") as f:
            self.head = (f.read()).decode('utf-8')
            self.start_file = self.head + self.start_file
            self.bg = self.head + "/bg/" + os.listdir(self.head + "/bg")[0]
            self.loadconfig(self.head + "/Genshin Impact Game/config.ini")
            self.ves = self.cof.get('General', 'game_version')

    def background_imageUpdate(self):
        """
        :return: 如需更新则自动更新并更换图片，反之无操作

        检查游戏 原神 的版本背景图片是否需要更新
        """
        self.postDate = js.loads(rt.get(url=self.mifayo_api + "content",
                                        params=Genshin_params_content(self.key, 'zh-cn', 18, "false").__dict__).text)
        if len(os.listdir(self.head + "/bg")) == 0 or self.postDate['data']['adv']['background'].split("/")[-1] != \
                os.listdir(self.head + "/bg")[0]:
            print("图片文件未更新，正在更新中")
            with open(self.head + "/bg/" + self.postDate['data']['adv']['background'].split("/")[-1], "wb") as f:
                f.write(rt.get(self.postDate['data']['adv']['background']).content)
            self.bg = self.head + "/bg/" + self.postDate['data']['adv']['background'].split("/")[-1]

    def game_resourcesUpdate(self):
        """
        :return: 是否需要更新 bool 值

        检查游戏 原神 是否需要进行游戏资源的更新
        """
        self.resData = js.loads(
            rt.get(url=self.mifayo_api + "resource", params=Genshin_params_res(self.key, 18, 1, 1).__dict__).text)[
            "data"]
        if self.ves != self.resData['game']['latest']['version']:
            self.isUpdate = True
        else:
            self.isUpdate = False

    def update_resources(self, QProcess: QProgressBar = None, QLabels: QLabel = None):
        """

        :param QProcess: Qt进度条组件 可不加
        :param QLabels: Qt标签组件 如果使用Qt进度条，这个参数必须填！ 反之不用填
        :return: 无

        执行游戏 原神 游戏资源更新操作
        """
        if self.isUpdate and self.resData is not None:
            if QProcess is None:
                with rt.get(self.resData['game']['diffs'][0]['path'], stream=True) as s, open(
                        "E:Genshin Impact/Genshin Impact Game/" + self.resData['game']['diffs'][0]['name'],
                        'wb') as file, td.tqdm(
                    desc="E:Genshin Impact/Genshin Impact Game/" + self.resData['game']['diffs'][0]['name'],
                    # 文件名
                    total=int(s.headers.get("content-length", 0)),  # 进度
                    unit='B',  # 单位
                    unit_scale=True,  # 认不得
                    unit_divisor=1024,  # 进制
                ) as bar:
                    print("下载游戏本体")
                    for data in s.iter_content(chunk_size=1024):
                        size = file.write(data)
                        bar.update(size)
                with rt.get(self.resData['game']['diffs'][0]['voice_packs'][0]['path'], stream=True) as s, open(
                        "E:Genshin Impact/Genshin Impact Game/" + self.resData['game']['diffs'][0]['voice_packs'][0]['name'],
                        'wb') as file, td.tqdm(
                    desc="E:Genshin Impact/Genshin Impact Game/" + self.resData['game']['diffs'][0]['voice_packs'][0]['name'],
                    # 文件名
                    total=int(s.headers.get("content-length", 0)),  # 进度
                    unit='B',  # 单位
                    unit_scale=True,  # 认不得
                    unit_divisor=1024,  # 进制
                ) as bar:
                    print("下载音频资源")
                    for data in s.iter_content(chunk_size=1024):
                        size = file.write(data)
                        bar.update(size)
            else:
                size_all = 0
                with rt.get(self.resData['game']['diffs'][0]['path'], stream=True) as s, open(
                        "E:Genshin Impact/Genshin Impact Game/" + self.resData['game']['diffs'][0]['name'],
                        'wb') as file:
                    QProcess.setMaximum(int(s.headers.get("content-length", 0)) / 1024 / 1024)
                    for data in s.iter_content(chunk_size=1024):
                        size = file.write(data)
                        size_all += size / 1024 / 1024
                        QProcess.setValue(size_all)
                        QLabels.setText(
                            "下载游戏本体更新[zip]：" + str(int(size_all)) + "MB / " + str(
                                int(int(s.headers.get("content-length", 0)) / 1024 / 1024)) + "MB")
                        QApplication.processEvents()
                with rt.get(self.resData['game']['diffs'][0]['voice_packs'][0]['path'], stream=True) as s, open(
                        "E:Genshin Impact/Genshin Impact Game/" + self.resData['game']['diffs'][0]['voice_packs'][0]['name'],
                        'wb') as file:
                    QProcess.setMaximum(int(s.headers.get("content-length", 0)) / 1024 / 1024)
                    size_all = 0
                    for data in s.iter_content(chunk_size=1024):
                        size = file.write(data)
                        size_all += size / 1024 / 1024
                        QProcess.setValue(size_all)
                        QLabels.setText("下载游戏音频更新[zip]：" + str(int(size_all))  + "MB / " + str(
                            int(int(s.headers.get("content-length", 0)) / 1024 / 1024)) + "MB")
                        QApplication.processEvents()

    def deleteResources(self, QProcess: QProgressBar = None, QLabels: QLabel = None):
        """

        :param QProcess: Qt进度条组件 可不加
        :param QLabels: Qt标签组件 如果使用Qt进度条，这个参数必须填！ 反之不用填
        :return: 无

        执行游戏 原神 游戏废弃资源删除操作
                """
        with open(self.head + r'/Genshin Impact Game/' + "deletefiles.txt", "r", encoding="utf-8") as f:
            try:
                if QProcess is None:
                    for i in f.readlines():
                        os.remove(self.head + r'/Genshin Impact Game/' + i.split("\n")[0])
                        print("delete:" + self.head + r'/Genshin Impact Game/' + i.split("\n")[0])
                    print("files have deleted")
                else:
                    QProcess.setMaximum(len(f.readlines()))
                    QProcess.setMinimum(0)
                    QProcess.setValue(0)
                    for i in f.readlines():
                        QLabels.setText(f"正在删除不需要的文件：[{f.readlines().index(i) + 1}]/[{len(f.readlines())}]")
                        os.remove(self.head + r'/Genshin Impact Game/' + i.split("\n")[0])
                        QProcess.setValue(QProcess.value() + 1)
            except Exception as e:
                print("ERROR!" + e.__str__())


class KSP(Game_launcher):
    def __init__(self):
        super().__init__()
        self.start_file = "/KSP_64.exe"
        self.head = ""
        self.name = "坎巴拉太空计划"

    @staticmethod
    def gameFile_save(road: str = None, **kwargs):
        with open(f"game_file_KSP.vtg", "wb") as f:
            f.write(road.encode('utf-8'))

    def gameFile_load(self, **kwargs):
        with open(f"game_file_KSP.vtg", "rb") as f:
            self.head = (f.read()).decode('utf-8')
            self.start_file = self.head + self.start_file


if __name__ == "__main__":
    a = Game_launcher()
    a.gameFile_save("这个大傻逼", "蕉神")
    print(a.gameFile_load("蕉神"))
