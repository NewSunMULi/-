"""辐射组管理系统的具体代码"""
import json as 嫁我
from typing import Any
from 功能设置 import *
from 基本常量 import *
from 统计 import 辐射计划5_镜像计划

sc = Tk()
sc.geometry(f"{x}x{y}+300+125")
sc.iconbitmap(bitmap="logo.ico")
list1 = []
list2 = []
list3 = []
active = False
UID = 0000000000
科目代码 = "ch"
可查看 = False
userName = ""
image1 = PhotoImage(file="10WST.gif")
image2 = PhotoImage(file="50WST.gif")
image3 = PhotoImage(file="250WST.gif")
image4 = PhotoImage(file="1250WST.gif")
image5 = PhotoImage(file="1.28RTY.gif")
image6 = PhotoImage(file="2.56RTY.gif")
image7 = PhotoImage(file="3.28RTY.gif")
image8 = PhotoImage(file="6.48RTY.gif")
原神宣传图 = PhotoImage(file="原神.gif")
明日宣传图 = PhotoImage(file="明日之后.gif")
Apex宣传图 = PhotoImage(file="Apex.gif")
方舟宣传图 = PhotoImage(file="明日方舟.gif")
崩三宣传图 = PhotoImage(file="崩坏三.gif")


# 分析背景图片 = PhotoImage(file=None)


def 原神_模拟():
    概率模拟_原神()


def 明日_模拟():
    import 概率模拟_明日之后


class 其余游戏:
    def __init__(self):
        pass

    @staticmethod  # 装饰器
    def Apex_模拟():
        import 概率模拟_Apex

    @staticmethod
    def 明日方舟_模拟():
        import 概率模拟_明日方舟

    @staticmethod
    def 崩三_模拟():
        import 概率模拟_崩坏3


def 辐射组logo(scname: Any = "好兄弟", up_text="放出光芒！"):
    """Logo放这好搞
    同时纪念曾经的年华，虽然它已经过去了
    We will finding your......
    """
    m = Label(scname, text=up_text, font=("华光钢铁直黑 可变体 Bold", 35, "italic"), fg="blue", width=20, anchor="nw")
    m.place(x=25, y=20)  # italic斜体
    g = Label(scname, text="VRt-21", font=("微软雅黑", 20, "italic"), fg="#FF00EF")
    g.place(x=25, y=70)
    return m, g


def 协议():
    if UID != 0:
        辐射组协议(ID=ID[user_list.index(UID)], PASSWORDS=user_password[user_list.index(UID)])
    else:
        辐射组协议()


def 账户财产(用户账号=UID):
    if 用户账号 in user_list:
        if len(list1) != 0:
            for i in list1:
                i.destroy()
        序数 = user_list.index(用户账号)
        wst = WST[序数]

        def 测试():
            """wst调试使用代码，平常就当摆设使用"""
            user_WST.set("你的WST:" + str(wst - 9999))

        user_WST = StringVar(sc)
        WST1 = Button(sc, textvariable=user_WST, bd=0, command=氪金系统)
        user_WST.set("你的WST:" + str(wst))
        WST1.place(x=590, y=570)
        user_RTY = StringVar(sc)
        rty = RTY[序数]
        RTY2 = Button(sc, textvariable=user_RTY, bd=0, command=氪金系统, width=250, anchor="w")
        user_RTY.set("你的RTY:" + str(rty))
        RTY2.place(x=690, y=570)
        list1.append(WST1)
        list1.append(RTY2)
    else:
        if len(list1) != 0:
            for i in list1:
                i.destroy()
        序数 = None
        user_WST = StringVar(sc)
        WST1 = Button(sc, textvariable=user_WST, bd=0, command=氪金系统)
        user_WST.set("未登录无法查看")
        WST1.place(x=590, y=570)
        user_RTY = StringVar(sc)
        RTY2 = Button(sc, textvariable=user_RTY, bd=0, command=氪金系统)
        user_RTY.set("未登录无法查看")
        RTY2.place(x=690, y=570)
        list1.append(WST1)
        list1.append(RTY2)


