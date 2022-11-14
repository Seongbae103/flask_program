import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from flaskProject.ml.stroke import stroke_meta


class StrokeService:
    def __init__(self):
        self.stroke = pd.read_csv('./data/healthcare-dataset-stroke-data.csv')
        self.my_stroke = None
    '''
    1.스펙보기
    '''
    def menu_1(self):
        print(" --- 1.Shape ---")
        print(self.stroke.shape)
        print(" --- 2.Features ---")
        print(self.stroke.columns)
        print(" --- 3.Info ---")
        print(self.stroke.info())
        print(" --- 4.Case Top1 ---")
        print(self.stroke.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(self.stroke.tail(3))
        print(" --- 6.Describe ---")
        print(self.stroke.describe())
        print(" --- 7.Describe All ---")
        print(self.stroke.describe(include='all'))
    '''
    2.한글 메타데이터
    '''
    def menu_2(self):
        self.my_stroke = self.stroke.rename(columns=stroke_meta)
        return self.my_stroke

    '''
    3. 타깃변수(=종속변수 dependent, y값) 설정
    입력변수(= 설명변수, 확률변수, X값)
    타깃변수명 :stroke (=뇌졸중)
    타깃 변수값 : 과거에 한 번이라도 뇌졸중이 발병했으면 1, 아니면 0
    '''
    def menu_3(self):
        print(self.my_stroke['아이디'].dtypes)
        print(self.my_stroke['아이디'].isnull().sum())
        print(len(pd.unique(self.my_stroke['아이디'])))
        print(self.my_stroke['뇌졸중'].dtype)
        print(self.my_stroke['뇌졸중'].isnull().sum())
        print(self.my_stroke['뇌졸중'].value_counts(dropna=False, normalize=True))

    def menu_4(self):
        df= self.my_stroke
        cols = ['나이', '평균 혈당', '체질량지수']
        print(df[cols].dtypes)
        pd.options.display.float_format = '{:.2f}'.format
        print(df[cols].describe())
        c = df['나이'] > 18
        print(df[c].head(3))
        len(df[c])
        print(len(df[c])/ len(df))
        df1 = df[c]
        df1 = df1.rename(columns={'Residence_type': 'residence_type'})
        print(df1.shape)
        cols1 = ['성별', '고혈압', '심장병', '기혼여부', '직종', '거주형태', '흡연 여부']
        print(df1[cols1].isnull().sum())
        print(df1.isna().any()[lambda x: x])
        print(df['체질량지수'].isnull().mean())
        print(df1[cols].describe())
        print(df1[cols].skew())
        print(df1[cols].kurtosis())
        print(df1['직종'].value_counts(dropna=False))
        print(pd.crosstab(df1['직종'], columns= 'count'))
        print(pd.crosstab(df1['직종'], columns= 'ratio', normalize=True))
        print(pd.crosstab(df1['직종'], df1['뇌졸중']))
        print(pd.crosstab(df1['직종'], df1['뇌졸중'], normalize = True))
        '''이상값 제거(p.83)'''
        fig, axes = plt.subplots(1, 3, figsize=(15,4))
        sns.histplot(ax=axes[0], data=df, x="나이", kde=True, bins=20)
        sns.histplot(ax=axes[1], data=df, x="평균 혈당", kde=True, bins=20)
        sns.histplot(ax=axes[2], data=df, x="체질량지수", kde=True, bins=20)
        plt.show()
        '''구간 변수상자(p86)'''
        sns.boxplot(ax=axes[0], x="나이", data=df1)
        sns.boxplot(ax=axes[1], x="평균 혈당", data=df1)
        sns.boxplot(ax=axes[2], x="체질량지수", data=df1)
        '''구간변수의 IQR계산 (p.86)'''
        Q1 = df1[['나이', '평균 혈당', '체질량지수']].quantile(0.25)
        Q3 = df1[['나이', '평균 혈당', '체질량지수']].quantile(0.75)
        IQR = Q3 - Q1
        print(IQR)
        '''IQR 상한, 하한'''
        Lower = Q1-3.0*IQR
        Upper = Q3+3.0*IQR
        print(Lower)
        print(Upper)
        c1 = df1['평균 혈당'] <= 232.64
        c2 = df1['체질량지수'] <= 60.3
        df2 = df1[c1 & c2]
        print(df2.shape)
        '''상관계수 검토'''
        print('이상치 제거한 성인개체')
        round(df2[cols].corr(),2)
        corr = df2[cols].corr()
        annot_kws ={"ha" : 'center', "va": 'top'}
        sns.heatmap(data=corr, annot= True, annot_kws=annot_kws, cmap="YlGnBu")
        df2.to_csv('healthcare-dataset-stroke-data.csv', index=False)

    '''
    5. 시각화
    '''
    def menu_5(self):
        df = self.my_stroke
        '''나이에 대한 그래프'''
        print(sns.histplot(data=df, x='나이', hue="뇌졸중", bins=20))
        '''나이의 타깃변수'''
        sns.set_style('whitegrid')
        print(sns.boxplot(x='뇌졸중', y='나이', data=df))
        '''각 상자의 평균'''
        group = df['나이'].groupby(df['뇌졸중'])
        print(group.mean())
        plt.show()
        df.to_csv("./save/stroke.csv", index=False)
