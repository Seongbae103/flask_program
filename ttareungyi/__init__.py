from ttareungyi.models import TtareungyiModel
from util.common import Common


while True:
    menu = Common.menu(["종료", "시각화", "모델링", "머신러닝", "배포"])
    if menu == "0": break
    elif menu == "1":
        print("### 시각화 ###")
        model = TtareungyiModel()
        mo = model.new_model("train.csv")
        print(f' Train Type: {type(mo)}')
        print(f' Train columns: {mo.columns}')
        print(f' Train head: {mo.head()}')
        print(f' Train null의 갯수: {mo.isnull().sum()}')

    elif menu == "2":
        print("### 모델링 ###")
    elif menu == "3":
        print("### 머신러닝 ###")
    elif menu == "4":
        print("### 배포 ###")
    else: print("없는 메뉴")