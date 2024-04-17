from threading import Thread as th
from tkinter import *
from 统计 import 游戏统计
from 算法函数 import 明日之后抽奖

x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0

概率 = {'无人机': 0.0119, '稀有装备涂装': 0.2259, '稀有装备配方': 0.4774, '个性庄园配方': 0.0466, '普通庄园配方': 0.2382}
奖池 = {'无人机': ["肥宅俱乐部", "真感情"],
      '稀有装备涂装': ["A2-13突榴枪-雨战先锋", "A2-13突榴枪-雪地精英", "A2-13突榴枪-典藏版",
                 "KSG霰弹枪-雨战先锋", "KSG霰弹枪-雪地精英", "KSG霰弹枪-典藏版",
                 "AWM狙击枪-雨战先锋", "AWM狙击枪-雪地精英", "AWM狙击枪-典藏版",
                 "EM-1电磁机枪-雨战先锋", "EM-1电磁机枪-雪地精英", "EM-1电磁机枪-典藏版",
                 "短管冲锋枪-雨战先锋", "短管冲锋枪-雪地精英", "短管冲锋枪-典藏版"],
      '稀有装备配方': ["A2-13突榴枪", "KSG霰弹枪", "AWM狙击枪", "EM-1电磁机枪"],
      '个性庄园配方': ["小晨的坟墓", "皮格厂厂牌", "小晨靶子", "夏尔狗的坟头"],
      '普通庄园配方': ["小晨的花圈", "小晨的遗照"]}
物品简介 = {}


def 氪金使你强大():
    配方残页.set(配方残页.get() + 160 * 50)


def 快速获取数据():
    def aa(次数=500000, 谁的概率="A2-13突榴枪-典藏版"):
        x = []
        y = []
        sd = []
        for i in range(1, 次数 + 1):
            print("抽奖中" + str(round(i / 次数 * 100, 7)) + "%")
            f2 = 明日之后抽奖(1, "配方机抽奖").配方机抽奖(概率, 奖池)
            if f2[2] == 谁的概率:
                sd.append(1)
            else:
                sd.append(0)
            x.append(i)
            y.append(sum(sd) / i)
        print("正在统计")
        游戏统计(x=x, y=y, 预设统计类型="明日之后--物品概率对比折线图").凯子统计法()
    th(target=aa).start()


def 明日之后_100级配方抽奖():
    global 配方残页
    global x1, x2, x3, x4, 总次数, x5
    if 配方残页.get() - 160 < 0:
        奖品.set("你没有足够的残页来抽这个奖池，要不氪点?")
        scm.update()
    else:
        总次数.set(总次数.get() + 1)
        配方残页.set(配方残页.get() - 160)
        for i in range(1):
            f = 明日之后抽奖(1, "配方机抽奖").配方机抽奖(概率, 奖池)
            if f[1] == '普通庄园配方':
                x1 += 1
            if f[1] == '个性庄园配方':
                x2 += 1
            if f[1] == '稀有装备配方':
                x3 += 1
            if f[1] == '稀有装备涂装':
                x4 += 1
            if f[2] == "A2-13突榴枪-典藏版":
                x5 += 1

            奖品.set("您获得了:" + f[1] + "----" + f[2])
            Label(scm, textvariable=奖品).place(x=20, y=100)
            Label(scm, textvariable=A2典藏概率).place(x=105, y=470)
            A2典藏概率.set(round(x5 / 总次数.get() * 100, 2))
            scm.update()


def 明日之后_活动抽奖():
    pass


scm = Tk()
scm.geometry("800x500+300+150")
scm.title("明日之后简易模拟器")
奖品 = StringVar(scm)
A2典藏概率 = DoubleVar()
配方残页 = IntVar(scm)
配方残页.set(9000)
总次数 = IntVar()
总次数.set(0)
Label(scm, text="抽配方请按这里(60级合成,100级概率)").place(x=10, y=10)
Label(scm, text="共计抽奖次数:").place(x=160, y=469)
Label(scm, textvariable=总次数).place(x=245, y=469)
Label(scm, text="残页").place(x=750, y=10)
Label(scm, text="A2典藏概率:").place(x=20, y=470)
Label(scm, text="残页").place(x=750, y=10)
a = Button(scm, text="Check me! 160残页", command=明日之后_100级配方抽奖)
a.place(x=10, y=40)
b = Button(scm, textvariable=配方残页, command=氪金使你强大, bd=0)
b.place(x=750, y=30)
c = Button(scm, text="快速统计", command=快速获取数据)
c.place(x=250, y=10)
scm.mainloop()
