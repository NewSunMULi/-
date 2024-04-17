题目 = []
答案 = []


def 题目编写(file_name, 题目变量: list, 答案列表: list, 初始序列=0):
    with open(file_name + ".html", "w", encoding="utf-8") as f:
        for i in range(len(题目变量)):
            f.write(f'''    <span class="pages">
                            <h1>题目实战</h1>
                            <div class="xzt" style="width: 100%;">
                            <p>{题目变量[i][0]}(<span style="display: inline; color: red;" id="xzt_{i+初始序列}"></span>)</p>
                            <p>{题目变量[i][1]}</p>
                            <p>{题目变量[i][2]}</p>
                            <p>{题目变量[i][3]}</p>
                            <p>{题目变量[i][4]}</p>
                            <br><br>
                            <button type="button" style="width: 5vw; height: 7vh; font-size: 7vh; border-radius: 2vh;"
                                onclick="input_aws('A', 'xzt_{i+初始序列}')">A</button>
                            <button type="button" style="width: 5vw; height: 7vh; font-size: 7vh; border-radius: 2vh;"
                                onclick="input_aws('B', 'xzt_{i+初始序列}')">B</button>
                            <button type="button" style="width: 5vw; height: 7vh; font-size: 7vh; border-radius: 2vh;"
                                onclick="input_aws('C', 'xzt_{i+初始序列}')">C</button>
                            <button type="button" style="width: 5vw; height: 7vh; font-size: 7vh; border-radius: 2vh;"
                                onclick="input_aws('D', 'xzt_{i+初始序列}')">D</button>
                            <button type="button" style="width: 25vw; height: 8vh; font-size: 6vh; border-radius: 2vh;" \nonclick="get_aws('{答案列表[i]}')">提交答案</button>
                        </div>
                        </span>''')


def 获取文件(file_name, types=None):
    with open(file_name + ".txt", "r", encoding="utf-8") as f2:
        if types == "答案":
            return f2.readlines()
        else:
            jks = f2.readlines()
            jk = []
            for i in range(0, len(jks), 5):
                jk.append([jks[i], jks[i + 1], jks[i + 2], jks[i + 3],
                           jks[i + 4]])
                print(f"循环{i}正常")
            return jk


if __name__ == "__main__":
    题目 = 获取文件("角色")
    答案 = 获取文件("世界观", types="答案")
    题目编写("tm", 题目, 答案, 4)
