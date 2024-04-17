"""原神角色祈愿随机实验----代码"""
from tkinter import *
from Rt_1引擎 import *
from 算法函数 import 米FA游游戏抽卡
import 基本常量
from 统计 import 游戏统计

cl = pg.time.Clock()
抽奖相对次数 = 0
总次数 = 0
五星角色概率 = 0.003
五星武器概率 = 0.003
四星角色概率 = 0.0255
四星武器概率 = 0.0255
概率增幅系数 = 600
增幅起始位置 = 74
保底控制 = False
自定义次数 = 2500
up列表 = []
上一次 = 0
with open("./概率模拟-原神/抽奖记录.json", "r", encoding="utf-8") as f:
    储存列表 = 基本常量.js.load(f)
with open("./概率模拟-原神/星级.json", "r", encoding="utf-8") as f:
    星级 = 基本常量.js.load(f)
临时列表 = []
保底角色 = "荒泷一斗"
结果 = True
相对次数列表 = []
卡池组 = None
卡池组名字 = "官方卡池"
ls = 米FA游游戏抽卡()


def 计算(判断=4):
    list888 = []
    for i in 星级:
        if i == 判断:
            list888.append(i)
        pass
    return round(len(list888) / 总次数 * 100, 2)


def 记录区():
    sc12 = Tk()
    sc12.title("抽卡记录")
    sc12.geometry("600x400+300+150")
    p = Text(sc12)
    g = 0
    md = 1
    for i in 储存列表:
        g += 1
        if g == 1:
            p.insert(END, str(md) + "." + i + ",")
        if g == 9:
            md += 1
            p.insert(END, i + "\n")
            g = 0
        else:
            p.insert(END, i + ",")
    p.config(state=DISABLED)
    p.pack(expand=YES, fill=BOTH)
    sc12.mainloop()


def 数据(界面1=None):
    背景 = 模型(phname="./概率模拟-原神/出货背景.png", name=界面1, x=0, y=0)
    背景.缩放(w=852, h=480)
    背景.加载()
    单行文字(文字="数据:", 字体文件="原神字体.ttf", 窗口=界面1, 字体大小=30, 字体颜色="#FFFFFF").有坐标展示(10, 10, True)
    单行文字(文字=f"目前共计抽了{总次数}次, 相对于上一次保底抽数为{抽奖相对次数}", 字体文件="原神字体.ttf", 窗口=界面1, 字体大小=25, 字体颜色="#FFFFFF").有坐标展示(70, 45, True)
    单行文字(文字=f"共计消耗原石{总次数*160}({总次数}x160), 纯氪金抽取需人民币{总次数*16}元", 字体文件="原神字体.ttf", 窗口=界面1, 字体大小=20, 字体颜色="#FFFFFF").有坐标展示(70, 75, True)
    单行文字(文字=f"未完待续......", 字体文件="原神字体.ttf", 窗口=界面1, 字体大小=25, 字体颜色="#FFFFFF").有坐标展示(70, 105, True)

    nm = True
    while nm:
        for jks in pg.event.get():
            if jks.type == pg.KEYDOWN:
                if jks.key == pg.K_F7:
                    nm = False
        pg.display.update()


def 声明(ID):
    声明字符 = '此程序因为实在没有素材导致出货动画表现不好，今后将会完善这一部分，深感抱歉!\n本程序无任何商业用途，就别拿去赚钱了。\n本程序抽卡概率等数据是可以自己调节的，概率算法比较贴进游戏。'
    sc12 = Tk()
    sc12.title("应用声明")
    sc12.geometry("600x400+300+150")
    p = Text(sc12)
    p.insert(END, 声明字符)
    if ID == "辐射组组长":
        p.config(state=NORMAL)
    else:
        p.config(state=DISABLED)
    p.pack(expand=YES, fill=BOTH)
    sc12.mainloop()


