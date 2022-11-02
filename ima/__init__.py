import cv2

from ima.v import View
from util.common import Common


if __name__ == '__main__':

    while True:
        menu = Common.menu(['종료', '원본', '??'])
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print('원본')
            img = View.modeling('canny.jpg')
            print(f' shape in {img.shape}')
            cv2.imshow('Gray', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()