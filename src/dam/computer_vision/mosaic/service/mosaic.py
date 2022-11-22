import copy
from io import BytesIO
from PIL import Image

import cv2 as cv
import numpy as np
import requests


import matplotlib.pyplot as plt

from flaskProject.src.cmm.service.common import Common
from flaskProject.src.const.crawler import HEADERS
from flaskProject.src.const.path import CTX, HAAR
from flaskProject.src.dam.computer_vision.mosaic.service import LENNA, SOCCER, BUILDING, CAT, GIRL, GIRL_WITH_MOM
from flaskProject.src.utl.lambdas import MosaicLambda


def image_read(fname) -> object:
    return (lambda x: cv.imread(CTX+x))(fname)

def ImageToNumberArray(url):
    # URL = "https://upload.wikimedia.org/wikipedia/ko/2/24/Lenna.png"
        return np.array(Image.open(BytesIO(requests.get(url, headers=HEADERS).content)))

def Canny(param):
    return cv.Canny(np.array(param), 50, 51)

def Hough(param):
    lines = cv.HoughLinesP(param, 1, np.pi / 180., 10, minLineLength=50, maxLineGap=5)
    dst = cv.cvtColor(param, cv.COLOR_GRAY2BGR)
    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1])
            pt2 = (lines[i][0][2], lines[i][0][3])
            cv.line(dst, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
    return dst

def Haar(param):
    haar = cv.CascadeClassifier(CTX+HAAR)
    img_haar = haar.detectMultiScale(param, minSize=(150, 150))
    if len(img_haar) == 0:
        print("얼굴인식 실패")
        quit()
    for (x, y, w, h) in img_haar:
        print(f'얼굴의 좌표 : {x},{y},{w},{h}')
        cv.rectangle(param, (x, y), (x + w, y + h), (255, 0, 0), thickness=20)
    return (x, y, x + w, y + h)

def mosaic(*params):
    img = params[0]
    rect = params[1]
    size = params[2]
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]
    i_small = cv.resize(i_rect, (size, size))
    i_mos = cv.resize(i_small, (w, h), interpolation=cv.INTER_AREA)
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2


def Mosaics(img, size):
    haar = cv.CascadeClassifier(CTX+HAAR)
    dst = copy.deepcopy(img)
    face = haar.detectMultiScale(dst, minSize=(150, 150))
    for (x, y, w, h) in face:
        print(f'얼굴의 좌표 : {x},{y},{w},{h}')
        (x1, y1, x2, y2) = (x, y, (x+w), (y+h))
        w = x2 - x1
        h = y2 - y1
        i_rect = img[y1:y2, x1:x2]
        i_small = cv.resize(i_rect, (size, size))
        i_mos = cv.resize(i_small, (w, h), interpolation=cv.INTER_AREA)
        dst[y1:y2, x1:x2] = i_mos
    return dst

def GaussianBlur(src, sigmax, sigmay):
        # 가로 커널과 세로 커널 행렬을 생성
        i = np.arange(-4 * sigmax, 4 * sigmax + 1)
        j = np.arange(-4 * sigmay, 4 * sigmay + 1)
        # 가우시안 계산
        mask = np.exp(-(i ** 2 / (2 * sigmax ** 2))) / (np.sqrt(2 * np.pi) * sigmax)
        maskT = np.exp(-(j ** 2 / (2 * sigmay ** 2))) / (np.sqrt(2 * np.pi) * sigmay)
        mask = mask[:, np.newaxis]
        maskT = maskT[:, np.newaxis].T
        return filter2D(filter2D(src, mask), maskT)  # 두 번 필터링

