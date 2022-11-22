biman_menu = {
        "1": lambda t: t(),
        "2": lambda t: t.print_list(),
        "3": lambda t: t.delete(),
        "4": lambda t: t.save_police_norm(),
    }
MENUS = ['입력', '목록', '삭제', '종료']
class Biman(object):
    def __init__(self, name, cm, kg):
        self.name = name
        self.cm = cm
        self.kg = kg
        self.get_total()
        self.get_avg()
        self.get_grade()

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

def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = Biman()
    while True:
        menu = my_menu(MENUS)
        if menu == '0' or '4':
            print("종료")
            break
        else:
            try:
                biman_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")