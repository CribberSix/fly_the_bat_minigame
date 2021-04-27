import pygame


class Block:

    def __init__(self, x, y, img, screen=None):

        self.x = x
        self.y = y
        self.img = img
        self.img_rect = img.get_rect()
        self.img_rect.x = x
        self.img_rect.y = y
        self.screen = screen if screen is not None else pygame.display.get_surface()

    def render(self):
        self.screen.blit(self.img, self.img_rect)

    def move(self, speed):
        self.img_rect.x -= speed
