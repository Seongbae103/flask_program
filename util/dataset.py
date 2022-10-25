from dataclasses import dataclass

@dataclass
class Dataset(object):

    context: str      # 파일이 저장된 경로
    fname: str        # 파일명
    train: object     # train.csv가 데이터프레임으로 전환된 객체
    test: object      # test.csv가 데이터프레임으로 전환된 객체
    id: str           # 승객id로 문제가 된다
    label: str        # 승객ID에 따른 생존여부로 답이 된다

    # 데이터를 읽고(getter = 프로퍼티) / 쓰기(setter) 기능을 추가한다.