import cv2

from util.dataset import Dataset


class LModel(object):
    detaset = Dataset()
    def __init__(self):
        pass
    def __str__(self):
        pass

    def new_model(self, fname):
        this = Dataset()
        this.context = './data/'
        img = cv2.imread(this.context + fname)
        return img

