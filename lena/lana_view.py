import cv2

from lena.lane_model import LenaModel
from util.dataset import Dataset


class LenaControll(object):
    dataset = Dataset()
    model = LenaModel()
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
    model = LenaModel()
    this = Dataset()
    this = model.new_lena_model()