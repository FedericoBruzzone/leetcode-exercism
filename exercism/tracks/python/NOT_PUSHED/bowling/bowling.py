import functools

class BowlingGame:
    def __init__(self):
        self.frames = []
        self.firstRoll = None

    def roll(self, pins):
        if self.firstRoll is None:
            if pins == 10: self.frames.append((10,0)); return
            self.firstRoll = pins
        else:
            self.frames.append((self.firstRoll, pins)); self.firstRoll = None

    def score(self):
        # return functools.reduce(lambda x,y: x+y, \
        #     [(self.frames[i][0] == 10 and sum(self.frames[i] + self.frames[i+1])) or \
        #     (sum(self.frames[i]) == 10 and sum(self.frames[i] + tuple([self.frames[i+1][0]]))) or \
        #     sum(self.frames[i])
        #     for i in range(len(self.frames)-1)])

        return functools.reduce(lambda x,y: x+y, \
            [(self.frames[i][0] == 10 and \
                sum([self.frames[j+i][0] for j in range(3) if self.frames[j+i][0] == 10] \
                    if self.frames[i+1][0] == 10 else self.frames[i] + self.frames[i+1])) or \
            (sum(self.frames[i]) == 10 and sum(self.frames[i] + tuple([self.frames[i+1][0]]))) or \
            sum(self.frames[i])
            for i in range(len(self.frames))])

# game = BowlingGame()

# # game.roll(4)
# # game.roll(5)
# # game.roll(1)
# # game.roll(6)
# # game.roll(10)
# # game.roll(9)
# # game.roll(1)

# #[game.roll(i) for i in [10, 5, 5, 9, 0]]
# #[game.roll(i) for i in [10, 10, 10, 10, 10,  0, 0, 0, 0, 0, 0, 0, 0, 0]]
# print(game.frames)
# print(game.score())