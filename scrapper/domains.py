
import urllib
from dataclasses import dataclass
from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup

from const.path import CTX

"""
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
"""


class MelonMusic(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        req = urllib.request.Request(self.url, headers=self.headers)
        soup = BeautifulSoup(urlopen(req), 'lxml')
        _ = 0
        title = {"class" : "rank01"}
        artist = {"class" : "rank02"}
        titles = soup.find_all(name = "div", attrs = title)
        artists = soup.find_all(name = "div", attrs = artist)
        [print(f"{i}위 {j.find('a').text} {k.find('a').text}")
         for i, j, k in zip(range(1, len(titles)), titles, artists)]

class Melon:
    pass

@dataclass
class MusicRank:

    parser : str
    domain : str
    query_str : str
    headers :dict
    tag_name : str
    fname : str
    class_names : list
    artists : list
    titles : list
    dic : dict
    df : None
    soup : BeautifulSoup


    @property
    def html(self) -> str: return self._html
    @html.setter
    def html(self, html): self._html = html

    @property
    def parser(self) -> str: return self.parser

    @parser.setter
    def parser(self, parser): self._parser = parser

    @property
    def domain(self) -> str: return self.domain

    @domain.setter
    def domain(self, domain): self._domain = domain

    @property
    def query_str(self) -> str: return self.query_str

    @query_str.setter
    def query_str(self, query_str): self._query_str = query_str

    @property
    def headers(self) -> str: return self.headers

    @headers.setter
    def headers(self, headers): self._headers = headers

    @property
    def tag_name(self) -> str: return self.tag_name

    @tag_name.setter
    def tag_name(self, tag_name): self._tag_name = tag_name

    @property
    def fname(self) -> str: return self.fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def class_names(self) -> str: return self.class_names

    @class_names.setter
    def class_names(self, class_names): self._class_names = class_names

    @property
    def artists(self) -> str: return self.artists

    @artists.setter
    def artists(self, artists): self._artists = artists

    @property
    def titles(self) -> str: return self.titles

    @titles.setter
    def titles(self, titles): self._titles = titles

    @property
    def dic(self) -> str: return self.dic

    @dic.setter
    def dic(self, dic): self._dic = dic

    @property
    def df(self) -> str: return self.df

    @df.setter
    def df(self, df): self._df = df

    @property
    def soup(self) -> str: return self.soup

    @soup.setter
    def soup(self,soup): self._soup = soup

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict((self.dic, orient='index'))

    def dataframe_to_csv(self):
        path = CTX +self.fname+ '.csv'
        self.df.to_csv(path, sep=',', na_rep="NaN")