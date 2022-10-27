import pandas as pd

from util.dataset import Dataset


class TtareungyiModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        pass

    def preprocess(self):
        pass

    def new_model(self, fname):
        this = self.dataset
        this.context = './Data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    def create_train(self):
        pass

