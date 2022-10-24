import random


class RandomList(object):
    def __init__(self):
        pass

    def get_random(self, start, end, count):
        return random.sample(range(start, end), k = count)

    def print_random(self):
        print(self.get_random(1, 100), 10)

    @staticmethod
    def main():
        rl = RandomList()
        rl.print_random()

RandomList.main()
