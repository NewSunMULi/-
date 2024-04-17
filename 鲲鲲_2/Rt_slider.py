"""爬虫代码部分"""
import json as js
import os
import re
import time
from PyQt5.QtWidgets import QProgressBar
import urllib.parse as up
from enum import Enum
from random import randint
import requests as rt
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip


class Mode(Enum):
    """
    枚举变量及作用\n
    KWY_WORD = 0 根据关键词爬虫\n
    URL = 1 直接爬取指定网址\n
    BV_TID = 2 根据BV/抖音号/ID号指定爬虫\n
    AUTO = 3 根据输入内容自动选择模式爬虫
    """
    KWY_WORD = 0
    URL = 1
    BV_TID = 2
    AUTO = 3
    RID = 4


class 下载模式(Enum):
    高画质 = 0
    中上画质 = 1
    中下画质 = 2
    低画质 = 3


class bilibili_slider:
    def __init__(self):
        self.headers = None
        self.mode = None
        self.keyword = ""
        self.url = "https://search.bilibili.com/all?keyword="
        self.final = []
        self.title = []
        self.hd = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': 'buvid3=299621CC-A119-751D-470A-5C5573F639EF01380infoc; b_n'
                      'ut=1683093801; i-wanna-go-back=-1; _uuid=4A6659D1-86BF-A9CC-D4'
                      '36-751069435B1AA02014infoc; FEED_LIVE_VERSION=V8; buvid4=D99'
                      'C173C-E250-DDC1-322B-072F2B237C1C02551-023050314-66oZKeNXDmoWx'
                      'vEmvo6mIQ%3D%3D; CURRENT_FNVAL=4048; nostalgia_conf=-1; CURREN'
                      'T_PID=3deaaa90-e978-11ed-90d9-d5849478db70; rpdid=|(umRmY)|Jkm'
                      '0J\'uY)J|mJ)u~; fingerprint=2bbd3eeadd934e6395558a9f3d0ba508; buvid_fp_plain=undefined; DedeU'
                      'serID=352003965; DedeUserID__ckMd5=baca4998f69081c0; SESSDATA=5b32eea0%2C1698645843%2C17971%2A52;'
                      ' bili_jct=ecbfdc82ff84001ca3e3bdb967cf7c96; sid=72azu753; b_ut=5; header_theme_version=CLOSE; h'
                      'ome_feed_column=5; browser_resolution=1920-968; b_lsid=5C511984_189777BE4BF; buvid_fp=c157864006f'
                      '1877fd1475d29ca438e58; bp_video_offset_352003965=820736553414295600; PVID=4',
            'origin': 'https://search.bilibili.com',
            'referer': f'https://search.bilibili.com/all?keyword={up.quote(self.keyword)}',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }
        self.hd2 = {
            'referer': 'https://www.bilibili.com/video',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
        }

    def get(self) -> None:
        """
        :return: 无
        """
        #print(self.mode)
        if self.mode == Mode.URL or (self.keyword[0:4] == "http" and self.mode == Mode.AUTO):
            self.final.append(self.keyword)
        elif self.mode == Mode.BV_TID or (self.keyword[0:1] == "BV" and self.mode == Mode.AUTO):
            self.final.append("https://www.bilibili.com/video/" + self.keyword)
        else:
            if self.headers is None:
                list1_text = rt.get(url=self.url + up.quote(self.keyword), headers=self.hd).text
            else:
                list1_text = rt.get(url=self.url + up.quote(self.keyword), headers=self.headers).text
            before1 = None
            before2 = None
            for i in re.findall(r'www.bilibili.com/video/(.*?)/', list1_text):
                if i != before1:
                    self.final.append("https://www.bilibili.com/video/" + i)
                    before1 = i
            for i in re.findall(r'<h3 class="bili-video-card__info--tit" title="(.*?)"', list1_text):
                #print(i)
                if i != before2:
                    self.title.append(i)
                    before2 = i
            #print(self.title)

    def find(self, url=None):
        """

        :param url: 地址，单个模式游戏
        :return: 具体视频地址
        """
        bi = rt.get(url, headers=self.hd2)
        title = re.findall('<meta data-vue-meta="true" itemprop="name" name="title" content=(.*?)>', bi.text)
        anchor = re.findall('<meta data-vue-meta="true" itemprop="author" name="author" content=(.*?)>', bi.text)
        title = title[0][-len(title[0]) + 1:-15]
        try:
            anchor = anchor[0][-len(title[0]) + 2:-1]
        except:
            anchor = anchor[0]
        res = re.findall("<script>window\.__playinfo__=(.*?)</script>", bi.text)[0]
        data = js.loads(res)
        time1 = data['data']['timelength']
        au_list = []
        vd_list = []
        for i in range(3):
            try:
                au_list.append(data['data']['dash']['audio'][i]['baseUrl'])
                vd_list.append(data['data']['dash']['video'][i * 3]['base_url'])
            except IndexError:
                pass
        return {"title": title, "anchor": anchor, "time": time1}, au_list, vd_list

    def download(self, 文件名称, url_a=None, url_v=None, mode="VA", print_way="PQ", 进度条: QProgressBar = None,
                 **kwargs):
        """

        :param 进度条: PyQt5进度条
        :param print_way: 输出容器默认为qt5进度条
        :param url_v: 视频链接列表-视频
        :param 文件名称: 文件的名字
        :param url_a: 视频链接列表-音频
        :param mode: "VA有声视频", "V"无声视频, "A"纯音频
        :return: 文件
        :param kwargs: 如果需要视频，必须给定参数:"画质=下载模式.XX",否则保修失效，只要音频的话不必给此参数
        """
        if (mode == "V" or mode == "VA") or url_v is not None:
            with rt.get(url_v, headers=self.hd2, stream=True) as s, open(文件名称[:-3] + ".mp4", 'wb') as file:
                dt = 0
                total = int(s.headers.get("content-length", 0))
                times = 0
                now = 0
                d_byte = 0
                if print_way == "PQ":
                    kwargs["Qt进度条"].setMaximum(total)

                for data in s.iter_content(chunk_size=1024 * 1024 * 3):
                    if times == 0:
                        dt = time.time()
                    times += 1
                    size = file.write(data)
                    now += size
                    d_byte += size
                    if print_way == "PQ":
                        进度条.setValue(进度条.value() + size)
                    else:
                        # print(f"download-audio:{round(now / 1024 / 1024, 2)}MB/{round(total / 1024 / 1024, 2)}MB")
                        if time.time() - dt >= 0.02:
                            v = round(d_byte / (time.time() - dt) / 1024 / 1024, 2)
                            print(f"vd_v={v}MB/S, \ntime:{round((total - now) / 1024 / 1024 / v, 3)}s")
                            times = 0
                            d_byte = 0
        if (mode == "A" or mode == "VA") or url_a is not None:
            with rt.get(url_a, headers=self.hd2, stream=True) as s, open(文件名称[:-3] + ".mp3", 'wb') as file:
                dt = 0
                total = int(s.headers.get("content-length", 0))
                times = 0
                now = 0
                d_byte = 0
                if print_way == "PQ":
                    kwargs["Qt进度条"].setMaximum(total)
                for data in s.iter_content(chunk_size=1024):
                    if times == 0:
                        dt = time.time()
                    times += 1
                    size = file.write(data)
                    now += size
                    d_byte += size
                    if print_way == "PQ":
                        进度条.setValue(进度条.value() + size)
                    else:
                        # print(f"download-audio:{round(now / 1024 / 1024, 2)}MB/{round(total / 1024 / 1024, 2)}MB")
                        if time.time() - dt >= 0.02:
                            v = round(d_byte / (time.time() - dt) / 1024 / 1024, 2)
                            print(f"ad_v={v}MB/S,\ntime:{round((total - now) / 1024 / 1024 / v, 3)}s")
                            times = 0
                            d_byte = 0
        if mode == "VA":
            ad = AudioFileClip(文件名称[:-3] + ".mp3")
            vd = VideoFileClip(文件名称[:-3] + ".mp4")
            MP42 = vd.set_audio(ad)
            MP42.write_videofile(f'{文件名称}.mp4')
            try:
                os.remove(文件名称[:-3] + ".mp3")
                os.remove(文件名称[:-3] + ".mp4")
            except:
                time.sleep(10)
                os.remove(文件名称[:-3] + ".mp3")
                os.remove(文件名称[:-3] + ".mp4")


if __name__ == "__main__":
    q = bilibili_slider()
    q.keyword = input("关键词")
    q.get()
    fx = q.final
    number = q.find(fx[0])
    q.download("C:\\Users\\Administrator\\Desktop\\kk2", number[1][0], number[2][0], print_way="other")
