from pygame_codeassets import TextButton
import pygame
import sys


class Endscreen:

    def __init__(self, points, screen=None):

        self.text = "THE END"
        self.screen = screen if screen is not None else pygame.display.get_surface()
        self.points = points

        self.button_w = 300
        self.button_h = 50
        w, h = pygame.display.get_surface().get_size()
        self.button_x = int((w/2) - (self.button_w / 2))
        self.button_y = int((h / 2) - (self.button_h / 2))

        color_bg_active = (42, 157, 143)
        color_bg_inactive = (0, 0, 0)
        self.button_continue = TextButton(self.screen, self.button_x, self.button_y, self.button_w, self.button_h,
                                          "Continue", color_bg_active, color_bg_inactive)

        self.font = pygame.font.Font("resources/Fonts/Quicksand-Bold.ttf", 30)

        self.points_textsurface = self.font.render(f"You got {str(self.points)} points!", False, (0, 0, 0))
        text_w = self.points_textsurface.get_width()
        text_h = self.points_textsurface.get_height()
        self.text_x = int((w/2) - (text_w / 2))
        self.text_y = int((h / 2) - (text_h / 2)) - 100

        self.points_background = pygame.Rect(self.text_x - 10, self.text_y, text_w + 20, text_h)


    def render(self):
        while True:
            # Pygame input
            mouse = pygame.mouse.get_pos()
            pygame_events = pygame.event.get()
            for event in pygame_events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Rendering
            pygame.draw.rect(self.screen, (255, 255, 255), self.points_background)
            self.screen.blit(self.points_textsurface, (self.text_x, self.text_y))
            reset_return = self.button_continue.render(mouse, pygame_events)
            if reset_return is not None:
                return

            pygame.display.flip()
            pygame.time.Clock().tick(30)
