import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

OKLAHOMA_MENUS = ["exit", #0
                "data",#1
                "rename",#2
                "interval",#3 18세이상만 사용함
                "ratio",#4
                "nominal",#5
                "ordinal",#6
                "학습",#7
                "예측"]#8
oklahoma_meta = {
    'ACCESS' : 'ACCESS',
    'ACR' : 'ACR',
    'AGEP' : '나이',
    'BATH' : 'BATH',
    'BDSP' : '침실수',
    'BLD' : 'BLD',
    'CONP' : 'CONP',
    'COW' : 'COW',
    'ELEP' : '월전기료',
    'FESRP' : 'FESRP',
    'FKITP' : 'FKITP',
    'FPARC' : 'FPARC',
    'FSCHP' : 'FSCHP',
    'FTAXP' : 'FTAXP',
    'GASP' : '월가스비',
    'HHL' : 'HHL',
    'HHT' : 'HHT',
    'HINCP' : '가계소득',
    'ANX' : 'ANX',
    'MAR' : 'MAR',
    'MV' : 'MV',
    'NRC' : '자녀수',
    'R18' : 'R18',
    'R65' : 'R65',
    'RAC1P' : 'RAC1P',
    'RMSP' : '방수',
    'RWAT' : 'RWAT',
    'SCH' : 'SCH',
    'SCHL' : 'SCHL',
    'SEX' : 'SEX',
    'VALP' : '주택가격',
    'VALP_B1' : '지하주택가격'
    }
oklahoma_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.rename_meta(),
    "3" : lambda t: t.interval(),
    "4" : lambda t: t.ratio(),
    "5" : lambda t: t.nominal(),
    "6" : lambda t: t.ordinal(),
    "7" : lambda t: t.target()
}
class Oklahoma():
    def __init__(self):
        self.oklahoma = pd.read_csv('./data/comb32.csv')
        self.oklahoma_home = None

    def spec(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        ok = self.oklahoma
        print(" --- 1.Shape ---")
        print(ok.shape)
        print(" --- 2.Features ---")
        print(ok.columns)
        print(" --- 3.Info ---")
        print(ok.info())
        print(" --- 4.Case Top1 ---")
        print(ok.head(1))
        print(" --- 5.Case Bottom1 ---")
        print(ok.tail(3))
        print(" --- 6.Describe ---")
        print(ok.describe())
        print(" --- 7.Describe All ---")
        print(ok.describe(include='all'))

    def rename_meta(self):
        self.oklahoma_home = self.oklahoma.rename(columns=oklahoma_meta)
        return self.oklahoma_home

    def interval(self):
        ok_home = self.oklahoma
        pd.options.display.float_format = '{:.2f}'.format
        cols1 = ['나이','침실수','CONP','월전기료','월가스비','가계소득','자녀수','방수','주택가격']
        print(ok_home[cols1].describe())
        print(ok_home[cols1].skew())
        print(ok_home[cols1].kurtosis())
        print(ok_home[cols1].value_counts())
        pd.options.display.float_format='{:.3f}'.format
        print(ok_home['CONP'].value_counts())
        ok_home.drop('CONP', axis=1, inplace=True)
        print(ok_home.shape)

        '''이상값 제거'''
        '''산포도'''
        df1 = ok_home[["침실수", '자녀수', '방수', '주택가격']]
        g = sns.PairGrid(df1)
        g.map_diag(sns.histplot)
        g.map_offdiag(sns.scatterplot)
        '''IQR계산'''
        Q1 = ok_home[['침실수','자녀수', '방수']].quantile(0.25)
        Q3 = ok_home[['침실수','자녀수', '방수']].quantile(0.75)
        IQR = Q3 - Q1
        print(IQR)
        '''IQR 상한, 하한'''
        Lower = Q1 - 3.0 * IQR
        Upper = Q3 + 3.0 * IQR
        print(Lower)
        print(Upper)
        print(ok_home[['침실수', '자녀수', '방수']].min())
        print(ok_home[['침실수', '자녀수', '방수']].max())

        dft2 = ok_home[['나이','월전기료','월가스비','가계소득','주택가격']]
        g= sns.PairGrid(dft2)
        print(g.map_diag(sns.histplot))
        print(g.map_offdiag(sns.scatterplot))
        Q1 = ok_home[['나이', '월전기료','월가스비','가계소득','주택가격']].quantile(0.25)
        Q3 = ok_home[['나이', '월전기료','월가스비','가계소득','주택가격']].quantile(0.75)
        IQR = Q3 - Q1
        print(IQR)
        '''IQR 상한, 하한'''
        Lower = Q1 - 3.0 * IQR
        Upper = Q3 + 3.0 * IQR
        print(Lower)
        print(Upper)
        print(ok_home[['나이', '월전기료','월가스비','가계소득']].min())
        print(ok_home[['나이', '월전기료','월가스비','가계소득','주택가격']].max())

        '''p.218'''
        c1 = ok_home['월전기료']<= 500
        c2 = ok_home['월가스비']<=311
        c3 = ok_home['가계소득']<=320000
        df1 = ok_home[c1&c2&c3]
        print(df1.shape)

        fig, axes = plt.subplots(1,2,figsize=(15,5))
        sns.histplot(ax=axes[0], data=ok_home, x="월전기료", kde=True, bins=23)
        axes[0].set_title('월전기료 before')
        sns.histplot(ax=axes[1], data=df1, x="월전기료", kde=True, bins=23)
        axes[1].set_title('월전기료 after')

        fig, axes = plt.subplots(1, 2, figsize=(15, 5))
        sns.histplot(ax=axes[0], data=ok_home, x="월가스비", kde=True, bins=23)
        axes[0].set_title('월가스비 before')
        sns.histplot(ax=axes[1], data=df1, x="월가스비", kde=True, bins=23)
        axes[1].set_title('월가스비 after')

        cols2 = []
        self.oklahoma = ok_home

    def ratio(self):
        ok_home = self.oklahoma
        print(pd.crosstab(ok_home['MAR'], columns='ratio', normalize=True))
        print(pd.crosstab(ok_home['MAR'], ok_home['지하주택가격'], normalize=True))

        self.oklahoma = ok_home

    def nominal(self):
        ok_home = self.oklahoma
        ok_home['MAR'].value_counts(dropna=False)
        print(pd.crosstab(ok_home['MAR'], columns='count'))
        print(pd.crosstab(ok_home['MAR'], ok_home['지하주택가격']))

        self.oklahoma = ok_home

    def ordinal(self):
        pass

    def target(self):
        print(self.oklahoma['지하주택가격'].dtype)
        print(self.oklahoma['지하주택가격'].isnull().sum())
        print(self.oklahoma['지하주택가격'].value_counts(dropna=False, normalize=True))






