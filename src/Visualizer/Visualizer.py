import pygame
from src.Visualizer.Block import Block


class Visualizer:

    def __init__(self, scale=1):
        self.scale = scale
        self.width = int(100 * scale)
        self.block_1_img = pygame.transform.scale(pygame.image.load("resources/Tiles/block_1.png"), (self.width, self.width))
        self.block_2_img = pygame.transform.scale(pygame.image.load("resources/Tiles/block_2.png"), (self.width, self.width))

        self.block_objects = []

    def append_row(self, row, x):

        for i, elem in enumerate(row):
            if elem == 1:
                self.block_objects.append(Block(x, i*self.width, self.block_1_img))
            elif elem == 2:
                self.block_objects.append(Block(x, i*self.width, self.block_2_img))

    def render(self):
        for elem in self.block_objects:
            elem.render()

    def move_blocks(self, move_by):
        for x in self.block_objects:
            x.move(move_by)