'''
def Canny(src, lowThreshold, highThreshold):
        Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # x축 소벨 행렬로 미분
        Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])  # y축 소벨 행렬로 미분
        Ix = filter2D(src, Kx)
        Iy = filter2D(src, Ky)
        G = np.hypot(Ix, Iy)  # 피타고라스 빗변 구하기
        static = G / G.max() * 255  # 엣지를 그레이스케일로 표현
        D = np.arctan2(Iy, Ix)  # 아크탄젠트 이용해서 그래디언트를 구함
        M, N = static.shape
        Z = np.zeros((M, N), dtype=np.int32)  # 이미지 크기만큼의 행렬을 생성
        angle = D * 180. / np.pi  # 라디안을 degree로 변환(정확하지 않음)
        angle[angle < 0] += 180  # 음수일 때 180을 더함
        for i in range(1, M - 1):
            for j in range(1, N - 1):
                try:
                    q = 255
                    r = 255
                    # angle 0
                    if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                        q = static[i, j + 1]
                        r = static[i, j - 1]
                    # angle 45
                    elif (22.5 <= angle[i, j] < 67.5):
                        q = static[i + 1, j - 1]
                        r = static[i - 1, j + 1]
                    # angle 90
                    elif (67.5 <= angle[i, j] < 112.5):
                        q = static[i + 1, j]
                        r = static[i - 1, j]
                    # angle 135
                    elif (112.5 <= angle[i, j] < 157.5):
                        q = static[i - 1, j - 1]
                        r = static[i + 1, j + 1]
                    if (static[i, j] >= q) and (static[i, j] >= r):  # 주변 픽셀(q, r)보다 크면 static 행렬의 값을 그대로 사용
                        Z[i, j] = static[i, j]
                    else:  # 그렇지 않을 경우 0을 사용
                        Z[i, j] = 0
                except IndexError as e:  # 인덱싱 예외 발생 시 pass
                    pass
        M, N = static.shape
        res = np.zeros((M, N), dtype=np.int32)
        weak = np.int32(25)  # 약한 에지
        strong = np.int32(255)  # 강한 에지
        # 이중 임곗값 비교
        # 최대 임곗값보다 큰 원소의 인덱스를 저장
        strong_i, strong_j = np.where(static >= highThreshold)
        # 최소 임곗값보다 작은 원소의 인덱스를 저장
        zeros_i, zeros_j = np.where(static < lowThreshold)
        # 최소 임곗값과 최대 임곗값 사이에 있는 원소의 인덱스를 저장
        weak_i, weak_j = np.where((static <= highThreshold) & (static >= lowThreshold))
        # 각각 강한 에지와 약한 에지의 값으로 저장
        res[strong_i, strong_j] = strong
        res[weak_i, weak_j] = weak
        for i in range(1, M - 1):
            for j in range(1, N - 1):
                if (static[i, j] == weak):
                    try:
                        if ((static[i + 1, j - 1] == strong) or (static[i + 1, j] == strong) or (static[i + 1, j + 1] == strong)
                                or (static[i, j - 1] == strong) or (static[i, j + 1] == strong)
                                or (static[i - 1, j - 1] == strong) or (static[i - 1, j] == strong) or (
                                        static[i - 1, j + 1] == strong)):  # 강한 에지와 연결 되어있을 때
                            static[i, j] = strong  # 연결되어 있는 에지 또한 강한 에지가 됨
                        else:  # 연결되어 있지 않을 때
                            static[i, j] = 0  # 에지가 없는 0으로 설정
                    except IndexError as e:
                        pass
        return static
'''
def filter2D(src, kernel, delta=0):
    # 가장자리 픽셀을 (커널의 길이 // 2) 만큼 늘리고 새로운 행렬에 저장
    halfX = kernel.shape[0] // 2
    halfY = kernel.shape[1] // 2
    cornerPixel = np.zeros((src.shape[0] + halfX * 2, src.shape[1] + halfY * 2), dtype=np.uint8)

    # (커널의 길이 // 2) 만큼 가장자리에서 안쪽(여기서는 1만큼 안쪽)에 있는 픽셀들의 값을 입력 이미지의 값으로 바꾸어 가장자리에 0을 추가한 효과를 봄
    cornerPixel[halfX:cornerPixel.shape[0] - halfX, halfY:cornerPixel.shape[1] - halfY] = src

    dst = np.zeros((src.shape[0], src.shape[1]), dtype=np.float64)

    for y in np.arange(src.shape[1]):
        for x in np.arange(src.shape[0]):
            # 필터링 연산
            dst[x, y] = (kernel * cornerPixel[x: x + kernel.shape[0], y: y + kernel.shape[1]]).sum() + delta
    return dst


