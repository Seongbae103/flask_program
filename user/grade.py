class Grade(object):
    def __init__(self, name, ko, en, ma):
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.total()
        self.avg()
        self.set_grade()

    def total(self):
        return self.ko + self.en + self.ma

    def avg(self):
        return self.total() / 3

    def set_grade(self):
        avg = self.avg()
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "c"
        elif avg >= 60:
            grade = "D"
        elif avg >= 50:
            grade = "E"
        else: grade = "F"
        return grade

    def __str__(self):
        return f"{self.name} {self.ko} {self.en} {self.ma} {self.total()} {self.avg()} {self.set_grade()}"

    @staticmethod
    def new_test():
        return Grade(input("이름 : "),
                     int(input("국어 : ")),
                     int(input("영어 : ")),
                     int(input("수학 : ")))
    @staticmethod
    def print_result(ls):
        print(f"### 성적 ###")
        print("*********************")
        print("이름 국어 영어 수학 총점 평균")
        print("*********************")
        [print(i) for i in ls]
        print("*********************")

    @staticmethod
    def delete(ls, name):
        '''for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]'''
        del ls[[i for i, j in enumerate(ls) if j.name == name][0]]
