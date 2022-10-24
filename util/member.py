'''
아이디, 비밀번호, 이름을 받아서
회원가입, 목록, 탈퇴하는 프로그램을 개발하시오.
'''

class Member(object):
    def __init__(self, name, num, id):
        self.name = name
        self.num = num
        self.id = id

    @staticmethod
    def print_menu():
        print("1. 회원가입")
        print("2. 회원 목록")
        print("3. 회원 삭제")
        print("4. 종료")
        return int(input("실행 메뉴 : "))

    @staticmethod
    def new_user():
        return Member(input("아이디 : "),
                  input("비밀번호 : "),
                   input("이름 : "))

    def print(self):
        print(f"{self.id} {self.num} {self.name}")
    @staticmethod
    def print_list(ls):
        print("###회원 명단###")
        print("************************")
        print("아이디 비밀번호 이름")
        print("************************")
        [i.print() for i in ls]
        print("************************")

    @staticmethod
    def delete(ls, id):
        del ls[[i for i, j in enumerate(ls) if j.id == id][0]]
    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 1:
                print("회원가입")
                ls.append(Member.new_user())
            elif menu == 2:
                print("회원 목록")
                Member.print_list(ls)
            elif menu == 3:
                print("회원 삭제")
                Member.delete(ls, input("아이디 : "))
            elif menu == 4:
                print("종료")
                break




Member.main()