def Hough(edges):
    lines = cv.HoughLinesP(edges, 1, np.pi / 180., 120, minLineLength=50, maxLineGap=5)
    hough = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
    if lines is not None:
        for i in range(lines.shape[0]):
            pt1 = (lines[i][0][0], lines[i][0][1])
            pt2 = (lines[i][0][2], lines[i][0][3])
            cv.line(hough, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
    return hough


def Haar(param):
    haar = cv.CascadeClassifier(CTX+HAAR)
    haar_img = haar.detectMultiScale(param, minSize=(150, 150))
    if len(haar_img) == 0:
        print("얼굴인식 실패")
        quit()
    for (x, y, w, h) in haar_img:
        print(f'얼굴의 좌표 : {x},{y},{w},{h}')
        cv.rectangle(param, (x, y), (x + w, y + h), (255, 0, 0), thickness=20)
    return (x, y, x + w, y + h)


def Mosaic(*params):
    img = params[0]
    rect = params[1]
    size = params[2]
    (x1, y1, x2, y2) = rect
    w = x2 - x1
    h = y2 - y1
    i_rect = img[y1:y2, x1:x2]
    i_small = cv.resize(i_rect, (size, size))
    i_mos = cv.resize(i_small, (w, h), interpolation=cv.INTER_AREA)
    img2 = img.copy()
    img2[y1:y2, x1:x2] = i_mos
    return img2


def Mosaics(img, size):
    haar = cv.CascadeClassifier(CTX+HAAR)
    dst = copy.deepcopy(img)
    face = haar.detectMultiScale(dst, minSize=(150, 150))
    for (x, y, w, h) in face:
        print(f'얼굴의 좌표 : {x},{y},{w},{h}')
        (x1, y1, x2, y2) = (x, y, (x+w), (y+h))
        w = x2 - x1
        h = y2 - y1
        i_rect = img[y1:y2, x1:x2]
        i_small = cv.resize(i_rect, (size, size))
        i_mos = cv.resize(i_small, (w, h), interpolation=cv.INTER_AREA)
        dst[y1:y2, x1:x2] = i_mos
    return dst


def image_read(fname) -> object:
    return (lambda x: cv.imread(CTX+x))(fname)
class MosaicControll(object):
    @staticmethod
    def menu_0(*params):
        print(params[0])

    @staticmethod
    def menu_1(*params):
        img = MosaicLambda('IMAGE_READ_FOR_CV', params[1])
        cv.imshow('원본', img)
        cv.waitKey(0)
        cv.destroyAllWindows()


    @staticmethod
    def menu_2(*params):
        arr = ImageToNumberArray(params[1])
        img = MosaicLambda('GRAY_SCALE', arr)
        img = MosaicLambda('IMAGE_FROM_ARRAY', img)
        plt.imshow(img)
        plt.show()

    @staticmethod
    def menu_3(*params):
        img = ImageToNumberArray(params[1])
        img_canny = cv.Canny(np.array(img), 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img_canny, cmap='gray')
        plt.title('CANNY'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        img_canny = cv.Canny(img, 100, 200)  # (image, threshold 1=100, threshold 2=200)
        img_hough = Hough(img_canny)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img_hough, cmap='gray')
        plt.title('hough'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*params):
        print(params[0])
        img_cat = cv.imread(CTX+params[1])
        img_mosaic = Mosaic(img_cat, (150, 150, 450, 450), 10)
        cv.imwrite(CTX +'cat-mosaic.png', img_mosaic)
        cv.imshow('CAT MOSAIC', img_mosaic)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_6(*params):
        girl = params[1]
        img = MosaicLambda('IMAGE_READ_FOR_PLT', girl)

        gray = MosaicLambda("GRAY_SCALE", img)

        img_canny = Canny(img)
        img_hough = Hough(img_canny)
        img_clone = copy.deepcopy(img)
        rect = Haar(img_clone)

        img_mosaic = Mosaic(img, rect, 10)

        plt.subplot(161), plt.imshow(img, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(162), plt.imshow(gray, cmap='gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(163), plt.imshow(img_canny, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])
        plt.subplot(164), plt.imshow(img_hough, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(165), plt.imshow(img_clone, cmap='gray')
        plt.title('Haar'), plt.xticks([]), plt.yticks([])
        plt.subplot(166), plt.imshow(img_mosaic, cmap='gray')
        plt.title('mosaic'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_7(*params):
        print(params[0])
        img = MosaicLambda('IMAGE_READ_FOR_CV', params[1])
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img_mosaic = Mosaics(img, 10)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img_mosaic, cmap='gray')
        plt.title('Mosaic Image'), plt.xticks([]), plt.yticks([])
        plt.show()

if __name__ == '__main__':
    api = MosaicControll()
    while True:
        menus = ["종료",
                 "원본보기","그레이스케일","엣지검출","직선검출","모자이크",
                 "소녀 모자이크","모녀 모자이크"]
        menu = Common.menu(menus)
        if menu == "0":
            api.menu_0(menus[0])
            break
        elif menu == "1": api.menu_1(menus[1], LENNA)
        elif menu == "2": api.menu_2(menus[2], SOCCER)
        elif menu == "3": api.menu_3(menus[3], SOCCER)
        elif menu == "4": api.menu_4(menus[4], BUILDING)
        elif menu == "5": api.menu_5(menus[5], CAT)
        elif menu == "6": api.menu_6(menus[6], GIRL)
        elif menu == "7": api.menu_7(menus[7], GIRL_WITH_MOM)
        else:
            print(" ### 해당 메뉴 없음 ### ")