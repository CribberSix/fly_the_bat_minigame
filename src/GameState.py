import pygame
import sys
from src.Visualizer.Visualizer import Visualizer
from src.Character.Character import Character
from src.Fin.Endscreen import Endscreen


class GameState:

    def __init__(self, screen=None):
        # PYGAME
        self.clock = pygame.time.Clock()
        self.FPS = 30
        self.screen = screen if screen is not None else pygame.display.get_surface()
        w, h = self.screen.get_size()
        scaling = h / 1000  # calculate correct scaling of objects for every screen size

        # GAME  SETUP
        self.map = []
        self.viz = Visualizer(scale=scaling)
        self.character = Character(int(w/4), int(h/2), scale=scaling)
        self.game_speed = 3
        self.game_speed_max = 8
        self.last_update_on = 0

        # Point system
        self.points = 0
        self.font = pygame.font.Font("resources/Fonts/Quicksand-Bold.ttf", 20)
        self.point_y = h - 35
        self.point_x = 5

        # Borders top & bottom
        self.border_top = pygame.Rect((0, 0), (w, 10))
        self.border_bottom = pygame.Rect((0, h - 10), (w, 10))

    def render_points(self):
        ts = self.font.render(str(int(self.points)), False, (0, 0, 0))
        self.screen.blit(ts, (self.point_x, self.point_y))

    def collision_detection(self):
        if self.character.hitbox.colliderect(self.border_bottom) or self.character.hitbox.colliderect(self.border_top):
            Endscreen(int(self.points)).render()
            return True

        for b in self.viz.block_objects:
            if self.character.hitbox.colliderect(b.hitbox):
                Endscreen(int(self.points)).render()
                return True
        return False

    def run(self):
        while True:
            self.points += 0.1 * self.game_speed

            # increase game difficulty over time
            #   -> every 100 points, speed goes up (until max speed)
            #   -> at 500 points, the minimum space is reduced to 3
            if int(self.points) != self.last_update_on and int(self.points) % 100 == 0 and self.game_speed < self.game_speed_max:
                self.last_update_on = int(self.points)
                self.game_speed += 1  # too fast, not enough space to go up/down
                if int(self.points) % 200 == 0:
                    self.character.animation_update -= 1
                if int(self.points) == 500 and self.viz.map_generator.min_space >= 4:
                    self.viz.map_generator.min_space = 3
            pygame_events = pygame.event.get()

            for event in pygame_events:
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.get_surface().fill((200, 200, 200))  # draw background

            # Movement
            self.character.move(pygame_events)
            self.viz.move_blocks(self.game_speed)
            self.viz.render()
            # Visuals
            pygame.draw.rect(self.screen, (0, 0, 0), self.border_bottom)
            pygame.draw.rect(self.screen, (0, 0, 0), self.border_top)
            self.character.render()
            self.render_points()

            if self.collision_detection():
                return

            pygame.display.flip()  # update screen
            self.clock.tick(self.FPS)
