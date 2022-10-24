class Grade(object):
    def __init__(self, name, ko, en, ma):
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.total()
        self.avg()
        self.print()

    def total(self):
        return self.ko + self.en + self.ma

    def avg(self):
        return self.total() / 3

    def set_grade(self):
        avg = self.avg()
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "c"
        elif avg >= 60:
            grade = "D"
        elif avg >= 50:
            grade = "E"
        else: grade = "F"
        return grade

    def print(self):
        print(f"{self.name} {self.ko} {self.en} {self.ma} {self.total()} {self.avg()} {self.set_grade()}")

    @staticmethod
    def print_menu():
        print("1. 성적 등록")
        print("2. 성적 출력")
        print("3. 성적 삭제")
        print("4. 종료")
        return int(input("실행 메뉴 : "))
    @staticmethod
    def new_test():
        return Grade(input("이름 : "),
                     int(input("국어 : ")),
                     int(input("영어 : ")),
                     int(input("수학 : ")))
    @staticmethod
    def print_result(ls):
        print(f"### 성적 ###")
        print("*********************")
        print("이름 국어 영어 수학 총점 평균")
        print("*********************")
        for i in ls:
            i.print()
        print("*********************")

    @staticmethod
    def delete(ls, name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Grade.print_menu()
            if menu == 1:
                print("성적 등록")
                ls.append(Grade.new_test())
            elif menu == 2:
                print("성적 출력")
                Grade.print_result(ls)
            elif menu == 3:
                print("성적 삭제")
                Grade.delete(ls, input("삭제할 이름 : "))
            elif menu == 4:
                print("종료")
                break

Grade.main()