import pygame


class Parallax:

    def __init__(self, img_path, speed, surface=None):
        self.screen = surface if surface is not None else pygame.display.get_surface()
        self.screen_width, _ = self.screen.get_size()

        self.speed = speed
        self.img = pygame.image.load(img_path)
        self.bg_rect1 = self.img.get_rect()
        self.bg_rect1.x = 0
        self.bg_rect1.y = 0

        w, h = self.img.get_size()
        self.bg_rect2 = self.img.get_rect()
        self.bg_rect2.x = w
        self.bg_rect2.y = 0

    def move(self):
        self.bg_rect1.x -= self.speed
        self.bg_rect2.x -= self.speed

        if self.bg_rect1.right <= 0:
            self.bg_rect1.x = self.screen_width
        if self.bg_rect2.right <= 0:
            self.bg_rect2.x = self.screen_width

    def render(self):
        self.screen.blit(self.img, self.bg_rect1)
        self.screen.blit(self.img, self.bg_rect2)
