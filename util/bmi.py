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

    def print_biman(self):
        print(f"{self.name} {self.h} {self.kg} {self.biman}")

    @staticmethod
    def print_menu():
        print("1. 비만도 등록")
        print("2. 비만도 출력")
        print("3. 비만도 삭제")
        print("4. 종료")
        return int(input("메뉴 선택 : "))

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
        for i in ls:
            i.print_biman()
        print("**********************")

    @staticmethod
    def delete(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Bmi.print_menu()
            if menu == 1:
                print("비만도 등록")
                ls.append(Bmi.new_user())
            elif menu == 2:
                print("비만도 출력")
                Bmi.print_result(ls)
            elif menu == 3:
                print("비만도 삭제")
                Bmi.delete(ls, input("삭제할 이름 : "))
            elif menu == 4:
                print("종료")
                break

Bmi.main()
