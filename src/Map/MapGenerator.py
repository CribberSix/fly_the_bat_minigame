import random


class MapGenerator:

    def __init__(self):

        self.block_no = 0
        self.block_1 = 1
        self.block_2 = 2

        self.height = 10
        self.min_space = 3

    def generate_row_empty(self):
        return [self.block_no for _ in range(self.height)]

    def generate_row(self):

        limit_downwards = int(self.height * 0.7)
        limit_above = random.randint(-1, limit_downwards)
        limit_upwards = limit_above + self.min_space
        limit_below = random.randint(limit_upwards, self.height)

        #print("____")
        #print(f"upper:  0-{limit_above}")
        #print(f"lower: {limit_below}-10")

        row = []
        if limit_above > 0:
            for _ in range(0, limit_above):
                row.append(self.block_1)

        for _ in range(limit_above, limit_below):
            row.append(self.block_no)

        if limit_below < self.height:
            for _ in range(limit_below, self.height):
                row.append(self.block_2)

        return row
