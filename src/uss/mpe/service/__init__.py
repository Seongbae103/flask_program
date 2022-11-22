from flaskProject.src.cmm.service.common import Common
from flaskProject.src.uss.mpe.service.bmi import Bmi
from flaskProject.src.uss.mpe.service.contact import Contact
from flaskProject.src.uss.mpe.service.grade import Grade
from flaskProject.src.uss.mpe.service.person import Person

ast = "*"*40
ls = []
while True:
    menu = Common.menu(["종료", "BMI", "주소록", "성적표", "개인정보"])
    if menu == "0":
        print("종료")
        break
    elif menu == "1":
        print("###BMI###")
        submenu = Common.menu(["종료", "BMI 등록", "BMI 목록", "BMI 삭제"])
        if submenu == "0": break
        elif submenu == "1":
            biman = Bmi.new_user()
            ls.append(biman)
        elif submenu == "2":
            Bmi.print_result(ls)
        elif submenu == "3":
            Bmi.delete(ls, input("삭제할 이름 : "))
    elif menu == "2":
        print("###주소록###")
        submenu = Common.menu(["종료", "주소 등록", "주소 목록", "주소 삭제"])
        if submenu == "0": break
        elif submenu == "1":
            print("주소 등록")
            ls.append(Contact.new_contact())
        elif menu == "2":
            print("주소 목록")
            Contact.print_result(ls)
        elif menu == "3":
            print("주소 삭제")
            Contact.delete(ls, input("삭제할 주소 : "))
        else:
            print("잘못된 입력")
    elif menu == "3":
        print("###성적표###")
        submenu = Common.menu(["종료", "성적 등록", "성적 목록", "성적 삭제"])
        if submenu == "0": break
        elif submenu == "1":
            print("성적 등록")
            ls.append(Grade.new_test())
        elif submenu == "2":
            print("성적 출력")
            Grade.print_result(ls)
        elif submenu == "3":
            print("성적 삭제")
            Grade.delete(ls, input("삭제할 이름 : "))
        else:
            print("잘못된 입력")
    elif menu == "4":
        print("###개인정보###")
        submenu = Common.menu(["종료", "개인정보 등록", "개인정보 목록", "개인정보 삭제"])
        if submenu == "0": break
        elif submenu == "1":
            print("개인정보 등록")
            ls.append(Person.new_person())
        elif submenu == "2":
            print("개인정보 목록")
            Person.print_list(ls)
        elif submenu == "3":
            print("개인정보 삭제")
            Person.delete(ls, input("삭제할 이름 : "))
        else: print("잘못된 메뉴")
    else:
        print("잘못된 메뉴")
