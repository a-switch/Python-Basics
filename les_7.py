import random

class Game:
    def __init__(self):
        self.cask = 90
        self.gCask = self.getCask()

    def getCask(self):
        count = [x for x in range(1,91)]
        random.shuffle(count)
        steps = {x:y for x,y in enumerate(count,1)}
        print(steps)
        index = 1
        print('Новый бочонок: {}, осталось {}'.format(steps[index], self.cask - index))
        index = index + 1
