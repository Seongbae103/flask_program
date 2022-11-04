import copy

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from const.path import HAAR
from mosaic.services import ImageToNumberArray, Haar, Hough, Mosaic
from util.dataset import Dataset
from util.lambdas import MoasicLambda


class LennaControll(object):


    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(*params):
        img = MoasicLambda('IMAGE_READ_FOR_CV', params[1])
        cv.imshow('원본', img)
        cv.waitKey(0)
        cv.destroyAllWindows()


    @staticmethod
    def menu_2(*params):
        arr = ImageToNumberArray(params[1])
        img = MoasicLambda('GRAY_SCALE', arr)
        img = MoasicLambda('IMAGE_FROM_ARRAY', img)
        plt.imshow(img)
        plt.show()

    @staticmethod
    def menu_3(*params):
        img = ImageToNumberArray(params[1])
        edges = cv.Canny(np.array(img), 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        img = ImageToNumberArray(params[1])
        edges = cv.Canny(img, 100, 200) #(imgae, threshold 1=100 ,threshold_2= 200)
        dst = Hough(edges)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Canny Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*params):
        print(params[0])
        cat = cv.imread(f"{Dataset().context}{params[1]}")
        mos = Mosaic(cat, (150, 150, 450, 450), 10)
        cv.imwrite(f'{Dataset().context}cat-mosaic.png', mos)
        cv.imshow('CAT MOSAIC', mos)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_6(*params):
        girl = params[1]
        img = MoasicLambda('IMAGE_READ_FOR_PLT', girl)

        gray = MoasicLambda("GRAY_SCALE", img)

        edges = cv.Canny(np.array(img), 10, 100)
        hough = Hough(edges)
        img_clone = copy.deepcopy(img)
        haar = Haar(HAAR, img)

        mos = Haar(haar, img, 10)

        plt.subplot(161), plt.imshow(img_clone, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(162), plt.imshow(gray, cmap='gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(163), plt.imshow(edges, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])
        plt.subplot(164), plt.imshow(hough, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(165), plt.imshow(haar, cmap='gray')
        plt.title('Haar'), plt.xticks([]), plt.yticks([])
        plt.subplot(166), plt.imshow(mos, cmap='gray')
        plt.title('mosaic'), plt.xticks([]), plt.yticks([])
        plt.show()
