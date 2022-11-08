from scrapper.domains import MusicRank
from scrapper.view import ScrapController
from util.common import Common

if __name__ == '__main__':   #본인 사이트 할 때 사용해라
    m = MusicRank()
    scr = ScrapController()
    while True:
        menus = ["종료", "벅스", "멜론"]
        menu = Common.menu(menus)
        if menu == "0":
            print(menus[0])
            break
        elif menu == "1":
            print(menus[1])
            m.domain = "https://music.bugs.co.kr/chart/track/day/total?chartdate="
            m.query_str = "20221101"
            m.parser = "xlml"
            m.class_names= ["title", "artist"]
            m.tag_name = "p"
            scr.menu_1(m)
        elif menu == "2":
            print(menus[2])
            m.domain = "https://www.melon.com/chart/index.htm"
            m.parser = "xlml"
            m.class_names = ["title", "artist"]
            m.tag_name = "p"
            scr.menu_2(m)
        else: print("잘못된 입력")
