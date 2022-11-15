# 흐름도
프로젝트 흐름도|
---|
데이터구하기|
타깃 변수 설정|
데이터 처리|
시각화|
ML모델 수립|
모델 실행|
모델 선정 및 활용|
#### ↘시각화
> 결측값 제거 

> ->구간변수
>> 요약 통계 검토
> 
>> 이상값 제거
> 
>> 상관관계 검토
> 
>> 시각화
> 
>> t검정

> -> 범주형변수
>> 도수분포표 검토
> 
>> 시각화
# 1. 타깃변수 설정
# 2. csv파일 불러오기
    import pandas as pd  -> 판다스 라이브러리
    import numpy as np   -> 넘파이 라이브러리

    pd.set_option('display.max_columns', None) -> 열 개수 최대화
    pd.set_option('display.max_rows', None) -> 행 개수 최대화
    df = pd.read_csv('파일명.csv') ->  # 데이터 파일을 불러와서 데이터 프레임(df)에 저장
    df.head(3) -> 데이터 프레임을 3행까지 보여주기

 - 열, 행 개수
    df.shape
 - df의 주요 정보 확인
    df.info()
 - 데이터타입 확인
    df['속성명'].dtypes
 - 변수 이름 변경
    my_stroke = stroke.rename(columns=stroke_meta)
        return my_stroke
    
# 3. ID 변수 설정 -
> -> 결측값과 중복값이 필수

### 1) 타입확인
### 2) 결측값(Null) 확인
    df['속성명'].isnull().sum()
### 3) 중복값(unique)
    n = (len(pd.unique(self.my_stroke['아이디'])))
   - ID 변수인 id값의 중복여부를 체크하기 위해 유일한 값의 개수 체크
   - pd.unique는 유일한 변숫값을 출력하고 len은 값의 개수를 카운트

# 4. 타깃 변수 생성    
### 1) 타입확인
    print(self.my_stroke['뇌졸중'].dtype)
### 2) 분포확인
    print(self.my_stroke['뇌졸중'].isnull().sum())
    print(self.my_stroke['뇌졸중'].value_counts(dropna=False, normalize=True))

# 5. 기타 변수데이터 처리
### 1) 구간변수 타입확인
    cols = ['나이', '평균 혈당', '체질량지수'] ->구간 변수를 cols에 저장
    print(df[cols].dtypes)

### 2) 구간 변수 기초 통계량
    pd.options.display.float_format = '{:.2f}'.format ->소숫점 2자리로 숫자표기 제한
    print(df[cols].describe())
### 3) 데이터세트에서 18세 이하 제거
    - 조건 확인
        c = df['나이'] > 18
    - 자료의 개수  -> 행 기준
        len(df[c])
    - 자료 개수 비율
        len(df[c])/ len(df)
### 4) 사용하지 않을 데이터 제거한 데이터 프레임
    df1 = df[c]
    - 변수명 변경
        df1 = df1.rename(columns={'Residence_type': 'residence_type'})
### 5) 결측값 확인
    cols1 = ['성별', '고혈압', '심장병', '기혼여부', '직종', '거주형태', '흡연 여부']
    print(df1[cols1].isnull().sum())
# 6. 탐색적 자료 분석 및 시각화
### 1) 결측값 높은 변수 제거
    - 결측값 있는 변수명 찾기
        df1.isna().any()[lambda x: x]
    - 체질량지수의 결측값 비율 확인
        df['체질량지수'].isnull().mean()
### 2) 구간 변수
##### (1) 요약 통계 검토
    - 구간변수의 통계 구하기
        df1[cols].describe()
    - 왜도, 첨도 확인
        df1[cols].skew()
        df1[cols].kurtosis()
    - 변수의 범주별 빈도수
        df1['변수'].value_counts(dropna=False)
    - 도수분포표
        * pd.crosstab(df1['직종'], columns= 'count') ->개수 기준
        * pd.crosstab(df1['직종'], columns= 'ratio', normalize=True) ->비율 기준
    - 분할표(=빈도분포)
        * pd.crosstab(df1['직종'], df1['뇌졸중'])
        * pd.crosstab(df1['직종'], df1['뇌졸중'], normalize = True)
##### (2) 이상값 제거 
> -> 통계에 영향을 주니까 제거해야 한다

    fig, axes = plt.subplots(1, 3, figsize=(15,4))
    sns.histplot(ax=axes[0], data=df, x="나이", kde=True, bins=20)
    sns.histplot(ax=axes[1], data=df, x="평균 혈당", kde=True, bins=20)
    sns.histplot(ax=axes[2], data=df, x="체질량지수", kde=True, bins=20)
    plt.show()

    - 구간 변수상자
        sns.boxplot(ax=axes[0], x="나이", data=df1)
        sns.boxplot(ax=axes[1], x="평균 혈당", data=df1)
        sns.boxplot(ax=axes[2], x="체질량지수", data=df1)
    - 구간변수의 IQR계산 
        Q1 = df1[['나이', '평균 혈당', '체질량지수']].quantile(0.25)
        Q3 = df1[['나이', '평균 혈당', '체질량지수']].quantile(0.75)
        IQR = Q3 - Q1
        print(IQR)
    - IQR 상한, 하한
        Lower = Q1-3.0*IQR
        Upper = Q3+3.0*IQR
        print(Lower)
        print(Upper)
        c1 = df1['평균 혈당'] <= 232.64
        c2 = df1['체질량지수'] <= 60.3
        df2 = df1[c1 & c2]
        print(df2.shape)
##### (3) 상관관계 검토
    - 변수 간 상관계수
        round(df2[cols].corr(),2) -> 구간변수 간 상관계수 출력
    - 상관계수의 크기 확인
        corr = df2[cols].corr()
        annot_kws ={"ha" : 'center', "va": 'top'}
        sns.heatmap(data=corr, annot= True, annot_kws=annot_kws, cmap="YlGnBu")
        df2.to_csv('healthcare-dataset-stroke-data.csv', index=False)
