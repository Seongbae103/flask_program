from flaskProject.src.dam.computer_vision.mosaic.service.mosaic_oop.views import MosaicControll

LENNA = "lenna.jpg"
SOCCER = "https://docs.opencv.org/4.x/roi.jpg"
BUILDING = "http://amroamroamro.github.io/mexopencv/opencv_contrib/fast_hough_transform_demo_01.png"
GIRL = 'girl.jpg'
GIRL_INCLINED = "girl_inclined.jpg"
GIRL_SIDE_FACE = 'girl_side_face.jpg'
GIRL_WITH_MOM = 'girl_with_mom.jpg'
CAT = "cat.jpg"

MENUS = ["종료", "원본", "그레이스케일", "엣지검출", "직선검출", "모자이크", "소녀 모자이크", "모녀 모자이크"]
mosaic_menu = {
    "1" : lambda t: t.menu_1(MENUS[1], LENNA),
    "2" : lambda t: t.menu_2(MENUS[2], SOCCER),
    "3" : lambda t: t.menu_3(MENUS[3], SOCCER),
    "4" : lambda t: t.menu_4(MENUS[4], BUILDING),
    "5" : lambda t: t.menu_5(MENUS[5], CAT),
    "6" : lambda t: t.menu_6(MENUS[6], GIRL),
    "7" : lambda t: t.menu_7(MENUS[7], GIRL_WITH_MOM)
}
def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')


if __name__ == '__main__':
    t = MosaicControll()
    while True:
        menu = my_menu(MENUS)
        if menu == 0:
            break
        else:
            try:
                mosaic_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")
