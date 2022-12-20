from flaskProject.src.ext.scrapper.service import BugsMusic, MelonMusic


class ScrapController(object):

    @staticmethod
    def menu_1(arg):
        BugsMusic(arg)

    @staticmethod
    def menu_2(arg):
        MelonMusic(arg)
