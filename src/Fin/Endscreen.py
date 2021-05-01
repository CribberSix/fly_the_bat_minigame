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

        self.points_textsurface = self.font.render(f"You got {str(self.points)} points!", False, (0, 0, 0), (38, 70, 83))
        text_w, text_h = self.points_textsurface.get_size()
        self.text_x = int((w/2) - (text_w / 2))
        self.text_y = int((h / 2) - (text_h / 2)) - 100

    def render(self):
        while True:
            # Pygame input
            mouse = pygame.mouse.get_pos()
            pygame_events = pygame.event.get()
            for event in pygame_events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return  # continue by pressing the spacebar

            self.screen.blit(self.points_textsurface, (self.text_x, self.text_y))  # Render points
            reset_return = self.button_continue.render(mouse, pygame_events)
            if reset_return is not None:
                return  # continue by pressing the button

            pygame.display.flip()
            pygame.time.Clock().tick(30)
