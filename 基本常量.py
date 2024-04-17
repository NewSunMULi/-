"""基本常量"""
import json as js
from typing import List, AnyStr
from enum import Enum  # 进口枚举类型，刚学的C#要学会运用呀 ^_^

# 注释死都不用马语
"""一些常量"""
列表 = List
所有字符 = AnyStr
x, y = 800, 600
信息 = ["昵称", "出生年月", "作品", "最近使用"]
检索 = ["账号", "密码", "昵称", "认证", "资料"]
斜体 = "italic"
加粗 = "bold"
大小 = f"{x}x{y}+300+150"
华体 = "华光钢铁直黑 可变体 Bold"
统一码 = "utf-8"
原神字体 = "汉仪文黑-85W Heavy"

"""一些数据"""
with open('账号.json', "r", encoding="utf-8") as f:
    user_list = js.load(f)
with open('密码.json', "r", encoding="utf-8") as f:
    user_password = js.load(f)
with open('昵称.json', "r", encoding="utf-8") as f:
    user_name = js.load(f)
with open('认证.json', "r", encoding="utf-8") as f:
    ID = js.load(f)
# with open('头像.json', "r", encoding="utf-8") as f:
# 头像: 列表[所有字符] = js.load(f)
with open('资料.json', "r", encoding="utf-8") as f:
    个人资料: 列表[所有字符] = js.load(f)
with open("WST.json", "r", encoding="utf-8") as f:
    WST = js.load(f)
with open("RTY.json", "r", encoding="utf-8") as f:
    RTY = js.load(f)


def 打包exe(file=None, icon图标路径="图标.ico", 黑屏=False):
    import os
    if 黑屏:
        os.system(f"pyinstaller -F -i {icon图标路径} -F {file}")
    else:
        os.system(f"pyinstaller -w -i {icon图标路径} -F {file}")


