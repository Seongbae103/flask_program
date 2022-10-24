class Fruit(object):
    def __init__(self,fname):
        self.fname = fname

    @staticmethod
    def print_menu():
        print("1. 과일 등록")
        print("2. 과일 목록")
        print("3. 삭제")
        print("4. 종료")
        return int(input("실행 메뉴 : "))

    @classmethod
    def add_fruit(ls):
        return Fruit(input("과일 이름 : "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Fruit.print_menu()
            if menu == 1:
                print("과일 등록")
                ls.append(Fruit.add_fruit())
            elif menu == 2:
                print("과일 목록")
                Fruit.add_fruit(ls)
            elif menu == 3:
                print("삭제")
            elif menu == 4:
                print("종료")



Fruit.main()