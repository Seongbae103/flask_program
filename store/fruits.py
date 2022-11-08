import pandas as pd

def fruits():
    ls1 = ['제품', '가격', '판매']
    ls2 = ['사과', '딸기', '수박', '평균']
    ls3 = [1800, 1500, 3000]
    ls4 = [24, 38, 13]
    column = [ls2, ls3, ls4]
    ls3.append(sum(ls3)/len(ls3))
    ls4.append(sum(ls4)/len(ls4))
    dc = {j : column[i] for i, j in enumerate(ls1)}
    df = pd.DataFrame(dc)
    print(df)

if __name__ == '__main__':
    fruits()