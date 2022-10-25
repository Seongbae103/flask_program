import random

class OddEven(object):
    def __init__(self):
        pass

    def get_random(self, start, end, count):
        return random.sample(range(start, end), k = count)
    def checker(self):
        rl = self.get_random(10, 100, 10)
        print(rl)
        for i in rl:
            if i % 2 == 0:
                print(i)

    @staticmethod
    def main():
        ls = []
        odd_even = OddEven()
        ls.append(odd_even.checker())


OddEven.main()
