import pygame


class Block:

    def __init__(self, x, y, type, img, screen=None):
        self.type = type
        self.img = img
        self.img_rect = img.get_rect()
        self.img_rect.x = x
        self.img_rect.y = y
        w, h = img.get_size()
        scaled = w / 100
        x += 10
        if type == 1:  # block_mid
            w -= int(20 * scaled)
        elif type == 2:  # block_bottom_top
            w -= int(20 * scaled)
            y += int(5 * scaled)
        elif type == 3:   # block_top_bottom
            w -= int(20 * scaled)
            y -= int(35 * scaled)

        self.hitbox = pygame.Rect((x, y), (w, h))
        self.screen = screen if screen is not None else pygame.display.get_surface()

    def render(self):
        # pygame.draw.rect(self.screen, (0, 0, 0), self.img_rect, 2)
        # pygame.draw.rect(self.screen, (255, 255, 0), self.hitbox, 2)
        self.screen.blit(self.img, self.img_rect)

    def move(self, speed):
        self.hitbox.x -= speed
        self.img_rect.x -= speed