def 概率修改器():
    global 五星角色概率
    global 五星武器概率
    global 四星角色概率
    global 四星武器概率
    global 概率增幅系数
    global 增幅起始位置
    global 保底角色
    global 自定义次数
    global 卡池组名字

    def 提交():
        global 五星角色概率
        global 五星武器概率
        global 四星角色概率
        global 四星武器概率
        global 概率增幅系数
        global 增幅起始位置
        global 保底角色
        global 自定义次数
        global 卡池组名字
        五星角色概率 = float(SSRr.get())
        四星角色概率 = float(SRr.get())
        五星武器概率 = float(SSRw.get())
        四星武器概率 = float(SRw.get())
        概率增幅系数 = int(up.get())
        增幅起始位置 = int(起始.get())
        保底角色 = 保底.get()
        自定义次数 = int(JIC.get())
        卡池组名字 = 卡池2.get()
        发 = Label(f, text="提交成功")
        发.place(x=0, y=370)
        f.after(2000, 发.destroy)

    f = Tk()
    f.geometry("400x400+300+125")
    f.title("概率修改器")
    Label(f, text="概率修改器", font=("汉仪文黑-85W Heavy", 20)).place(x=0, y=0)
    Label(f, text="五星角色概率", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=40)
    Label(f, text="四星角色概率", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=70)
    Label(f, text="五星武器概率", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=100)
    Label(f, text="四星武器概率", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=130)
    Label(f, text="五星概率增幅系数", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=160)
    Label(f, text="增幅起始位置", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=190)
    Label(f, text="保底角色名字", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=220)
    Label(f, text="自定义次数", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=250)
    Label(f, text="自定义卡池组", font=("汉仪文黑-85W Heavy", 15)).place(x=0, y=280)
    JIC = Entry(f)
    JIC.place(x=160, y=253)
    JIC.insert(END, 自定义次数)
    卡池2 = Entry(f)
    卡池2.place(x=160, y=283)
    卡池2.insert(END, 卡池组名字)
    SSRr = Entry(f)
    SRr = Entry(f)
    SSRw = Entry(f)
    SRw = Entry(f)
    SSRr.place(x=160, y=43)
    SRr.place(x=160, y=73)
    SSRw.place(x=160, y=103)
    SRw.place(x=160, y=133)
    up = Entry(f)
    up.place(x=190, y=163)
    起始 = Entry(f)
    起始.place(x=160, y=193)
    保底 = Entry(f)
    保底.place(x=160, y=223)
    SSRr.insert(END, 五星角色概率)
    SRr.insert(END, 四星角色概率)
    SSRw.insert(END, 五星武器概率)
    SRw.insert(END, 四星武器概率)
    up.insert(END, 概率增幅系数)
    起始.insert(END, 增幅起始位置)
    保底.insert(END, 保底角色)
    提交 = Button(f, text="修改好了提交", bd=1, font=("汉仪文黑-85W Heavy", 15), command=提交)
    提交.pack(side=BOTTOM)
    f.mainloop()


