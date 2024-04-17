import random as rd
import enum

母本 = ("AA", "Bb")
父本 = ("aa", "BY")
子一代 = []
子二代 = []
子三代 = []
times = int(input("做到几代？"))
基因数量 = {"A": 0, "a": 0, "B": 0, "b": 0, "Y": 0, "FeMa": 0}
所需数量 = 0
基因数量2 = {"A": 0, "a": 0, "B": 0, "b": 0, "Y": 0, "FeMa": 0}


class 性状(enum.Enum):
    雌性长翅正常眼 = 0
    雌性短翅正常眼 = 1
    雄性长翅正常眼 = 2
    雄性短翅正常眼 = 3
    雄性长翅棒状眼 = 4
    雄性短翅棒状眼 = 5


for i in range(times):
    for r in range(100000):
        if i == 0:
            子一代.append(
                f"{rd.choice(list(母本[0]))}{rd.choice(list(父本[0]))}{rd.choice(list(母本[1]))}{rd.choice(list(父本[1]))}")
        elif i == 1:
            子一代父本 = "sadd"
            子一代母本 = "saYY"
            while "Y" not in 子一代父本:
                子一代父本 = rd.choice(子一代)
            while "Y" in 子一代母本:
                子一代母本 = rd.choice(子一代)
            #print(子一代父本, 子一代母本)
            #print(子一代母本[0:2], 子一代母本[2:], 子一代父本[0:2], 子一代父本[2:])
            x = rd.choice(list(子一代父本[2:]))
            子二代性状 = f"{rd.choice(list(子一代母本[0:2]))}{rd.choice(list(子一代父本[0:2]))}{rd.choice(list(子一代母本[2:]))}{x if x != 'b' else 'null'}"
            #print(子二代性状)
            if "null" not in 子二代性状:
                子二代.append(子二代性状)
        elif i == 2:
            子一代父本 = "sadd"
            子一代母本 = "saYY"
            while "A" not in 子一代父本 or "Y" not in 子一代父本 or "B" in 子一代父本:
                子一代父本 = rd.choice(子二代)
            while "A" not in 子一代母本 or "Y" in 子一代母本:
                子一代母本 = rd.choice(子二代)
            #print(子一代父本, 子一代母本)
            #print(子一代母本[0:2], 子一代父本[0:2], 子一代母本[2:], 子一代父本[2:])
            x = rd.choice(list(子一代父本[2:]))
            子二代性状 = f"{rd.choice(list(子一代母本[0:2]))}{rd.choice(list(子一代父本[0:2]))}{rd.choice(list(子一代母本[2:]))}{x if x != 'b' else 'null'}"
            if "null" not in 子二代性状:
                #print(子二代性状)
                子三代.append(子二代性状)

for s in 子二代:
    if "BB" in s:
        基因数量["B"] += 2
        基因数量["FeMa"] += 1
    elif "Bb" in s or "bB" in s:
        基因数量["B"] += 1
        基因数量["b"] += 1
        基因数量["FeMa"] += 1
    elif "BY" in s or "YB" in s:
        基因数量["B"] += 1
        基因数量["Y"] += 1
    elif "bY" in s or "Yb" in s:
        基因数量["Y"] += 1
        基因数量["b"] += 1

    if "AA" in s:
        基因数量["A"] += 2
    elif "Aa" in s or "aA" in s:
        基因数量["A"] += 1
        基因数量["a"] += 1
    elif "aa" in s:
        基因数量["a"] += 2

for s in 子三代:
    if "A" in s and "b" in s:
        所需数量 += 1
    if "BB" in s:
        基因数量2["B"] += 2
        基因数量2["FeMa"] += 1
    elif "Bb" in s or "bB" in s:
        基因数量2["B"] += 1
        基因数量2["b"] += 1
        基因数量2["FeMa"] += 1
    elif "BY" in s or "YB" in s:
        基因数量2["B"] += 1
        基因数量2["Y"] += 1
    elif "bY" in s or "Yb" in s:
        基因数量2["Y"] += 1
        基因数量2["b"] += 1

    if "AA" in s:
        基因数量2["A"] += 2
    elif "Aa" in s or "aA" in s:
        基因数量2["A"] += 1
        基因数量2["a"] += 1
    elif "aa" in s:
        基因数量2["a"] += 2


print("实验报告：[共计10 000 000 次实验]")
print("子二代所含基因数量:"+str(基因数量))
print("子三代所含基因数量:"+str(基因数量2))
print("子三代雄性长翅棒眼性状比例"+str(所需数量/len(子三代)))
print("1/9的值的大小:"+str(1/9))
print("误差："+str(round((所需数量/len(子三代)) - (1/9), 4)))