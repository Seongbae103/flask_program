from randomlist import RandomList

class Bubble(object):
    def __init__(self):
        pass
    @staticmethod
    def print():
        rl = RandomList().get_random(10, 100, 10)
        print(rl)
        for i in range(len(rl)-1):
            for j in range(len(rl)-1):
                if rl[j] > rl[j+1]:
                    rl[j], rl[j + 1] = rl[j+1], rl[j]
        print(rl)
    @staticmethod
    def main():
        bubble = Bubble()
        Bubble.print()
Bubble.main()
