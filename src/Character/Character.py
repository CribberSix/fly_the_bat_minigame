import pygame


class Character:

    def __init__(self, scale=1, screen=None):
        self.width = int(scale * 100)
        self.img = pygame.transform.scale(pygame.image.load("resources/Character/character.png"), (self.width, self.width))
        self.img_rect = self.img.get_rect()
        self.img_rect.center = (200, 200)
        self.screen = screen if screen is not None else pygame.display.get_surface()
        self.speed = 2

    def move(self, pressed_keys):
        self.img_rect.x += 0
        if pressed_keys[ord('w')]:
            self.img_rect.y -= self.speed
        elif pressed_keys[ord('s')]:
            self.img_rect.y += self.speed
        elif pressed_keys[ord('a')]:
            self.img_rect.x -= self.speed
        elif pressed_keys[ord('d')]:
            self.img_rect.x += self.speed

    def render(self):
        self.screen.blit(self.img, self.img_rect)


