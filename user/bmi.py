from util.common import Common


class Bmi(object):
    def __init__(self, name, h, kg):
        self.name = name
        self.h = h
        self.kg = kg
        self.biman = ""

    def get_bmi(self):
        m = self.h / 100
        kg = self.kg
        return kg/m**2

    def get_biman(self):
        bmi = self.get_bmi()
        if bmi >= 35:
            biman = "고도 비만"
        elif bmi >= 30:
            biman = "중(重)도 비만 (2단계 비만)"
        elif bmi >= 25:
            biman = "경도 비만 (1단계 비만)"
        elif bmi >= 23:
            biman = "과체중"
        elif bmi >= 18.5:
            biman = "정상"
        else:
            biman = "저체중"
        self.biman = biman

    def __str__(self):
        return f"{self.name} {self.h} {self.kg} {self.biman}"


    @staticmethod
    def new_user():
        return Bmi(input("이름 : "),
                   int(input("키 : ")),
                   int(input("체중 : ")))

    @staticmethod
    def print_result(ls):
        print("###비만도###")
        print("**********************")
        print("이름 키 체중 bmi 비만도")
        print("**********************")
        [print(i) for i in ls]
        print("**********************")

    @staticmethod
    def delete(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

