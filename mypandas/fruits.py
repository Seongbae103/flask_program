import pandas as pd

def fruits():
    ls1 = ['제품', '가격', '판매']
    ls2 = ['사과', '딸기', '수박']
    ls3 = [1800, 1500, 3000]
    ls4 = [24, 38, 13]
    column = [ls2, ls3, ls4]
    df = pd.DataFrame({j : column[i] for i, j in enumerate(ls1)})
    print(df)
    print('가격 평균 : '+ str(df['가격'].mean()))
    print('판매량 평균 : '+ str(df['판매'].mean()))

if __name__ == '__main__':
    fruits()