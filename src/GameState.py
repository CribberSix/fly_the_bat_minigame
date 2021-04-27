import pygame
import sys
from src.Map.MapGenerator import MapGenerator
from src.Visualizer.Visualizer import Visualizer
from src.Character.Character import Character
from src.Fin.Endscreen import Endscreen
from src.Visualizer.Block import Block


class GameState:

    def __init__(self, screen=None):
        scaling = 0.75

        # PYGAME
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.screen = screen if screen is not None else pygame.display.get_surface()
        w, h = self.screen.get_size()

        # GAME  SETUP
        self.map = []
        self.viz = Visualizer(scale=scaling)
        self.map_generator = MapGenerator()
        c_x = int(w/4)
        c_y = int(h/2)
        self.character = Character(c_x, c_y, scale=scaling)
        self.game_speed = 3

        # Point system
        self.points = 0
        self.font = pygame.font.Font("resources/Fonts/Quicksand-Bold.ttf", 20)
        self.point_y = h - 25
        self.point_x = 5

        # Borders top & bottom
        img_top = pygame.image.load("resources/Tiles/top.png")
        img_top = pygame.transform.scale(img_top, (w, 10))
        self.border_top = Block(0, 0, img_top)

        img_bottom = pygame.image.load("resources/Tiles/bottom.png")
        img_bottom = pygame.transform.scale(img_bottom, (w, 10))
        self.border_bottom = Block(0, h-10, img_bottom)

        # Generate 5 empty rows for the start
        x = 0
        for _ in range(0, 5):
            self.viz.append_row(self.map_generator.generate_row_empty(), x)
            x += int(scaling * 100)

        # Generate first piece of the map (20 rows)
        for _ in range(0, 20):
            x += int(scaling * 100 * 4)
            row = self.map_generator.generate_row()
            self.viz.append_row(row, x)

    def render_points(self):
        textsurface = self.font.render(str(int(self.points)), False, (0, 0, 0))
        self.screen.blit(textsurface, (self.point_x, self.point_y))

    def collision_detection(self):

        if self.character.img_rect.colliderect(self.border_bottom.img_rect) or self.character.img_rect.colliderect(self.border_top.img_rect):
            Endscreen(int(self.points)).render()
            return True

        for b in self.viz.block_objects:
            if self.character.img_rect.colliderect(b.img_rect):
                Endscreen(int(self.points)).render()
                return True
        return False

    def run(self):
        while True:
            self.points += 0.1 * self.game_speed
            pygame_events = pygame.event.get()

            for event in pygame_events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.get_surface().fill((200, 200, 200))  # draw background

            # Movement
            self.character.move(pygame_events)
            self.viz.move_blocks(self.game_speed)
            # Visuals
            self.border_bottom.render()
            self.border_top.render()
            self.viz.render()
            self.character.render()
            self.render_points()

            if self.collision_detection():
                return

            pygame.display.flip()  # update screen
            self.clock.tick(self.FPS)