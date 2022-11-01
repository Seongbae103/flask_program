import cv2
from matplotlib import pyplot as plt

from lena.lenna_model import LennaModel
from util.dataset import Dataset


class LennaControll(object):
    dataset = Dataset()
    model = LennaModel()
    def __init__(self):
        pass
    def __str__(self):
        pass

    def preprocess(self, fname) -> object:
        img = self.model.new_lena_model('https://docs.opencv.org/4.x/roi.jpg')
        return img

    def modeling(self, fname):
        img = self.preprocess(fname)
        return img

    def canny(self):
        edges = cv2.Canny(self.img, 100, 200)
        plt.Subplot(121), plt.imshow(self.img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        plt.show()


if __name__ == '__main__':
    model = LennaModel()
    this = Dataset()
    this = model.new_lena_model()