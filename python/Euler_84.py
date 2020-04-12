# https://projecteuler.net/problem=84
# 12 Apr 2020

from random import randint, shuffle

class MonopolyGame:
    def __init__(self, die_max):
        self.die_max = die_max

        self.pos = 0
        self.chest = ['GO', 'JAIL'] + ['?'] * 14
        self.chance = [
            'GO',
            'JAIL',
            'C1', 'E3', 'H2', 'R1', 'NEXT_R', 'NEXT_R', 'NEXT_U', 'BACK_3',
        ] + ['?'] * 6

        shuffle(self.chest)
        shuffle(self.chance)

        self.consecutive_doubles = 0
        self.history = [0] * 40
        self.moves = 0

    def open_community_chest(self):
        # TODO: Do we ever have to re-shuffle?
        pull = self.chest[0]
        self.chest = self.chest[1:] + [self.chest[0]]

        if pull == 'GO':
            self.pos = 0
        elif pull == 'JAIL':
            self.pos = 10

    def open_chance(self):
        # TODO: Do we ever have to re-shuffle?
        pull = self.chance[0]
        self.chance = self.chance[1:] + [self.chance[0]]

        if pull == 'GO':
            self.pos = 0
        elif pull == 'JAIL':
            self.pos = 10
        elif pull == 'C1':
            self.pos = 11
        elif pull == 'E3':
            self.pos = 24
        elif pull == 'H2':
            self.pos = 39
        elif pull == 'R1':
            self.pos = 5
        elif pull == 'NEXT_R':
            if self.pos < 5: self.pos = 5
            elif self.pos < 15: self.pos = 15
            elif self.pos < 25: self.pos = 25
            elif self.pos < 35: self.pos = 35
            else: self.pos = 5
        elif pull == 'NEXT_U':
            if self.pos < 12: self.pos = 12
            elif self.pos < 28: self.pos = 28
            else: self.pos = 12
        elif pull == 'BACK_3':
            self.pos -= 3

    def record_end_position(self):
        self.history[self.pos] += 1

    def roll(self):
        self.moves += 1
        d1 = randint(1, self.die_max)
        d2 = randint(1, self.die_max)

        if d1 == d2:
            self.consecutive_doubles += 1
        else:
            self.consecutive_doubles = 0

        if self.consecutive_doubles == 3:
            self.consecutive_doubles = 0
            self.pos = 10
            return

        self.pos = (self.pos + d1 + d2) % 40

        if self.pos == 30:
            # Go to jail
            self.pos = 10
        elif self.pos in [2, 17, 33]:
            self.open_community_chest()
        elif self.pos in [7, 22, 37]:
            self.open_chance()

        self.record_end_position()

if __name__ == '__main__':
    game = MonopolyGame(4)
    for i in range(1000000):
        game.roll()

    top_three = sorted(range(len(game.history)), key=lambda k: -game.history[k])[:3]
    modal_string = ''.join(map(lambda s: str(s).rjust(2, '0'), top_three))
    print modal_string
