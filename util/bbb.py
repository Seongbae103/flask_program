class Biman(object):
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg
        self.get_total()
        self.get_avg()
        self.get_grade()

    @staticmethod
    def print_menu():
        print("1. 입력")
        print("2. 목록")
        print("3. 삭제")
        print("4, 종료")
        return int(input("실행 : "))

    def get_bmi(self):
        return self.kg/(self.cm / 100)**2

    def get_biman(self):
        bmi = Biman.get_bmi()
        if bmi >= 35:
            biman = "고도 비만"
        elif bmi >= 30:
            biman = "중도 비만"
        elif bmi >= 25:
            biman = "경도 비만"
        elif bmi >= 23:
            biman = "과체중"
        elif bmi >= 18.5:
            biman = "정상"
        else: biman = "저체중"
        return biman

    def print(self):
        print(f"{self.name} {self.cm} {self.kg} {self.get_bmi()} {self.get_biman()}")

    @staticmethod
    def print_list(ls):
        print("###비만도###")
        print("******************")
        print("이름 키 체중 bmi 비만도")
        print("******************")
        [i.print() for i in ls]
        print("******************")

    @staticmethod
    def delete(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name]]


    @staticmethod
    def main():
        ls = []
        while True:
            menu = Biman.print_menu()
            if menu == 1:
                print("1. 입력")
                ls.append(Biman.new_user())
            elif menu == 2:
                print("2. 목록")
                Biman.print_list(ls)
            elif menu == 3:
                print("3. 삭제")
                Biman.delete(ls, input("삭제할 이름 : "))
            elif menu == 4:
                print("4. 종료")
                break
            else: print("잘못된 입력")