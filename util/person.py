"""
이름, 주민번호 (950101-1), 주소를 입력받아서
회원명부를 관리하는 어플을 제작하고자 한다.
출력되는 결과는 다음과 같다.
### 자기소개서 ###
*******************************  *
이름 :
성별 :
나이 :
주소 :
********************************
"""
class Person(object):
    def __init__(self, name, num, addr):
        self.name = name
        self.num = num
        self.addr = addr
        self.gender =""
        self.set_age

    @staticmethod
    def print_menu():
        print("1. 등록")
        print("2. 조회")
        print("3. 탈퇴")
        print("4. 종료")
        return int(input("실행 : "))
    @staticmethod
    def new_person():
        name = input("이름 : ")
        num = input("주민번호 : ")
        addr = input("주소 : ")
        return Person(name, num, addr)

    def gender(self):
        gen = self.num[7]
        yy = int(self.num[:2])
        if gen == 1 or gen == 2:
            self.birth = yy + 1900

            if gen == 1:
                self.gender = "남자"
            elif gen == 2:
                self.gender = "여자"
        elif gen == 3 or gen == 4:
            self.birth = yy + 2000
            if gen == 3:
                self.gender = "남자"
            elif gen == 4:
                self.gender = "여자"

    @property
    def set_age(self):
        current = 2022
        return current - self.birth + 1

    def print_info(self):
        print("### 자기소개서 ###" 
              "\n ********************************" 
              f"\n 이름 : {self.name}" 
              f"\n 성별 : {self.gender}" 
              f"\n 나이 : {self.set_age}"
              f"\n 주소 : {self.addr}"
              "\n ********************************")
    @staticmethod
    def print_list(ls):
        [i.print_info() for i in ls]

    @staticmethod
    def delete(ls, name):
        del ls[[i for i, j in ls if j.name == name][0]]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Person.print_menu()
            if menu == 1:
                print("회원등록")
                ls.append(Person.new_person())
            elif menu == 2:
                print("주민 목록")
                Person.print_list(ls)
            elif menu == 3:
                print("삭제")
                Person.delete(ls, input("삭제할 이름 : "))
            elif menu == 4:
                print("종료")
Person.main()