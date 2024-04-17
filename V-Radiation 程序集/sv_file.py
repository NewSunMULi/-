class SV_File:
    def __init__(self, fileName):
        self.file = open(fileName, "r", encoding="utf-8")
        self.dataList1 = list(self.file.readlines())
        self.dataList2 = []
        for i in range(len(self.dataList1)):
            self.dataList2.append(self.dataList1[i].split("\n")[0].split(" "))

    def getData(self, keyword=None):
        if keyword is None:
            return_list = []
            for i in self.dataList2[:-2]:
                for j in range(len(i[1:])):
                    i[j + 1] = int(i[j + 1])
                    return_list.append(i[j + 1])
            return return_list

        else:
            for i in self.dataList2:
                if i[0] == keyword:
                    for j in range(len(i[1:])):
                        try:
                            i[j + 1] = int(i[j + 1])
                        except:
                            pass
                    return i[1:]
                else:
                    continue
            return None

    def getAllScore(self):
        return_list1 = []
        for i in self.dataList2[:6]:
            for j in range(len(i[1:])):
                i[j + 1] = int(i[j + 1])
                return_list1.append(i[j + 1])
        return_list2 = []
        x = len(return_list1) / 6
        for i in range(int(x)):
            list1 = []
            for j in range(len(return_list1)//int(x)):
                list1.append(return_list1[i + int(x)*j])
            return_list2.append(list1)
        return return_list2


if __name__ == "__main__":
    print(SV_File("./sv30/data2.sv").getAllScore())