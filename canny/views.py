import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from canny.services import ImageToNumberArray, image_read, ExcuteLambda, Haar, Hough
from util.dataset import Dataset


class LennaControll(object):


    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(*params):
        img = ExcuteLambda('IMAGE_READ', params[1])
        cv.imshow('원본', img)
        cv.waitKey(0)
        cv.destroyAllWindows()


    @staticmethod
    def menu_2(*params):
        arr = ImageToNumberArray(params[1])
        img = ExcuteLambda('GRAY_SCALE', arr)
        img = ExcuteLambda('IMAGE_FROM_ARRAY', img)
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
        print(params[0])
        img = ImageToNumberArray(params[1])
        edges = cv.Canny(img, 100, 200) #(imgae, threshold 1=100 ,threshold_2= 200)
        dst = Hough(edges)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*params):
        ds = Dataset()
        haar = cv.CascadeClassifier(f"{ds.context}{params[1]} ")
        girl = params[2]
        img = cv.cvtColor(ExcuteLambda('IMAGE_READ', girl), cv.COLOR_BGR2RGB)
        plt.subplot(151), plt.imshow(img, cmap='gray')
        plt.title('img'), plt.xticks([]), plt.yticks([])
        gray = ExcuteLambda("GRAY_SCALE", img)

        edges = cv.Canny(np.array(img), 10, 100)

        lines = cv.HoughLinesP(edges, 1, np.pi / 180., 20, minLineLength=30, maxLineGap=5)
        dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
        face = haar.detectMultiScale(img, minSize=(150, 150))

        Haar(dst, face, img, lines)

        plt.subplot(152), plt.imshow(gray, cmap='gray')
        plt.title('gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(153), plt.imshow(edges, cmap='gray')
        plt.title('edge'), plt.xticks([]), plt.yticks([])
        plt.subplot(154), plt.imshow(dst, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(155), plt.imshow(img, cmap='gray')
        plt.title('haar'), plt.xticks([]), plt.yticks([])
        plt.show()



    @staticmethod
    def menu_6(*params):
        pass




