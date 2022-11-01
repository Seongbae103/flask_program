import cv2

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
        elif menu == "4":
            print("### 배포 ###")
        else:
            print("없는 메뉴")