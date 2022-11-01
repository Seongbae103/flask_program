from io import BytesIO

import cv as cv
import cv2
import numpy as np
import requests
from PIL import Image
from matplotlib import pyplot as plt

from lena.lenna_view import LennaControll
from util.common import Common


if __name__ == '__main__':

    api = LennaControll()
    while True:
        menu = Common.menu(["종료", "레나", "URL", "머신러닝", "배포"])
        if menu == "0":
            break
        elif menu == "1":
            print("### 원본 ###")
            this = api.modeling('lena.jpg')
            print(f' shape is {this.shape}')
            cv2.imshow('Gray', this)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        elif menu == "2":
            print("### 그레이 스케일 ###")

        elif menu == "3":
            print("### 엣지검출 ###")
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