import pygame
from src.Visualizer.Block import Block


class Visualizer:

    def __init__(self, scale=1, screen=None, screen_width=750):

        self.screen = screen if screen is not None else pygame.display.get_surface()
        self.scale = scale
        self.width = int(100 * scale)
        self.block_1_img = pygame.transform.scale(pygame.image.load("resources/Tiles/1.png"), (self.width, self.width))
        self.block_2_img = pygame.transform.scale(pygame.image.load("resources/Tiles/2.png"), (self.width, self.width))
        self.block_3_img = pygame.transform.scale(pygame.image.load("resources/Tiles/3.png"), (self.width, self.width))

        self.block_objects = []

        # Background
        self.screen_width = screen_width
        self.bg_img = pygame.transform.scale(pygame.image.load("resources/Tiles/background.jpg"), (screen_width, screen_width))
        self.bg_rect = self.bg_img.get_rect()
        self.bg_rect.x = 0
        self.bg_rect.y = 0
        self.bg_rect2 = self.bg_img.get_rect()
        self.bg_rect2.x = screen_width
        self.bg_rect2.y = 0

    def append_row(self, row, x):
        for i, elem in enumerate(row):
            if elem == 1:
                self.block_objects.append(Block(x, i*self.width, self.block_1_img))
            elif elem == 2:
                self.block_objects.append(Block(x, i*self.width, self.block_2_img))
            elif elem == 3:
                self.block_objects.append(Block(x, i*self.width, self.block_3_img))

    def render(self):
        self.render_background()
        for elem in self.block_objects:
            elem.render()

    def move_blocks(self, move_by):
        for x in self.block_objects:
            x.move(move_by)

    def render_background(self):
        # move background for parallax effect
        self.bg_rect.x -= 1
        self.bg_rect2.x -= 1

        # reset when image is not visible anymore
        if self.bg_rect.x <= -self.screen_width:
            self.bg_rect.x = self.screen_width
        if self.bg_rect2.x <= -self.screen_width:
            self.bg_rect2.x = self.screen_width

        # render
        self.screen.blit(self.bg_img, self.bg_rect)
        self.screen.blit(self.bg_img, self.bg_rect2)
