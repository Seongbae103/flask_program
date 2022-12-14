from flaskProject.ml.stroke import STROKE_MENUS, stroke_menu
from flaskProject.ml.stroke import StrokeService
from flaskProject.ml.oklahoma import OKLAHOMA_MENUS, oklahoma_menu, Oklahoma


def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = Oklahoma()
    while True:
        menu = my_menu(OKLAHOMA_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                oklahoma_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")
