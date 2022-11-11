from flaskProject.titanic.models import TitanicModel
from flaskProject.util.dataset import Dataset


class TitanicController(object):
    def __init__(self):
        pass

    def __str__(self):
        return f""

    dataset = Dataset()
    model = TitanicModel()

    def preprocess(self, train, test) -> object:
        model = self.model
        this = self.dataset
        this.train = model.new_model(train)
        this.test = model.new_model(test)
        this.id = this.test['PassengerId']
        this = model.sex_nominal(this)
        this = model.age_ordinal(this)
        this = model.fare_ordinal(this)
        this = model.embarked_nominal(this)
        this = model.title_nominal(this)
        this = model.drop_features(this,
                                   'PassengerId', 'Name', 'Sex', 'Age',
                                   'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin')
        return this

    def modeling(self, train, test) -> object:
        model = self.model
        this = self.preprocess(train, test)
        this.label = model.create_label(this)
        this.train = model.create_train(this)
        return this

    def learning(self, train, test):
        this = self.modeling(train, test)
        accuracy = self.model.get_accuracy(this)
        accuracy_dt = self.model.get_decision(this)
        print(f'랜덤포레스트분류기 정확도 : {accuracy} % ')
        print(f'랜덤포레스트분류기 정확도 : {accuracy_dt} % ')
    def submit(self):
        pass

if __name__ =='__main__':
    c = TitanicController()
    this = Dataset()
    this = c.modeling('train.csv','test.csv')
    print(this.train.columns)
    print(this.train.head())
    print(this.lena)