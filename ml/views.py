import pandas as pd
df = pd.read_csv('./data/healthcare-dataset-stroke-data.csv')
c = df['age'] > 18
df1 = df[c]
df1 = df1.rename(columns={'Residence_type' : 'residence_type'})
cols = ['age', 'avg_glucose_level', 'bmi']
class StrokeController:
    pass
    @staticmethod
    def menu_2():
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(df.head(3))

    @staticmethod
    def menu_3():
        print(df['id'].dtypes)
        print(df['id'].isnull().sum())
        print(len(pd.unique(df['id'])))
        print(df['stroke'].dtype)
        print(df['stroke'].isnull().sum())
        print(df['stroke'].value_counts(dropna=False, normalize=True))
    @staticmethod
    def menu_4():
        print(df[cols].dtypes)
        pd.options.display.float_format = '{:.2f}'.format
        print(df[cols].describe())
        print(df[c].head(3))
        len(df[c])
        print(len(df[c])/ len(df))
        print(df1.shape)
        cols1 = ['gender', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'residence_type', 'smoking_status']
        print(df1[cols1].isnull().sum())
        print(df1.isna().any()[lambda x: x])
        print(df['bmi'].isnull().mean())
        print(df1[cols].describe())
        print(df1[cols].skew())
        print(df1[cols].kurtosis())
        print(df1['work_type'].value_counts(dropna=False))
        print(pd.crosstab(df1['work_type'], columns= 'count'))
        print(pd.crosstab(df1['work_type'], columns= 'ratio', nomalize=True))
        print(pd.crosstab(df1['work_type'], df1['stroke']))
        print(pd.crosstab(df1['work_type'], df1['stroke'], nomalize = True))