def 概率模拟_原神(认证=None):
    global 五星角色概率
    global 五星武器概率
    global 四星角色概率
    global 四星武器概率
    global 概率增幅系数
    global 增幅起始位置
    global 保底角色
    global up列表
    global 上一次
    pg.init()
    界面 = pg.display.set_mode((int(852), int(480)))
    ss = pg.image.load("图表.png")
    pg.display.set_caption("原神抽卡模拟器")
    pg.display.set_icon(ss)
    x = 0
    yd = 模型(界面, "./概率模拟-原神/一斗.png", 180, 50)
    yd.缩放(倍数=3, name=界面)
    f = 按钮(界面, fg="#000000", text="来一发", x=650, y=430, 字体文件="原神字体.ttf", zsize=10, 背景图案='./概率模拟-原神/抽奖按钮.png'
           , 倍数=1.7)
    f10 = 按钮(界面, fg="#000000", text="来十发", x=500, y=430, 字体文件="原神字体.ttf", zsize=10, 背景图案='./概率模拟-原神/抽奖按钮.png'
             , 倍数=1.7)
    fN = 按钮(界面, fg="#000000", text=f"来N发", x=350, y=430, 字体文件="原神字体.ttf", zsize=10, 背景图案='./概率模拟-原神/抽奖按钮.png'
            , 倍数=1.7)
    概率修改 = 按钮(界面, fg="#000000", text="更改概率", x=40, y=435, 字体文件="原神字体.ttf", zsize=10, 背景图案='./概率模拟-原神/兑换按钮.png'
              , 倍数=1.5)
    说明 = 按钮(界面, fg="#000000", text="声明", x=140, y=435, 字体文件="原神字体.ttf", zsize=10, 背景图案='./概率模拟-原神/兑换按钮.png'
            , 倍数=1.5)
    记录 = 按钮(界面, fg="#000000", text="记录", x=240, y=435, 字体文件="原神字体.ttf", zsize=10, 背景图案='./概率模拟-原神/兑换按钮.png'
            , 倍数=1.5)

    #视频动画(窗口对象=界面, 文字动画=["昆十二中数学建模小组 制作", "前端 陈玄", "算法 陈玄,王文健", "后台统计 赵靖凯", "素材 原神官方和b站up主"],
    #字体文件="原神字体.ttf", 文字对齐="居中", FPS=5, 淡出=True, 字体大小=35)

    def 统计():
        global 五星角色概率
        global 五星武器概率
        global 四星角色概率
        global 四星武器概率
        global 概率增幅系数
        global 增幅起始位置
        global 保底角色
        游戏统计(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             y=星级,
             预设统计类型="原神--出金概率折线图").凯子统计法(title="原神概率统计", 频数统计=[True, [相对次数列表, 星级], up列表])

    def 抽奖动画(次数=1):
        global 抽奖相对次数
        global 总次数
        global 保底控制
        global 保底角色
        global 上一次
        if 次数 == 1:
            抽奖相对次数 += 1
            总次数 += 1
            g = ls.原神抽卡(五星角色概率=五星角色概率, 五星武器概率=五星武器概率, 四星武器概率=四星武器概率, 四星角色概率=四星角色概率,
                        第几次=抽奖相对次数, 大小保底控制=保底控制, up五星角色=保底角色, 自定义奖池名字=卡池组名字)
            储存列表.append(g[0])
            星级.append(g[1])
            if g[0] == 保底角色:
                up列表.append(总次数 - 上一次)
                上一次 = 总次数
                保底控制 = False
                h2 = "大保底"
            else:
                up列表.append(0)
                if g[1] == 5:
                    保底控制 = True
                    h2 = "小保底"
            if 抽奖相对次数 == 90:
                抽奖相对次数 = 0
            if g[1] == 5:
                相对次数列表.append(抽奖相对次数)
                视频(dirmv=f"./概率模拟-原神/单抽出金/Image", dirmu="./概率模拟-原神/原神抽卡声音.mp3", name=界面, x=0, y=0)
                抽奖相对次数 = 0
            elif g[1] == 4:
                相对次数列表.append(0)
                视频(dirmv=f"./概率模拟-原神/单抽出紫/Image", dirmu="./概率模拟-原神/原神抽卡声音.mp3", name=界面, x=0, y=0)
                h2 = "没有五星"
            else:
                相对次数列表.append(0)
                视频(dirmv=f"./概率模拟-原神/单抽出蓝/Image", dirmu="./概率模拟-原神/原神抽卡声音.mp3", name=界面, x=0, y=0)
                h2 = "没有五星"
            with open("./概率模拟-原神/抽奖记录.json", "w", encoding="utf-8") as fq:
                基本常量.js.dump(储存列表, fq)
            with open("./概率模拟-原神/星级.json", "w", encoding="utf-8") as fq:
                基本常量.js.dump(星级, fq)

            出货(g[0] + " " + str(g[1]), '单抽', h2, g[2], g[-3], g[-1], g[-2])

        elif 次数 == 10:
            for i in range(1, 11, 1):
                抽奖相对次数 += 1
                总次数 += 1
                g = ls.原神抽卡(五星角色概率=五星角色概率, 五星武器概率=五星武器概率, 四星武器概率=四星武器概率, 四星角色概率=四星角色概率,
                            第几次=抽奖相对次数, 大小保底控制=保底控制, up五星角色=保底角色, 自定义奖池名字=卡池组名字)
                if g[0] == 保底角色:
                    up列表.append(总次数 - 上一次)
                    上一次 = 总次数
                    保底控制 = False
                    h2 = "大保底"
                else:
                    up列表.append(0)
                    if g[1] == 5:
                        保底控制 = True
                        h2 = "小保底"
                if g[1] == 5:
                    相对次数列表.append(抽奖相对次数)
                    抽奖相对次数 = 0
                else:
                    相对次数列表.append(0)
                星级.append(g[1])
                临时列表.append(g[1])
                储存列表.append(g[0])

            if 抽奖相对次数 == 90:
                抽奖相对次数 = 0
            if 5 in 临时列表:
                视频(dirmv=f"./概率模拟-原神/十连出金/Image", dirmu="./概率模拟-原神/原神抽卡声音.mp3", name=界面, x=0, y=0)
            else:
                视频(dirmv=f"./概率模拟-原神/十连出紫/Image", dirmu="./概率模拟-原神/原神抽卡声音.mp3", name=界面, x=0, y=0)
                h2 = "没有五星"
            list5 = []
            ga = -10
            for ii in 储存列表[-10:]:
                list5.append(ii + " " + str(临时列表[ga]))
                ga += 1
            出货(list5, "十连抽", h2, g[2], g[-3], g[-1], g[-2])
            临时列表.clear()

        else:
            for i in range(1, 自定义次数 + 1, 1):
                抽奖相对次数 += 1
                总次数 += 1
                g = ls.原神抽卡(五星角色概率=五星角色概率, 五星武器概率=五星武器概率, 四星武器概率=四星武器概率, 四星角色概率=四星角色概率,
                            第几次=抽奖相对次数, 大小保底控制=保底控制, up五星角色=保底角色, 自定义奖池名字=卡池组名字)
                储存列表.append(g[0])
                星级.append(g[1])
                if g[0] == 保底角色:
                    up列表.append(总次数 - 上一次)
                    上一次 = 总次数
                    保底控制 = False
                    h2 = "小保底"
                else:
                    up列表.append(0)
                    if g[1] == 5:
                        保底控制 = True
                        h2 = "大保底"
                if 抽奖相对次数 == 90:
                    抽奖相对次数 = 0
                if g[1] == 5:
                    相对次数列表.append(抽奖相对次数)
                    抽奖相对次数 = 0
                else:
                    相对次数列表.append(0)
            with open("./概率模拟-原神/抽奖记录.json", "w", encoding="utf-8") as fq:
                基本常量.js.dump(储存列表, fq)
            with open("./概率模拟-原神/星级.json", "w", encoding="utf-8") as fq:
                基本常量.js.dump(星级, fq)
            出货("N/A", f'自定义抽奖次数{自定义次数}', "N/A", g[2], g[-3], g[-1], g[-2])

    def 出货(抽到的东西, 类型=None, 大保底触发=False, 五星概率=None, f2=None, 四星概率1=None, 四星概率2=None):
        global 结果
        背景 = 模型(phname="./概率模拟-原神/出货背景.png", name=界面, x=0, y=0)
        背景.缩放(w=852, h=480)
        背景.加载()
        单行文字(f"抽奖结果(相对次数={抽奖相对次数},总次数={总次数})", None, "原神字体.ttf", 界面, 字体大小=39, 字体颜色="#FFFFFF").有坐标展示(0, 0, True)
        单行文字(f"你抽奖的类型:{类型}", None, "原神字体.ttf", 界面, 字体大小=30, 字体颜色="#FFFFFF").有坐标展示(0, 50, True)
        if type(抽到的东西) == type(储存列表):
            单行文字(f"你抽到了:{抽到的东西[0:5]}", None, "原神字体.ttf", 界面, 字体大小=20, 字体颜色="#FFFFFF").有坐标展示(0, 100, True)
            单行文字(f"             {抽到的东西[5:]}", None, "原神字体.ttf", 界面, 字体大小=20, 字体颜色="#FFFFFF").有坐标展示(0, 130, True)
        else:
            单行文字(f"你抽到了:{抽到的东西}", None, "原神字体.ttf", 界面, 字体大小=30, 字体颜色="#FFFFFF").有坐标展示(0, 100, True)
        单行文字("概要:", None, "原神字体.ttf", 界面, 字体大小=30, 字体颜色="#FFFFFF").有坐标展示(0, 160, True)
        单行文字(f"       角色概率:五星={round(五星概率 * 100, 4)}% 四星={round(四星概率1 * 100, 4)}%", None, "原神字体.ttf", 界面, 字体大小=25,
             字体颜色="#FFFFFF").有坐标展示(0, 200, True)
        单行文字(f"       武器概率:五星={round(f2 * 100, 4)}% 四星={round(四星概率2 * 100, 4)}%", None, "原神字体.ttf", 界面, 字体大小=25,
             字体颜色="#FFFFFF").有坐标展示(
            0, 230, True)
        if 大保底触发 == "N/A":
            单行文字(f"       目前物品频率:五星{计算(5)}%,四星{计算()}%", None, "原神字体.ttf", 界面, 字体大小=25, 字体颜色="#FFFFFF").有坐标展示(0, 260,
                                                                                                             True)
        else:
            单行文字(f"       是否大保底{大保底触发}", None, "原神字体.ttf", 界面, 字体大小=25, 字体颜色="#FFFFFF").有坐标展示(0, 260, True)
        单行文字(f"       原石总消耗:{总次数 * 160},纯氪金消耗人民币{总次数 * 16}元", None, "原神字体.ttf", 界面, 字体大小=25, 字体颜色="#FFFFFF").有坐标展示(0,
                                                                                                                   290,
                                                                                                                   True)
        单行文字("按F4可查看更详细的情况", None, "原神字体.ttf", 界面, 字体大小=30, 字体颜色="#FFFFFF").有坐标展示(0, 395, True)
        单行文字("点击鼠标可返回抽奖界面", None, "原神字体.ttf", 界面, 字体大小=30, 字体颜色="#FFFFFF").有坐标展示(0, 440, True)
        pg.display.update()
        结果 = True
        while 结果:
            for ee in pg.event.get():
                if ee.type == pg.QUIT:
                    pg.quit()
                    with open("./概率模拟-原神/抽奖记录.json", "w", encoding="utf-8") as fq:
                        基本常量.js.dump([], fq)
                    with open("./概率模拟-原神/星级.json", "w", encoding="utf-8") as fq:
                        基本常量.js.dump([], fq)
                if ee.type == pg.MOUSEBUTTONDOWN:
                    结果 = False
                if ee.type == pg.KEYDOWN:
                    if ee.key == pg.K_F4:
                        统计()
                        print("我们在飞速统计中")

    while True:
        cl.tick(60)
        界面.fill("#000000")
        x += 1
        图片插入(f"./概率模拟-原神/背景壁纸/image{x}.png", 界面, 0, 0)
        单行文字("祈愿", 字体文件="原神字体.ttf", 窗口=界面, 字体大小=30, 字体颜色="#00FFFF").有坐标展示(10, 10)
        单行文字(f"次数:{总次数}", 字体文件="原神字体.ttf", 窗口=界面, 字体大小=30, 字体颜色="#00FFFF").有坐标展示(10, 40)
        yd.加载()
        f.绘制()
        f10.绘制()
        fN.绘制()
        概率修改.绘制()
        说明.绘制()
        记录.绘制()
        xh = f.感应()
        sh = f10.感应()
        fk = fN.感应()
        fh = 概率修改.感应()
        pp = 说明.感应()
        ppp = 记录.感应()
        if x == 1142:
            x = 0
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                with open("./概率模拟-原神/抽奖记录.json", "w", encoding="utf-8") as fq:
                    基本常量.js.dump([], fq)
                with open("./概率模拟-原神/星级.json", "w", encoding="utf-8") as fq:
                    基本常量.js.dump([], fq)
                sys.exit()
            if xh == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                抽奖动画()
            if sh == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                抽奖动画(10)
            if fk == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                抽奖动画(自定义次数)
            if fh == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                概率修改器()
            if pp == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                声明(ID=认证)
            if ppp == "ok" and event.type == pg.MOUSEBUTTONDOWN:
                记录区()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_F1:
                    抽奖动画(10)
                if event.key == pg.K_F2:
                    抽奖动画(1)
                if event.key == pg.K_F3:
                    抽奖动画(自定义次数)
                if event.key == pg.K_F4:
                    th.Thread(target=统计).start()
                    print("我们在飞速统计中")
                if event.key == pg.K_F5:
                    数据(界面)
        pg.display.update()


if __name__ == "__main__":
    概率模拟_原神()
