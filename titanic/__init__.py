from flaskProject.titanic.template import Plot
from flaskProject.titanic.views import TitanicController
from flaskProject.util.common import Common

if __name__ == '__main__':
    api = TitanicController()
    while True:
        menu = Common.menu(["종료", "시각화", "모델링", "머신러닝", "배포"])
        if menu == "0": break
        elif menu == "1":
            print("### 시각화 ###")

            '''print(f' Train Type: {type(b)}')
            print(f' Train columns: {b.columns}')
            print(f' Train head: {b.head()}')
            print(f' Train null의 갯수: {b.null().sum()}')'''
            plot = Plot("train.csv")
            plot.draw_survived()
            plot.draw_pclass()
            plot.draw_sex()
            plot.draw_embarked()

        elif menu == "2":
            print("### 모델링 ###")
            df = api.modeling('train.csv', 'test.csv')
        elif menu == "3":
            print("### 머신러닝 ###")
            df = api.learning('train.csv', 'test.csv')
            # 랜덤포레스트 분류기
            # 결정트리 분류기
            # 로지스틱회귀
            # 서포트벡터머신
        elif menu == "4":
            print("### 배포 ###")
            df = api.submit('train.csv', 'test.csv')
        else: print("없는 메뉴")
