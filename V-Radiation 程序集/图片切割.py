import tkinter.filedialog as tf
from PIL import Image

filename = tf.askopenfilename()
asksave = tf.askdirectory()
img = Image.open(filename)
print(img.size)
切割份数 = int(input())
图片扩大倍数 = int(input())
图片列表 = []
for i in range(切割份数):
    print("正在分割图片,序列" + str(i + 1) + "保存文件夹" + asksave + "格式：jpg")
    大小 = int(img.size[1]/切割份数)
    print((0, 大小 * i, img.size[0], 大小 * (1 + i)))
    cop = img.crop((0, 大小 * i, img.size[0], 大小 * (1 + i)))
    print(cop.size)
    if cop.size[0] != 0 and cop.size[1] != 0:
        cop.save(f"{asksave}/image{i + 1}.jpg")
    else:
        print("不能存空图片！")

pj = Image.new("RGB", (1820, 1323))
pj2 = Image.new("RGB", (1820, 1323))
x = 0
y = 0
for j in range(len(图片列表)):
    Img = Image.open(f"{asksave}/image{j + 1}.jpg")
    if j < 15:
        pj.paste(Img, (img.size[0] * x, img.size[1] * y))
        x += 1
        if x > 5:
            y += 1
            x = 0
    else:
        pj2.paste(Img, (img.size[0] * x, img.size[1] * y))
        x += 1
        if x > 5:
            y += 1
            x = 0
pj.save(f"{asksave}/1.jpg")
pj2.save(f"{asksave}/2.jpg")
