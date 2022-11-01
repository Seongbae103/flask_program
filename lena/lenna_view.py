import cv2

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
        img = self.model.new_lena_model('lena.jpg')
        return img

    def modeling(self, fname):
        img = self.preprocess(fname)
        return img

if __name__ == '__main__':
    model = LennaModel()
    this = Dataset()
    this = model.new_lena_model()