
STROKE_MENUS = ["종료", #0
                "데이터구하기",#1
                "한글화"#2
                "타깃변수설정",#3
                "데이터처리",#4
                "시각화",#5
                "모델링",#6
                "학습",#7
                "예측"]#8
stroke_meta = {
    'id':'아이디',
    'gender':'성별',
    'age':'나이',
    'hypertension':'고혈압',
    'heart_disease':'심장병',
    'ever_married':'기혼여부',
    'work_type':'직종',
    'Residence_type':'거주형태',
    'avg_glucose_level':'평균 혈당',
    'bmi':'체질량지수',
    'smoking_status':'흡연 여부',
    'stroke':'뇌졸중'}
stroke_menu = {
    "1" : lambda t: t.menu_1(),
    "2" : lambda t: t.menu_2(),
    "3" : lambda t: t.menu_3(),
    "4" : lambda t: t.menu_4(),

    "5" : lambda t: t.menu_5(),
    "6" : lambda t: t.find_highest_hwy(),
    "7" : lambda t: t.which_cty_in_suv_compact(),
    "8" : lambda t: t.find_top5_hwy_in_audi(),
    "9" : lambda t: t.find_top3_avg(),
}
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5110 entries, 0 to 5109
Data columns (total 12 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 5110 non-null   int64  
 1   gender             5110 non-null   object 
 2   age                5110 non-null   float64
 3   hypertension       5110 non-null   int64  
 4   heart_disease      5110 non-null   int64  
 5   ever_married       5110 non-null   object 
 6   work_type          5110 non-null   object 
 7   Residence_type     5110 non-null   object 
 8   avg_glucose_level  5110 non-null   float64
 9   bmi                4909 non-null   float64
 10  smoking_status     5110 non-null   object 
 11  stroke             5110 non-null   int64  
dtypes: float64(3), int64(4), object(5)
memory usage: 479.2+ KB
None
'''

