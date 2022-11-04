from io import BytesIO

import cv2 as cv

import menu as menu
import numpy as np
import requests
from PIL import Image
from matplotlib import pyplot as plt

from const.path import HAAR
from mosaic.views import LennaControll
from util.common import Common
LENNA = "lena.jpg"
SOCCER = "https://docs.opencv.org/4.x/roi.jpg"
BUILDING ="http://amroamroamro.github.io/mexopencv/opencv_contrib/fast_hough_transform_demo_01.png"

GIRL = 'girl.jpg'
GIRL_INCLINED = "girl_inclined.jpg"
GIRL_SIDE_FACE = 'girl_side_face.jpg'
Girl_WITH_MOM = 'girl_with_mom.jpg'
CAT = "cat.jpg"

if __name__ == '__main__':

    api = LennaControll()

    while True:
        menus = ["종료", "원본", "그레이스케일", "엣지검출", "직선검출", "모자이크", "소녀 모자아크"]
        menu = Common.menu(menus)
        if menu == 0:
            break
        elif menu == "1":
            api.menu_1(menus[1], LENNA)

        elif menu == "2":
            api.menu_2(menus[2], SOCCER)

        elif menu == "3":
            api.menu_3(menus[3], SOCCER)

        elif menu =="4":
            api.menu_4(menus[4], BUILDING)

        elif menu =="5":
            api.menu_5(menus[5], CAT)

        elif menu == "6":
            api.menu_6(menus[6], GIRL)

        elif menu == "7":
            api.menu_7(menus[7])
        else:
            print("없는 메뉴")