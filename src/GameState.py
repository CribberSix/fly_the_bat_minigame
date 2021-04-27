import pygame
import sys
from src.Map.MapGenerator import MapGenerator
from src.Visualizer.Visualizer import Visualizer
from src.Character.Character import Character
from src.Fin.Endscreen import Endscreen


class GameState:

    def __init__(self, screen=None):
        scaling = 0.5

        # PYGAME
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.screen = screen if screen is not None else pygame.display.get_surface()

        # GAME  SETUP
        self.map = []
        self.viz = Visualizer(scale=scaling)
        self.map_generator = MapGenerator()
        self.character = Character(scale=scaling)
        self.game_speed = 1

        # Point system
        self.points = 0
        self.font = pygame.font.Font("resources/Fonts/Quicksand-Bold.ttf", 20)
        w, h = self.screen.get_size()
        self.point_y = h - 25
        self.point_x = 5

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
        textsurface = self.font.render(str(self.points), False, (0, 0, 0))
        self.screen.blit(textsurface, (self.point_x, self.point_y))

    def run(self):
        while True:
            self.points += self.game_speed
            pygame_events = pygame.event.get()
            pressed_keys = pygame.key.get_pressed()

            for event in pygame_events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.get_surface().fill((200, 200, 200))  # draw background

            self.character.move(pressed_keys)

            self.viz.move_blocks(self.game_speed)
            self.viz.render()
            self.character.render()
            self.render_points()

            for b in self.viz.block_objects:
                collision = self.character.img_rect.colliderect(b.img_rect)
                if collision:
                    Endscreen(self.points).render()
                    return

            pygame.display.flip()  # update screen
            self.clock.tick(self.FPS)