class 玄氏评级:
    def __init__(self):
        pass

    @staticmethod
    def 化学评级(分数=0):
        class 评级(Enum):
            SL_Y = 95
            VRT_C_W = 94
            JK_Z = 90
            Cxk_G = 85
            Dog_H = 90
            DK_E = 89
            MIN = 90
            Dc_GH = 100
            DJ_HZ = 110
            CJ_K = 115
            Dcz_GHK = 117
            VCT_CLS1 = 120

        if 评级.Dog_H.value > 分数 or 分数 < 评级.MIN.value:
            return 评级.DK_E

        elif 分数 >= 评级.SL_Y.value:
            return 评级.SL_Y

        elif 评级.Dog_H.value == 评级.Cxk_G.value and 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
            return 评级.Dc_GH

        elif 评级.Dog_H.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.DJ_HZ

        elif 评级.Cxk_G.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.CJ_K

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z and 分数 < 评级.VRT_C_W.value:
            return 评级.Dcz_GHK

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z == 评级.VRT_C_W:
            return 评级.VRT_cls1

        else:
            if 评级.Dog_H.value <= 分数 < 评级.Cxk_G.value:
                return 评级.Dog_H

            elif 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
                return 评级.Cxk_G

            elif 评级.JK_Z.value <= 分数 < 评级.VRT_C_W.value:
                return 评级.JK_Z

            else:
                return 评级.VRT_C_W

    @staticmethod
    def 生物评级(分数=0):
        class 评级(Enum):
            DK_E = 75
            Dog_H = 90
            Cxk_G = 85
            JK_Z = 90
            VRT_C_W = 98
            SL_Y = 99
            MAX = 100
            MIN = 75
            Dc_GH = 100
            DJ_HZ = 110
            CJ_K = 115
            Dcz_GHK = 117
            VCT_CLS1 = 120

        if 评级.Dog_H.value > 分数 or 分数 < 评级.MIN.value:
            return 评级.DK_E

        elif 分数 >= 评级.MAX.value:
            return 评级.SL_Y

        elif 评级.Dog_H.value == 评级.Cxk_G.value and 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
            return 评级.Dc_GH

        elif 评级.Dog_H.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.DJ_HZ

        elif 评级.Cxk_G.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.CJ_K

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z and 分数 < 评级.VRT_C_W.value:
            return 评级.Dcz_GHK

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z == 评级.VRT_C_W:
            return 评级.VRT_cls1

        else:
            if 评级.Dog_H.value <= 分数 < 评级.Cxk_G.value:
                return 评级.Dog_H

            elif 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
                return 评级.Cxk_G

            elif 评级.JK_Z.value <= 分数 < 评级.VRT_C_W.value:
                return 评级.JK_Z

            else:
                return 评级.VRT_C_W

    @staticmethod
    def 物理评级(分数=0):
        class 评级(Enum):
            DK_E = 75
            Dog_H = 90
            Cxk_G = 85
            JK_Z = 90
            VRT_C_W = 98
            SL_Y = 99
            MAX = 100
            MIN = 75
            Dc_GH = 100
            DJ_HZ = 110
            CJ_K = 115
            Dcz_GHK = 117
            VCT_CLS1 = 120

        if 评级.Dog_H.value > 分数 or 分数 < 评级.MIN.value:
            return 评级.DK_E

        elif 分数 >= 评级.MAX.value:
            return 评级.SL_Y

        elif 评级.Dog_H.value == 评级.Cxk_G.value and 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
            return 评级.Dc_GH

        elif 评级.Dog_H.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.DJ_HZ

        elif 评级.Cxk_G.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.CJ_K

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z and 分数 < 评级.VRT_C_W.value:
            return 评级.Dcz_GHK

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z == 评级.VRT_C_W:
            return 评级.VRT_cls1

        else:
            if 评级.Dog_H.value <= 分数 < 评级.Cxk_G.value:
                return 评级.Dog_H

            elif 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
                return 评级.Cxk_G

            elif 评级.JK_Z.value <= 分数 < 评级.VRT_C_W.value:
                return 评级.JK_Z

            else:
                return 评级.VRT_C_W

    @staticmethod
    def 语文评级(分数=0):
        class 评级(Enum):
            DK_E = 75
            Dog_H = 90
            Cxk_G = 85
            JK_Z = 90
            VRT_C_W = 98
            SL_Y = 99
            MAX = 100
            MIN = 75
            Dc_GH = 100
            DJ_HZ = 110
            CJ_K = 115
            Dcz_GHK = 117
            VCT_CLS1 = 120

        if 评级.Dog_H.value > 分数 or 分数 < 评级.MIN.value:
            return 评级.DK_E

        elif 分数 >= 评级.MAX.value:
            return 评级.SL_Y

        elif 评级.Dog_H.value == 评级.Cxk_G.value and 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
            return 评级.Dc_GH

        elif 评级.Dog_H.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.DJ_HZ

        elif 评级.Cxk_G.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.CJ_K

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z and 分数 < 评级.VRT_C_W.value:
            return 评级.Dcz_GHK

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z == 评级.VRT_C_W:
            return 评级.VRT_cls1

        else:
            if 评级.Dog_H.value <= 分数 < 评级.Cxk_G.value:
                return 评级.Dog_H

            elif 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
                return 评级.Cxk_G

            elif 评级.JK_Z.value <= 分数 < 评级.VRT_C_W.value:
                return 评级.JK_Z

            else:
                return 评级.VRT_C_W

    @staticmethod
    def 数学评级(分数=0):
        class 评级(Enum):
            DK_E = 75
            Dog_H = 90
            Cxk_G = 85
            JK_Z = 90
            VRT_C_W = 98
            SL_Y = 99
            MAX = 100
            MIN = 75
            Dc_GH = 100
            DJ_HZ = 110
            CJ_K = 115
            Dcz_GHK = 117
            VCT_CLS1 = 120

        if 评级.Dog_H.value > 分数 or 分数 < 评级.MIN.value:
            return 评级.DK_E

        elif 分数 >= 评级.MAX.value:
            return 评级.SL_Y

        elif 评级.Dog_H.value == 评级.Cxk_G.value and 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
            return 评级.Dc_GH

        elif 评级.Dog_H.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.DJ_HZ

        elif 评级.Cxk_G.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.CJ_K

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z and 分数 < 评级.VRT_C_W.value:
            return 评级.Dcz_GHK

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z == 评级.VRT_C_W:
            return 评级.VRT_cls1

        else:
            if 评级.Dog_H.value <= 分数 < 评级.Cxk_G.value:
                return 评级.Dog_H

            elif 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
                return 评级.Cxk_G

            elif 评级.JK_Z.value <= 分数 < 评级.VRT_C_W.value:
                return 评级.JK_Z

            else:
                return 评级.VRT_C_W

    @staticmethod
    def 鸟语评级(分数=0):
        class 评级(Enum):
            DK_E = 75
            Dog_H = 90
            Cxk_G = 85
            JK_Z = 90
            VRT_C_W = 98
            SL_Y = 99
            MAX = 100
            MIN = 75
            Dc_GH = 100
            DJ_HZ = 110
            CJ_K = 115
            Dcz_GHK = 117
            VCT_CLS1 = 120

        if 评级.Dog_H.value > 分数 or 分数 < 评级.MIN.value:
            return 评级.DK_E

        elif 分数 >= 评级.MAX.value:
            return 评级.SL_Y

        elif 评级.Dog_H.value == 评级.Cxk_G.value and 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
            return 评级.Dc_GH

        elif 评级.Dog_H.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.DJ_HZ

        elif 评级.Cxk_G.value == 评级.JK_Z.value and 评级.VRT_C_W.value > 分数 >= 评级.JK_Z.value:
            return 评级.CJ_K

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z and 分数 < 评级.VRT_C_W.value:
            return 评级.Dcz_GHK

        elif 评级.Dog_H == 评级.Cxk_G == 评级.JK_Z == 评级.VRT_C_W:
            return 评级.VRT_cls1

        else:
            if 评级.Dog_H.value <= 分数 < 评级.Cxk_G.value:
                return 评级.Dog_H

            elif 评级.Cxk_G.value <= 分数 < 评级.JK_Z.value:
                return 评级.Cxk_G

            elif 评级.JK_Z.value <= 分数 < 评级.VRT_C_W.value:
                return 评级.JK_Z

            else:
                return 评级.VRT_C_W


if __name__ == "__main__":
    打包exe(file=r'"./V-Radiation 程序集/辐射组集合程序/V_RtGL程序.py"')