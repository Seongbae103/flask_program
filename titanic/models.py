import pandas as pd

from util.dataset import Dataset

'''
 ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
         'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
         === null 값 ===
         age    177
         cabin  687
         Embark   2
   '''

class TitanicModel(object):

    dataset = Dataset()

    def __init__(self):
        pass

    def __str__(self):
        b = self.new_model(self.dataset.fname)
        return f'Train Type: {type(b)}\n' \
               f'Train columns: {b.column()}\n' \
               f'Train head: {b.head()}\n' \
               f'Train null의 갯수: {b.isnull().sum()}'

    def preprocess(self):
        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './Data/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) ->object:
        pass

    def create_label(self):
        pass