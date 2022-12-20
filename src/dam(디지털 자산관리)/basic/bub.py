import random


class Bub(object):
    def __init__(self):
        pass

    def get_random(self, start, end, count):
        return random.sample(range(start, end), k = count)

    def print(self):
        rl = self.get_random(10, 100, 10)
        print(rl)
        for i in range(len(rl)-1):
            for j in range(len(rl)-1):
                if rl[j] > rl[j+1]:
                    rl[j], rl[j+1] = rl[j+1], rl[j]
        print(rl)

    @staticmethod
    def main():
        bub = Bub()
        bub.print()
Bub.main()