def 氪金系统():
    def A():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            WST[user_list.index(UID)] += 10
            with open("WST.json", "w", encoding=统一码) as f:
                嫁我.dump(WST, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def B():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            WST[user_list.index(UID)] += 50
            with open("WST.json", "w", encoding=统一码) as f:
                嫁我.dump(WST, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def C():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            WST[user_list.index(UID)] += 250
            with open("WST.json", "w", encoding=统一码) as f:
                嫁我.dump(WST, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def D():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            WST[user_list.index(UID)] += 1250
            with open("WST.json", "w", encoding=统一码) as f:
                嫁我.dump(WST, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def E():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            RTY[user_list.index(UID)] += 2
            with open("RTY.json", "w", encoding=统一码) as f:
                嫁我.dump(RTY, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def F():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            RTY[user_list.index(UID)] += 3
            with open("RTY.json", "w", encoding=统一码) as f:
                嫁我.dump(RTY, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def G():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            RTY[user_list.index(UID)] += 4
            with open("RTY.json", "w", encoding=统一码) as f:
                嫁我.dump(RTY, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    def H():
        if UID not in user_list:
            充值界面.destroy()
            messagebox.showinfo("充值提示", "无账户")
        else:
            RTY[user_list.index(UID)] += 6
            with open("RTY.json", "w", encoding=统一码) as f:
                嫁我.dump(RTY, f)
            账户财产(UID)
            充值界面.destroy()
            messagebox.showinfo("充值提示", "支付成功")

    充值界面 = Toplevel()
    充值界面.geometry(f"{x}x{y}+300+125")
    充值界面.title("充值")
    辐射组logo(充值界面, "充值入口")
    Label(充值界面, text="WTS:功能使用基础货币", font=("", 15)).place(x=30, y=120)
    aa = Button(充值界面, image=image1, bd=0, command=A)
    aa.place(x=10, y=150)
    Label(充值界面, text="10 WST ￥1", font=(华体, 17)).place(x=32, y=280)
    b = Button(充值界面, image=image2, bd=0, command=B)
    b.place(x=210, y=150)
    Label(充值界面, text="50 WST ￥5", font=(华体, 17)).place(x=229, y=280)
    c = Button(充值界面, image=image3, bd=0, command=C)
    c.place(x=410, y=150)
    Label(充值界面, text="250 WST ￥25", font=(华体, 17)).place(x=420, y=280)
    d = Button(充值界面, image=image4, bd=0, command=D)
    d.place(x=610, y=150)
    Label(充值界面, text="1250 WST ￥125", font=(华体, 17)).place(x=605, y=280)

    Label(充值界面, text="RTY:功能使用高级货币", font=("", 15)).place(x=30, y=340)
    e = Button(充值界面, image=image5, bd=0, command=E)
    e.place(x=10, y=370)
    Label(充值界面, text="1.28 RTY  ￥128", font=(华体, 17)).place(x=10, y=500)
    ff = Button(充值界面, image=image6, bd=0, command=F)
    ff.place(x=210, y=370)
    Label(充值界面, text="2.56 RTY ￥256", font=(华体, 17)).place(x=210, y=500)
    g = Button(充值界面, image=image7, bd=0, command=G)
    g.place(x=410, y=370)
    Label(充值界面, text="3.28 RTY ￥328", font=(华体, 17)).place(x=420, y=500)
    h = Button(充值界面, image=image8, bd=0, command=H)
    h.place(x=610, y=370)
    Label(充值界面, text="6.48 RTY ￥648", font=(华体, 17)).place(x=605, y=500)


def 登录和注册():
    global list3
    global active
    sc4 = Tk()

    def 登录():
        global list3
        global userName

        def 检测1(*EN):
            global active
            global userName
            global log
            global UID
            num = userNumber.get()
            pas = userPassword.get()
            if num in user_list:
                if pas not in user_password or user_list.index(num) != user_password.index(pas):
                    a8 = Label(sc4, text="密码错误", width=150, anchor="sw")
                    a8.place(x=375, y=420)
                elif user_list.index(num) == user_password.index(pas):
                    a8 = Label(sc4, text="登陆成功", width=150, anchor="sw")
                    active = True
                    userName = user_name[user_list.index(num)]
                    UID = num
                    log = Button(sc, text=userName, font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=退出登录, width=20,
                                 anchor="w")
                    Label(sc, text="已登录", font=("微软雅黑", 8, 斜体,), fg="green").place(x=660, y=79)
                    Label(sc, text=ID[user_list.index(num)], font=("微软雅黑", 8, 斜体,), fg="green", width=100,
                          anchor="w").place(x=715, y=79)
                    账户财产(UID)
                    log.place(x=659, y=50)
                    a8.place(x=375, y=420)
                    sc4.destroy()
            else:
                a8 = Label(sc4, text="无此账户", width=150, anchor="sw")
                a8.place(x=375, y=420)

        a1 = Label(sc4, text="VRt-21", fg="#F508F0", font=("微软雅黑", 48, 斜体))
        a1.place(x=800 / 2 - 48 * 5 / 2, y=30)
        a2 = Label(sc4, text="登录&注册", fg="#00FFF2", font=("微软雅黑", 24, 斜体))
        a2.place(x=800 / 2 - 48 * 3.75 / 2, y=100)
        a3 = Label(sc4, text="登录", fg="red", font=("微软雅黑", 20))
        a3.place(x=800 / 2 - 48 * 1.5 / 2, y=200)
        a4 = Label(sc4, text="账号(名)", font=("", 10))
        a4.place(x=280, y=250)
        a5 = Label(sc4, text="账户密码", font=("", 10))
        a5.place(x=280, y=290)
        userNumber = Entry(sc4)
        userNumber.place(x=340, y=250)
        userPassword = Entry(sc4, show="*")
        userPassword.place(x=340, y=290)
        userNumber.insert(END, "2802912710")
        userPassword.insert(END, "z555r5555")
        a6 = Button(sc4, text="登录", width=5, command=检测1)
        a6.place(x=380, y=320)
        a7 = Button(sc4, text="没有账号?注册一个", bd=0, command=注册)
        a7.place(x=350, y=360)
        list3 = [a1, a2, a3, a4, a5, a6, a7, userPassword, userNumber]
        sc4.bind("<3>", 检测1)
        sc4.mainloop()

    def 注册():
        global list3

        def 检测2():
            global active
            num = userNumber.get()
            pas = userPassword.get()
            if num not in user_list and len(pas) != 0:
                a8 = Label(sc4, text="注册成功", width=150, anchor="sw")
                user_list.append(num)
                user_password.append(pas)
                user_name.append(num)
                ID.append("普通用户")
                WST.append(0)
                RTY.append(0.0)
                with open("./资料/" + num + ".jk", "w", encoding="utf-8") as f:
                    f.write(f"{num}\n")
                    f.write("N-N-N\n")
                    f.write("欢迎您的到来")
                个人资料.append("./资料/" + num + ".jk")
                a8.place(x=375, y=420)
                临时列表 = [user_list, user_password, user_name, ID, 个人资料, WST, RTY]
                for i in 检索:
                    with open(i + ".json", "w", encoding="utf-8") as f:
                        嫁我.dump(临时列表[检索.index(i)], f)
            elif len(num) != 10:
                a8 = Label(sc4, text="十位数账号", width=150, anchor="sw")
                a8.place(x=370, y=420)
            elif len(pas) == 0:
                a8 = Label(sc4, text="密码呢?", width=150, anchor="sw")
                a8.place(x=375, y=420)
            else:
                a8 = Label(sc4, text="已被注册", width=150, anchor="sw")
                a8.place(x=375, y=420)

        for i in list3:
            i.destroy()
            list3.remove(i)
        a1 = Label(sc4, text="VRt-21", fg="#F508F0", font=("微软雅黑", 48, 斜体))
        a1.place(x=800 / 2 - 48 * 5 / 2, y=30)
        a2 = Label(sc4, text="登录&注册", fg="#00FFF2", font=("微软雅黑", 24, 斜体))
        a2.place(x=800 / 2 - 48 * 3.75 / 2, y=100)
        a3 = Label(sc4, text="注册", fg="red", font=("微软雅黑", 20))
        a3.place(x=800 / 2 - 48 * 1.5 / 2, y=200)
        a4 = Label(sc4, text="账号(名)", font=("", 10))
        a4.place(x=280, y=250)
        a5 = Label(sc4, text="账户密码", font=("", 10))
        a5.place(x=280, y=290)
        userNumber = Entry(sc4)
        userNumber.place(x=340, y=250)
        userPassword = Entry(sc4)
        userPassword.place(x=340, y=290)
        a6 = Button(sc4, text="注册", width=5, command=检测2)
        a6.place(x=380, y=320)
        a7 = Button(sc4, text="注册好了登录", bd=0, command=登录)
        a7.place(x=365, y=360)
        list3 = [a1, a2, a3, a4, a5, a6, a7, userPassword, userNumber]
        sc4.mainloop()

    sc4.title("登录&注册")
    sc4.geometry(f"{x}x{y}+300+150")
    登录()


def 退出登录():
    global UID
    global log

    def 退出():
        global UID
        global log
        UID = 0000000000
        sc5.destroy()
        账户财产(UID)
        log = Button(sc, text="登录", font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=登录和注册, width=300, anchor="w")
        log.place(x=659, y=50)
        Label(sc, text="             ", font=("微软雅黑", 8, 斜体,), fg="green").place(x=660, y=79)
        Label(sc, text="             ", font=("微软雅黑", 8, 斜体,), fg="green", width=100, anchor="w").place(x=720, y=79)

    sc5 = Tk()
    sc5.title("个人资料")
    sc5.geometry(大小)
    Label(sc5, text="个人主页", fg="green", font=(华体, 30, 加粗)).place(x=0, y=30)
    Label(sc5, text="头像：正在制作", font=(华体, 18)).place(x=40, y=100)
    with open(f"{个人资料[user_list.index(UID)]}", "r", encoding="utf-8") as f:
        资料信息 = f.readlines()
    for i in 资料信息:
        Label(sc5, text=f"{信息[资料信息.index(i)]}:{i}", font=(华体, 18)).place(x=40, y=150 + 资料信息.index(i) * 50)
    exit = Button(sc5, text="退出登录", font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=退出)
    exit.pack(side=BOTTOM, anchor="s")


if active:
    log = Button(sc, text=userName, font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=退出登录)
    Label(sc, text="已登录", font=("微软雅黑", 8, 斜体,), fg="green").place(x=660, y=79)
    Label(sc, text=ID, font=("微软雅黑", 8, 斜体,), fg="green").place(x=720, y=79)
else:
    # “bold”加粗、“italic”斜体、“underline”下划线、“overstrike”删除线。
    log = Button(sc, text="登录", font=("华光钢铁直黑 可变体 Bold", 15), bd=0, command=登录和注册)
log.place(x=659, y=50)
账户财产(UID)


class 辐射组管理程序:
    """除了概率模拟其余功能只能让辐射组成员使用"""

    def __init__(self):
        """自动运行的部分"""
        self.控件 = []

    def 首页(self):
        if self.控件 is not None:
            for i in self.控件:
                i.destroy()
            self.控件.clear()
        sc.title("辐射组管理程序--首页")
        Label(sc, text="首页", font=("华光钢铁直黑 可变体 Bold", 35, "italic"), fg="blue", width=20, anchor="sw").place(x=25,
                                                                                                             y=20)
        Label(sc, text="VRt-21", font=("微软雅黑", 20, "italic"), fg="#FF00EF").place(x=25, y=70)
        img1 = PhotoImage(file="概率模拟.gif")
        self.概率 = Button(sc, text="概率模拟", font=("微软雅黑", 15, 斜体), image=img1, compound=CENTER, bd=0,
                         command=self.概率模拟)  # compound图片显示与文字之哪
        self.概率.place(x=70, y=140)
        self.gg = Button(sc, text="免费音乐", font=("微软雅黑", 15, 斜体), image=img1, compound=CENTER, bd=0,
                         command=self.免费音乐)  # compound图片显示与文字之哪
        self.gg.place(x=270, y=140)
        self.协议 = Button(sc, text="辐射组/合作社协议", font=("微软雅黑", 12), bd=0, command=协议)
        self.协议.pack(side=BOTTOM, anchor="center")
        self.计划 = Button(sc, text="规划", font=("微软雅黑", 15, 斜体), image=img1, compound=CENTER, bd=0,
                         command=self.辐射组规划)
        self.计划.place(x=470, y=140)
        self.控件.append(self.计划)
        self.控件.append(self.概率)
        self.控件.append(self.协议)
        self.控件.append(self.gg)
        sc.update()
        sc.bind("<F12>", self.分析评级平台)
        sc.mainloop()

    def 免费音乐(self):
        global sc
        if self.控件 is not None:
            for i in self.控件:
                i.destroy()
            self.控件.clear()
        p, k = 辐射组logo(sc, "免费音乐")
        sc.title("辐射组管理程序--音乐试听与下载")
        q = Label(sc, text="提供音乐的名字或者歌手名字我可以帮你搜点你想听的音乐:", font=("", 15))
        q.place(x=40, y=120)
        key = Entry(sc, width=60)
        key.place(x=40, y=160)
        search = Button(sc, text="搜索", bd=1,
                        command=lambda: tk爬虫_中文版().音乐爬虫(key.get(), None, 初始坐标x=50, 初始坐标y=160, 父容器=sc))
        search.place(x=470, y=157)
        self.上级 = Button(sc, text="返回上一级", font=(华体, 12), fg="#AA00FF", bd=0, command=self.首页)
        self.上级.place(x=550, y=50)
        self.控件.append(self.上级)
        self.控件.append(p)
        self.控件.append(k)
        self.控件.append(q)
        self.控件.append(key)
        self.控件.append(search)

    @staticmethod
    def 分析评级平台(*args):
        global sc
        global 科目代码

        def 统计图表(*jk):
            list11 = []
            注释 = []
            dir_list1 = os.listdir('./成绩')
            for i in dir_list1:
                with open('./成绩/' + i, "r", encoding="utf-8") as f:
                    list11.append(js.load(f))
                    if i[:-5] == "自己":
                        注释.append("yourself")
                    else:
                        注释.append(i[:-5])
            a = 辐射计划5_镜像计划(json文件对象=list11)
            a.图表(eval(f"a.科别数.{科目代码}"), 评级等级=注释)

        def 改变函数(event):
            global 科目代码
            if event.keysym == "F10":
                科目代码 = "ch"
                print("语文")
            elif event.keysym == "F9":
                科目代码 = "mt"
                print("数学")
            elif event.keysym == "F8":
                科目代码 = "ph"
                print("物理")
            elif event.keysym == "F7":
                科目代码 = "ob"
                print("生物")
            elif event.keysym == "F6":
                科目代码 = "chs"
                print("化学")

        """if self.控件 is not None:
            for i in self.控件:
                i.destroy()
            self.控件.clear()"""

        sc5 = Toplevel(sc)
        sc5.geometry("800x600+300+125")
        sc5.title("辐射组管理程序 ---- 分析-评级区")
        can = Canvas(sc5, highlightthickness=0, width=800, height=600)
        can.place(x=0, y=0)
        can.create_text(60, 20, text="欢迎！", font=("", 25))
        with open("./成绩/自己.json", "r", encoding="utf-8") as f3:
            Self = js.load(f3)
        can.create_text(110, 60, text=f"你本次的成绩情况,日期{Self[-1][0][0:4]}年{Self[-1][0][4:6]}月{Self[-1][0][6:]}日")
        with open("./成绩/Dog_H.json", "r", encoding="utf-8") as f4:
            Ds = js.load(f4)
        with open("./成绩/Cxk_G.json", "r", encoding="utf-8") as f5:
            Cs = js.load(f5)
        with open("./成绩/BJK_Z.json", "r", encoding="utf-8") as f6:
            Bs = js.load(f6)
        with open("./成绩/APE_L.json", "r", encoding="utf-8") as f7:
            As = js.load(f7)
        with open("./成绩/SL_Y.json", "r", encoding="utf-8") as f8:
            Ss = js.load(f8)
        ch = can.create_text(90, 80, text=f"语文----{Self[-1][1]},较上一次提升{Self[-1][1]-Self[-2][1]}")
        mt = can.create_text(90, 100, text=f"数学----{Self[-1][2]},较上一次提升{Self[-1][2]-Self[-2][2]}")
        py = can.create_text(90, 120, text=f"物理----{Self[-1][3]},较上一次提升{Self[-1][3]-Self[-2][3]}")
        od = can.create_text(90, 140, text=f"生物----{Self[-1][4]},较上一次提升{Self[-1][4]-Self[-2][4]}")
        cs = can.create_text(90, 160, text=f"化学----{Self[-1][5]},较上一次提升{Self[-1][5]-Self[-2][5]}")
        等级 = can.create_text(100, 180, text=f"综合等级评定----DK E 严重失败!")
        can.create_text(800 - 200, 60, text="本次镜像等级变化:")
        Dog_H = can.create_text(800 - 200, 80,
                                text=f"Dog H等级:语文{Ds[-1][1]}，数学{Ds[-1][2]}，物理{Ds[-1][3]}，生物{Ds[-1][4]}，化学{Ds[-1][5]}")
        Cxk_G = can.create_text(800 - 200, 100,
                                text=f"Cxk G等级:语文{Cs[-1][1]}，数学{Cs[-1][2]}，物理{Cs[-1][3]}，生物{Cs[-1][4]}，化学{Cs[-1][5]}")
        BJK_Z = can.create_text(800 - 200, 120,
                                text=f"BJK Z等级:语文{Bs[-1][1]}，数学{Bs[-1][2]}，物理{Bs[-1][3]}，生物{Bs[-1][4]}，化学{Bs[-1][5]}")
        APE_L = can.create_text(800 - 200, 140,
                                text=f"APE L等级:语文{As[-1][1]}，数学{As[-1][2]}，物理{As[-1][3]}，生物{As[-1][4]}，化学{As[-1][5]}")
        SL_Y = can.create_text(800 - 200, 160,
                               text=f"SL Y等级:语文{Ss[-1][1]}，数学{Ss[-1][2]}，物理{Ss[-1][3]}，生物{Ss[-1][4]}，化学{Ss[-1][5]}")
        can.create_text(80, 570, text="按F11可以查阅统计图表")
        sc5.bind("<F11>", 统计图表)
        sc5.bind("<F10>", 改变函数)
        sc5.bind("<F9>", 改变函数)
        sc5.bind("<F8>", 改变函数)
        sc5.bind("<F7>", 改变函数)
        sc5.bind("<F6>", 改变函数)
        sc5.mainloop()

    def 辐射组规划(self):
        def 辐射计划():
            scc = 84.5
            pc = 82
            cc = 87
            mt = 78
            chs = 100
            en = 71
            sc3 = Toplevel(sc)
            sc3.geometry(f"{x}x{y}+300+125")
            sc3.title("辐射计划5")
            p1, k1 = 辐射组logo(sc3, "辐射计划V")
            Label(sc3, text="实力目标计划", font=(华体, 25)).place(x=50, y=110)
            Label(sc3,
                  text=f"三大主科:语文{chs}/110-{round(chs / 1.1, 4)}%\n数学{mt}/150-{round(mt / 1.5, 4)}%\n鸟语{en}/90-{round(en / 0.9, 4)}%。",
                  font=(华体, 20)).place(x=50, y=150)
            Label(sc3,
                  text=f"理综:物理{pc}/90-{round(pc / 0.9, 4)}%\n生物{scc}/95-{round(scc / 0.95, 4)}%\n化学{cc}/95-{round(cc / 0.95, 4)}%。",
                  font=(华体, 20)).place(x=50, y=250)
            Label(sc3, text="现阶段:在期中考试之后三大主科必须要有1个达到100%完成\n理综必须全部100%完成\n11月25号期中考(预计)", font=(华体, 20)).place(x=50,
                                                                                                               y=350)
            Label(sc3, text="实力, 决定一切, 别被婊子占了上风！", font=(华体, 30), fg="red").pack(side=BOTTOM)

        try:
            if not ID[user_list.index(UID)] != "辐射组成员" or not ID[user_list.index(UID)] != "合作社成员" or not ID[user_list.index(
                    UID)] != "辐射组组长":
                if self.控件 is not None:
                    for i in self.控件:
                        i.destroy()
                    self.控件.clear()
                p, k = 辐射组logo(sc, "辐射组/合作社规划")

                fp = Button(sc, text="辐射计划V点这查看", command=辐射计划)
                fp.place(x=40, y=100)
                self.控件.append(fp)

                self.上级 = Button(sc, text="返回上一级", font=(华体, 12), fg="#AA00FF", bd=0, command=self.首页)
                self.上级.place(x=550, y=550)
                self.控件.append(self.上级)
                self.控件.append(p)
                self.控件.append(k)
            else:
                messagebox.showwarning("警告", "您的账户无法使用此功能")
        except Exception:
            messagebox.showwarning("警告", "无账户，无法使用此功能")

    def 开发者模式(self):
        list1 = []
        x1 = []
        y1 = []
        text = []
        sc3 = Tk()

        def 编辑界面(*event):
            sc3.destroy()
            sc1 = Tk()
            sc1.title("窗口编辑")
            sc1.geometry(f"{x}x{y}+300+250")
            qq = PhotoImage(file="tk模板.png")
            Label(sc1, image=qq).place(x=0, y=0)

            def 显示(event1):
                m = Label(sc1, text=str(event1.x) + "," + str(event1.y), width=300, anchor="w")
                m.place(x=700, y=560)
                sc1.after(5000, m.destroy)

            def 组件管理():
                gl = Tk()
                gl.title("组件管理")
                gl.geometry("400x400")
                for i in list1:
                    num = list1.index(i)
                    Label(gl, text="组件信息:" + i["text"] + "(" + str(x1[num]) + "," + str(y1[num]) + ")").pack(anchor="w")
                    i.place(x=x1[num], y=y1[num])
                gl.mainloop()

            def 标签():
                x1.append(int(input("self")))
                y1.append(int(input("y")))
                text1 = input("text")
                text.append(text1)
                list1.append(Label(sc1, text=text1))

            def 按钮():
                pass

            def 单行输入框():
                pass

            菜单 = Menu(sc1)  # 菜单组件
            文件 = Menu(sc1)
            组件 = Menu(菜单, tearoff=0)
            组件.add_command(label="标签", command=标签)  # 普通菜单
            组件.add_command(label="组件管理", command=组件管理)
            菜单.add_cascade(label="文件")
            菜单.add_cascade(label="组件", menu=组件)  # 瀑布式菜单
            sc1['menu'] = 菜单  # 菜单显示在窗口上
            m = Label(sc1)
            sc1.bind("<Motion>", 显示)
            sc1.mainloop()

        def 检测():
            user = self.sr.get()
            p = False
            password = self.password.get()
            if user in user_list and password in user_password:
                if user_list.index(user) == user_password.index(password):
                    Label(sc3, text="登陆成功", width=200, anchor="w").place(x=100, y=140)
                    p = True
                else:
                    Label(sc3, text="用户名或密码错误", width=200, anchor="w").place(x=100, y=140)
                    p = False
            else:
                Label(sc3, text="无此用户", width=200, anchor="w").place(x=100, y=140)
            if p:
                编辑界面()

        sc3.title("管理程序--开发者模式")
        sc3.geometry("300x200+300+250")
        Label(sc3, text="登录", font=("宋体", 30)).place(x=0, y=0)
        self.m = Label(sc3, text="用户名", font=("宋体", 20))
        self.m.place(x=0, y=50)
        self.sr = Entry(sc3)
        self.sr.place(x=100, y=55)
        self.mm = Label(sc3, text="密码", font=("宋体", 20))
        self.mm.place(x=0, y=100)
        self.password = Entry(sc3, show="♂")
        self.password.place(x=100, y=105)
        self.log = Button(sc3, text="登录", bd=1, font=("", 15), command=检测)
        self.log.place(x=0, y=140)
        sc3.bind("<ButtonPress-3>", 编辑界面)
        sc3.mainloop()

    def 概率模拟(self):
        if len(self.控件) != 0:
            for i in self.控件:
                i.destroy()
            self.控件.clear()
        辐射组logo(sc, "概率模拟")
        sc.title("辐射组管理程序--概率模拟")
        self.原神 = Button(sc, text="原神概率模拟", font=(华体, 20), fg="#FF0000", image=原神宣传图, bd=0, command=原神_模拟, anchor="se",
                         compound=CENTER)
        # compound图片显示与文字之哪
        self.原神.place(x=50, y=140)
        self.控件.append(self.原神)

        self.明日 = Button(sc, text="明日配方抽奖", font=(华体, 20), fg="#00EEFF", image=明日宣传图, bd=0, command=明日_模拟, anchor="se",
                         compound=CENTER)
        self.明日.place(x=355, y=140)
        self.控件.append(self.明日)

        self.A = Button(sc, text="Apex快速模拟", font=(华体, 16), fg="#0020FF", image=Apex宣传图, bd=0, command=其余游戏.Apex_模拟,
                        anchor="se",
                        compound=CENTER)
        self.A.place(x=45, y=320)
        self.控件.append(self.A)

        self.方舟 = Button(sc, text="明日方舟寻访模拟", font=(华体, 16), fg="#1145FF", image=方舟宣传图, bd=0, command=其余游戏.明日方舟_模拟,
                         anchor="se",
                         compound=CENTER)
        self.方舟.place(x=270, y=320)
        self.控件.append(self.方舟)

        self.崩 = Button(sc, text="崩坏三标配补给", font=(华体, 16), fg="#EE00F0", image=崩三宣传图, bd=0, command=其余游戏.崩三_模拟,
                        anchor="se",
                        compound=CENTER)
        self.崩.place(x=500, y=320)
        self.控件.append(self.崩)

        self.上级 = Button(sc, text="返回首页", font=(华体, 12), fg="#AA00FF", bd=0, command=self.首页)
        self.上级.place(x=20, y=575)
        self.控件.append(self.上级)

        self.数据 = Button(sc, text="查看概率分析", font=(华体, 12), fg="#156555", bd=0, command=self.分析)
        self.数据.place(x=100, y=575)
        self.控件.append(self.数据)
        sc.update()

    def 分析(self):
        global 可查看

        def 支付():
            global 可查看
            try:
                WST[user_list.index(UID)] -= 399
                with open("WST.json", "w", encoding=统一码) as f:
                    嫁我.dump(WST, f)
                账户财产(UID)
                messagebox.showinfo("付费提示", "支付成功")
                查看分析()
            except ValueError:
                messagebox.showwarning("警告", "您没有登录，无法完成支付！")

        def 查看分析():
            pass

        for i in self.控件:
            i.destroy()
        self.控件.clear()
        辐射组logo(sc, "抽卡分析")
        sc.title("辐射组管理程序--抽卡分析")
        FX = Button(sc, text="支付399 WST可查看更具体分析数据", bd=1, command=支付)
        FX.place(x=40, y=120)
        aa = Label(sc, text="基础概率分析:", font=(华体, 25, 加粗))
        aa.place(x=40, y=180)
        bb = Label(sc, text="原神----有up角色抽奖：\nP(5星物品)=1.61%\nP(4星物品)=13.57%\n大多数第77抽出金\n根据非小酋等统计网站分析\n一般第77抽出金，132抽大保底",
                   font=(原神字体, 18, 加粗), anchor="w", fg="#EE0000")
        bb.place(x=65, y=220)
        cc = Label(sc, text="明日之后----90级配方机抽奖\nA2出货概率为0.3506%\n与实际出货概率严重不符", font=("", 18, 加粗), anchor="w",
                   fg="#0033FF")
        cc.place(x=405, y=220)
        dd = Label(sc, text="其余游戏:\nApex-传家宝综合概率=2.2%，保底500\n明日方舟-六星出货概率=2.891%,保底100,平均57发出货\n崩坏三角色出货率=20.8248%,保底100",
                   font=("", 18, 加粗), anchor="w", fg="#FF00FF")
        dd.place(x=79, y=400)
        self.上级 = Button(sc, text="返回上一级", font=(华体, 12), fg="#AA00FF", bd=0, command=self.概率模拟)
        self.上级.place(x=20, y=575)
        self.控件.append(self.上级)
        self.控件.append(aa)
        self.控件.append(bb)
        self.控件.append(cc)
        self.控件.append(dd)
        self.控件.append(FX)
        sc.update()


if __name__ == "__main__":
    a = 辐射组管理程序()
    a.首页()
