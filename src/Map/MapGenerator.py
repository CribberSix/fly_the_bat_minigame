import random


class MapGenerator:

    def __init__(self):
        self.block_no = 0
        self.block_mid = 1
        self.block_bottom_top = 2
        self.block_top_bottom = 3

        self.height = 10
        self.min_space = 4

    def generate_row_empty(self):
        return [self.block_no for _ in range(self.height)]

    def generate_row(self):

        limit_downwards = int(self.height * (self.height - self.min_space) / 10)
        limit_above = random.randint(-1, limit_downwards)
        limit_upwards = limit_above + self.min_space
        limit_below = random.randint(limit_upwards, self.height)

        row = []
        if limit_above > 0:
            for i in range(0, limit_above):
                if i < limit_above - 1:
                    row.append(self.block_mid)  # mid
                else:
                    row.append(self.block_top_bottom)  # end of top block

        for _ in range(limit_above, limit_below):
            row.append(self.block_no)

        if limit_below < self.height:
            for i in range(limit_below, self.height):
                if i == limit_below:
                    row.append(self.block_bottom_top)
                else:
                    row.append(self.block_mid)

        return row
