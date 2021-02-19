# クラス
class Student:

    def __init__(self, name):
        self.name = name

    def calculateAvg(self, data_list):
        avg = sum(data_list) / len(data_list)
        return avg

    def judge(self, avg):
        if(avg >= 60):
            result = "passed"
        else:
            result = "failed"
        return result


a001 = Student("Sato")
a001.data_list = [10, 20, 30, 40, 50]
a001.avg = a001.calculateAvg(a001.data_list)
a001.result = a001.judge(a001.avg)

print("avg = ", a001.avg)
print("judge = ", a001.result)
