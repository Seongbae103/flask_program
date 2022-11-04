from ima.m import LModel


class View(object):
    def __init__(self):
        pass
    def __str__(self):
        pass
    model = LModel()
    def preprocess(self, fname):
        img = self.model.new_model('mosaic.jpg')
        return img

    def modeling(self, fname):
        img = self.preprocess(fname)
        return img