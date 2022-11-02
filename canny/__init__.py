from io import BytesIO

import cv as cv
import cv2
import menu as menu
import numpy as np
import requests
from PIL import Image
from matplotlib import pyplot as plt

from canny.views import LennaControll
from util.common import Common
LENNA = "lena.jpg"
SOCCER = "https://docs.opencv.org/4.x/roi.jpg"
BUILDING ="http://amroamroamro.github.io/mexopencv/opencv_contrib/fast_hough_transform_demo_01.png"
if __name__ == '__main__':

    api = LennaControll()
    while True:
        menus = ["종료", "원본", "그레이스케일", "엣지검출", "직선검출"]
        menu = Common.menu(menus)
        if menu == 0:
            break
        elif menu == "1":
            print("### 원본 ###")
            api.menu_1(menus[1], LENNA)

        elif menu == "2":
            print("### 그레이 스케일 ###")
            api.menu_2(menus[2], SOCCER)

        elif menu == "3":
            print("### 엣지검출 ###")
            api.menu_3(menus[3], SOCCER)

        elif menu =="4":
            print("###직선 검출###")
            api.menu_4(menus[4], BUILDING)
        elif menu == "9":
            print("### 테스트 ###")
            fname = 'https://docs.opencv.org/4.x/roi.jpg'
            img = Image.open(BytesIO(requests.get(fname, headers={'User-Agent': 'My User Agent 1.0'}).content))
            img = np.array(img)
            edges = cv2.Canny(img, 100, 200)
            plt.subplot(121), plt.imshow(img, cmap='gray')
            plt.title('Original Image'), plt.xticks([]), plt.yticks([])
            plt.subplot(122), plt.imshow(edges, cmap='gray')
            plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
            plt.show()

        else:
            print("없는 메뉴")