# menu 입력
    def list(MENUS):
    for i, j in enumerate(MENUS):
        print(f'{i}. {j}')
    return input('실행 : ')

# 도메인
### 지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용</hr>
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.

    @dataclass
    class MusicRank:
        html = ''
        parser = ''
        domain = ''
        query_str = ''
        headers = {}
        tag_name = ''
        fname = ''
        class_names = []
        artists = []
        titles = []
        dic = {}
        df = None

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.diction, orient='index')

    def dataframe_to_csv(self):
        path = './save/ranking.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN", header =None)


