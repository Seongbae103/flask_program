import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from flaskProject.src.cmm.service.dataset import Dataset
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
'''
['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
시각화를 동해 얻은 상관관계 변수(veriable = feature =column)는
Pclass
Sex
Age
Fare
Embarked
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
        this.context = './../../../../../static/data/dam_titanic/'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) ->object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_features(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop(i, axis = 1)
            this.test = this.test.drop(i, axis = 1)
        return this

    @staticmethod
    def sex_nominal(this):
        for i in [this.train, this.test]:
            i['Gender'] = i['Sex'].map({"male": 0, "female": 1})
        return this
    @staticmethod
    def age_ordinal(this):
        for i in [this.train, this.test]:
            i['Age'] = i['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 68, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4, 'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for i in [this.train, this.test]:
            i['AgeGroup'] = pd.cut(i['Age'], bins=bins, labels=labels)
            i['AgeGroup'] = i['AgeGroup'].map(age_mapping)
        return this

    @staticmethod
    def fare_ordinal(this):
        for i in [this.train, this.test]:
           i['FareBand'] = pd.qcut(i['Fare'], 4, labels={1, 2, 3, 4})
        return this

    @staticmethod
    def embarked_nominal(this):

        this.train = this.train.fillna({"Embarked": 'S'})
        this.test = this.test.fillna({"Embarked": 'S'})
        for i in [this.train, this.test]:
            i['Embarked'] = i['Embarked'].map({"S" : 1, "C" : 2, "Q" : 3})
        return this

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        for i in combine:
            i['Title'] = i.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for i in combine:
            i['Title'] = i['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            i['Title'] = i['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'],
                                            'Rare')
            i['Title'] = i['Title'].replace('Mlle', 'Mr')
            i['Title'] = i['Title'].replace('Ms', 'Miss')
            i['Title'] = i['Title'].fillna(0)
            i['Title'] = i['Title'].map({
                'Mr': 1,
                'Miss': 2,
                'Mrs': 3,
                'Master': 4,
                'Royal': 5,
                'Rare': 6
            })
        return this

    @staticmethod
    def create_k_fole():
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def get_accuracy(this):
        score = cross_val_score(RandomForestClassifier(),
                                this.train,
                                this.label,
                                cv = TitanicModel.create_k_fole(),
                                n_jobs=1,
                                scoring='accuracy')
        return round(np.mean(score)*100,2)

    @staticmethod
    def get_decision(this):
        dt = DecisionTreeClassifier(random_state=11)
        dt.fit(this.train, this.label)
        dt = dt.predict(this.train)
        print('결정트리 정확도: {0:.4f}'.format(accuracy_score(this.label, dt)))

    @staticmethod
    def get_logistic(this):
        logi = LogisticRegression()
        logi.fit(this.train, this.label)
        lr_pred = logi.predict(this.train)
        print('로지스틱 회귀 정확도: {0:.4f}'.format(accuracy_score(this.label, lr_pred)))

if __name__ =='__main__':
    t = TitanicModel()
    this = Dataset()
    this.train = t.new_model('train.csv')
    this.test = t.new_model('test.csv')
    this = TitanicModel.sex_nominal(this)
    this = TitanicModel.fare_ordinal(this)
    this = TitanicModel.embarked_nominal(this)
    this = TitanicModel.age_ordinal(this)
    print(this.train.columns)
    print(this.train['Age'].isnull().sum())
    print(this.train.head())