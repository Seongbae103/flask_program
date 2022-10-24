class Grade(object):
    def __init__(self):
        pass
    def excute(self):
        pass

    @staticmethod
    def print_menu():
        print("1. 성적 등록")
        print("2. 성적 출력")
        print("3. 성적 삭제")
        print("4. 종료")
        return int(input("실행 메뉴 : "))
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Grade.print_menu()
            if menu == "1":
                print("성적 등록")
            elif menu == "2":
                print("성적 출력")
            elif menu == "3":
                print("성적 삭제")
            elif menu == "4":
                print("종료")
                break

Grade.main()