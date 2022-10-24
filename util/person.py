class Person(object):
    def __init__(self):
        pass
    def excute(self):
        pass

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Person.print_menu()
            if menu == "1":
                print("주민등록")
            elif menu == "2":
                print("주민 목록")
            elif menu == "3":
                print("삭제")
            elif menu == "4":
                print("종료")
Person.main()