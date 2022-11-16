import googlemaps
import pandas as pd
'''
주어진 데이터를 활용해서 서울시내 경찰서 범죄발생과 검거율 현황지도(폴리움)를 작성하시오
'''
CRIME_MENUS = ["종료", #0
                "spec",#1
                "Merge", #2
                "interval",#3
                "ratio",
                "norminal",
                "ordinal",#4
                "target",
                "샘플링",#5
                "모델링",#6
                "학습",#7
                "예측"]#8
crime_meta = {
    'id':'아이디', 'gender':'성별', 'age':'나이',
    'hypertension':'고혈압',
    'heart_disease':'심장병',
    'ever_married':'기혼여부',
    'work_type':'직종',
    'Residence_type':'거주형태',
    'avg_glucose_level':'평균혈당',
    'bmi':'체질량지수',
    'smoking_status':'흡연여부',
    'stroke':'뇌졸중'
}
crime_menu = {
    "1" : lambda t: t.spec(),
    "2" : lambda t: t.save_police_pos(),
    "3" : lambda t: t.interval(),
    "4" : lambda t: t.ratio(),
    "5" : lambda t: t.norminal(),
    "6" : lambda t: t.ordinal(),
    "7" : lambda t: t.target(),
    "8" : lambda t: t.partition(),
    "9" : lambda t: t.popu(),

}
class Crime:
    def __init__(self):
        self.cctv = pd.read_csv('./data/cctv_in_seoul.csv')
        self.seoul_crime = pd.read_csv('./data/crime_in_seoul.csv')
        self.population = pd.read_excel('./data/pop_in_seoul.xls', usecols=[1,3,6,9,13], skiprows=[0,2])

    def spec(self):
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        [(lambda x: print(f" --- 1.Shape ---\n{x.shape}"
                               f"--- 2.Features ---\n{x.columns}"
                               f"--- 3.Info ---\n{x.info()}"
                               f"--- 4.Case Top1 ---\n{x.head(1)}"
                               f"--- 5.Case Bottom1 ---\n{x.tail(3)}"
                               f"--- 6.Describe ---{x.describe()}"
                               f"--- 7.Describe All ---\n{x.describe(include='all')}"))(i) for i in [self.seoul_crime, self.cctv]]
        print(self.population)
    def save_police_pos(self):
        crime = self.seoul_crime
        station_names = []
        for name in crime['관서명']:
            print(f'지역 이름: {name}')
            station_names.append(f'서울{str(name[:-1])}경찰서')
        print(station_names)
        print(f'서울 시내 경찰서는 총 {len(station_names)}개다')
        gmaps = (lambda x: googlemaps.Client(key=x))('') #커밋할 때는 키 지워야된다
        print(gmaps.geocode("서울중부경찰서", language='ko'))
        print('API에서 주소추출 시작')
        station_addrs = []
        station_lats = []
        station_lngs = []
        for i, name in enumerate(station_names):
            _ = gmaps.geocode(name, language='ko')
            print(f'name {i} = {_[0].get("formatted_address")}')
            station_addrs.append(_[0].get('formatted_address'))
            _loc = _[0].get('geometry')
            station_lats.append(_loc['location']['lat'])
            station_lngs.append(_loc['location']['lng'])
        gu_names = []
        for name in station_addrs:
            _ = name.split()
            gu_name = [gu for gu in _ if gu[-1]=='구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names
        crime.to_csv('./save/police_pos.csv', index=False)


    def interval(self):
        t = self.cctv
        inter = ['소계','2013년도 이전','2014년','2015년','2016년']
        print(f'--- 구간변수 기초 통계량 --- \n{t[inter].describe()}')

    def ratio(self):
        pass
    def norminal(self):
        pass
    def ordinal(self):
        pass
    def target(self):
        pass
    def partition(self):
        pass

def my_menu(ls):
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

if __name__ == '__main__':
    t = Crime()
    while True:
        menu = my_menu(CRIME_MENUS)
        if menu == '0':
            print("종료")
            break
        else:
            try:
                crime_menu[menu](t)
            except KeyError:
                print(" ### Error ### ")