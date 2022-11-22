import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

def BugsMusic(arg):
        soup = BeautifulSoup(urlopen(arg.domain + arg.query_str), 'lxml')
        title = {"class" : arg.class_names[0]}
        artist = {"class" : arg.class_names[1]}
        titles = soup.find_all(name = arg.tag_name, attrs = title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name = arg.tag_name, attrs = artist)
        artists = [i.find('a').text for i in artists]
        #디버깅
        [print(f"{i}위 {j} : {k}")
         for i, j, k in zip(range(1, len(titles)), titles, artists)]
        #dict로 변환
        diction =  {}
        for i, j in enumerate(titles):
                diction[j] = artists[i]
        # csv 파일로 저장
        arg.diction = diction
        arg.dict_to_dataframe()
        arg.dataframe_to_csv() #csv 파일로 저장

def MelonMusic(arg):
        req = urllib.request.Request(arg, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(urlopen(req), 'lxml')
        title = {"class": "rank01"}
        artist = {"class": "rank02"}
        titles = soup.find_all(name="div", attrs=title)
        titles = [i.find('a').text for i in titles]
        artists = soup.find_all(name="div", attrs=artist)
        artists = [i.find('a').text for i in artists]
        [print(f"{i}위 {j} : {k}")
         for i, j, k in zip(range(1, len(titles)), titles, artists)]
        diction = {}
        for i, j in enumerate(titles):
                diction[j] = artists[i]
        arg.diction = diction
        arg.dict_to_dataframe()
        arg.dataframe_to_csv()