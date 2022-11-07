from scrapper.service import BugsMusic


class ScrapController(object):

    @staticmethod
    def menu_1(arg):
        BugsMusic(arg)


    @staticmethod
    def menu_2(arg):
        melon = MelonMusic(arg)
        melon.scrap()