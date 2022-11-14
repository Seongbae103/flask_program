from flaskProject.mypandas.mpg import Mpg, MENUS
def my_menu(MENUS):
    for i, j in enumerate(MENUS):
        print(f' {i}. {j}')
    return input('실행 : ')
if __name__ == '__main__':
    t = Mpg()
    while True:
        menu = Mpg.my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                Mpg.switch[menu](t)
            except KeyError:
                print(" ### Error ### ")