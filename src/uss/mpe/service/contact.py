
class Contact(object):
    def __init__(self, name, pnum, mail, addr):
        self.name = name
        self.pnum = pnum
        self.mail = mail
        self.addr = addr

    def __str__(self):
        return f"{self.name} {self.pnum} {self.mail} {self.addr}"

    @staticmethod
    def new_contact():
        name = input("이름 : ")
        pnum = input("연락처 : ")
        mail = input("이메일 :")
        addr = input("주소 : ")
        return Contact(name, pnum, mail, addr)

    @staticmethod
    def print_result(ls):
        print("### 연락처 ###")
        print("**********************")
        print("이름 연락처 이메일 주소")
        print("**********************")
        [print(i) for i in ls]
        print("**********************")
    @staticmethod
    def delete(ls, name):
        del ls[[i for i, j in enumerate(ls) if j.name == name]]
