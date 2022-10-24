class Member(object):
    def __init__(self):
        pass
    def excute(self):
        pass

    @staticmethod
    def print_menu():
        print("1. 회원가입")
        print("2. 회원 목록")
        print("3. 회원 삭제")
        print("4. 종료")
        return int(input("실행 메뉴 : "))

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == "1":
                print("회원가입")
            elif menu == "2":
                print("회원 목록")
            elif menu == "3":
                print("회원 삭제")
            elif menu == "4":
                print("종료")
Member.excute()