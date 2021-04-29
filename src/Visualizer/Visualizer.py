import pygame
from src.Visualizer.Block import Block
from src.Map.MapGenerator import MapGenerator
from src.Visualizer.Parallax import Parallax


class Visualizer:

    def __init__(self, scale=1, screen=None):

        self.screen = screen if screen is not None else pygame.display.get_surface()
        self.screen_width, self.screen_height = self.screen.get_size()
        self.scale = scale
        self.block_width = int(100 * scale)
        self.distance_factor = 4
        self.distance = int(self.scale * 100 * self.distance_factor)
        self.map_generator = MapGenerator()

        # Blocks
        self.block_objects = []
        self.block_1_img = pygame.transform.scale(pygame.image.load("resources/Tiles/1.png"), (self.block_width, self.block_width))
        self.block_2_img = pygame.transform.scale(pygame.image.load("resources/Tiles/2.png"), (self.block_width, self.block_width))
        self.block_3_img = pygame.transform.scale(pygame.image.load("resources/Tiles/3.png"), (self.block_width, self.block_width))

        # Background
        self.screen_width = self.screen_width
        self.bg_img = pygame.image.load("resources/Backgrounds/2.png")
        self.bg_rect = self.bg_img.get_rect()
        self.bg_rect.x = 0
        self.bg_rect.y = 0
        # Parallax
        self.parallax_screens = [Parallax("resources/Backgrounds/3.png", 1), Parallax("resources/Backgrounds/4.png", 2), Parallax("resources/Backgrounds/5.png", 3)]

        x = 0
        for _ in range(0, 2):
            self.append_row(self.map_generator.generate_row_empty(), x)
            x += self.distance
        # Generate first piece of the map (5 rows)
        for _ in range(0, 5):
            x += self.distance
            row = self.map_generator.generate_row()
            self.append_row(row, x)

    def update_distance(self, u):
        self.distance_factor = u
        self.distance = int(self.scale * 100 * self.distance_factor)

    def append_row(self, row, x):
        for i, elem in enumerate(row):
            if elem == 1:
                self.block_objects.append(Block(x, i * self.block_width, elem, self.block_1_img))
            elif elem == 2:
                self.block_objects.append(Block(x, i * self.block_width, elem, self.block_2_img))
            elif elem == 3:
                self.block_objects.append(Block(x, i * self.block_width, elem, self.block_3_img))

    def render(self):
        self.render_background()
        for elem in self.block_objects:
            elem.render()

    def move_blocks(self, move_by):

        for x in self.block_objects:
            x.move(move_by)
        if self.block_objects[-1].img_rect.x < self.screen_width:
            self.append_row(self.map_generator.generate_row(), self.block_objects[-1].img_rect.x + int(self.scale * 100 * self.distance_factor))

        # delete blocks which are left of screen
        self.block_objects = [b for b in self.block_objects if b.img_rect.x > -100]

    def render_background(self):
        # move background for parallax effect

        self.screen.blit(self.bg_img, self.bg_rect)
        for p in self.parallax_screens:
            p.render()
            p.move()
