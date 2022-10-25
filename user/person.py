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
        self.age = 0

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
            return self.birth

    def set_age(self):
        current = 2022
        self.age = current - self.birth + 1

    def __str__(self):
        return f"{self.name} {self.gender} {self.age} {self.addr}"

    @staticmethod
    def print_list(ls):
        print("************************************")
        print("이름 성별 나이 주소")
        print("************************************")
        [print(i) for i in ls]
        print("************************************")

    @staticmethod
    def delete(ls, name):
        del ls[[i for i, j in ls if j.name == name][0]]

