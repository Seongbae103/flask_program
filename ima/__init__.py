import cv2

from util.common import Common

if __name__ == '__main__':
    while True:
        menu = Common.menu(['종료', '원본', '??'])
        if menu == "0":
            print("종료")
            break
        elif menu == "1":
            print('원본')

            a = cv2.imread('./data/lena.jpg', cv2.IMREAD_COLOR)
            print(f' shape in {a.shape}')
            cv2.imshow('Gray', a)
            cv2.waitKey(0)
            cv2.destroyAllWindows()