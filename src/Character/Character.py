import pygame


class Character:

    def __init__(self, x, y, scale=1, screen=None):
        width = int(scale * 100)
        self.img = pygame.transform.scale(pygame.image.load("resources/Character/tile000.png"), (width, width))
        self.img_rect = self.img.get_rect()
        self.img_rect.center = (x, y)
        self.screen = screen if screen is not None else pygame.display.get_surface()
        self.gravity = 0.15
        self.speed = 4
        self.acceleration_y = -1
        self.acc_y_max = 5
        self.acc_y_min = -5

        self.animations = [pygame.image.load("resources/Character/tile000.png"),
                           pygame.image.load("resources/Character/tile001.png"),
                           pygame.image.load("resources/Character/tile002.png"),
                           pygame.image.load("resources/Character/tile003.png"),
                           pygame.image.load("resources/Character/tile004.png"),
                           pygame.image.load("resources/Character/tile005.png"),
                           pygame.image.load("resources/Character/tile006.png"),
                           pygame.image.load("resources/Character/tile007.png"),
                           pygame.image.load("resources/Character/tile008.png"),
                           pygame.image.load("resources/Character/tile009.png"),
                           pygame.image.load("resources/Character/tile010.png")
        ]

        self.animations = [pygame.transform.scale(x, (width, width)) for x in self.animations]
        self.animation_counter = 0
        self.animation_mod = 0
        self.fly = 0

    def move(self, pygame_events):
        # only display animation after spacebar has been pressed for 20 frames - change image every 5 frames
        self.fly -= 1
        if self.fly > 0:
            self.animation_mod += 1
            if self.animation_mod % 5 == 0:
                self.animation_counter += 1
            self.animation_counter = 0 if self.animation_counter >= len(self.animations) else self.animation_counter

        for e in pygame_events:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                self.fly = 20
                self.acceleration_y -= self.speed

        self.img_rect.y += self.acceleration_y

        self.acceleration_y += self.gravity  # gravity

        self.acceleration_y = self.acc_y_min if self.acceleration_y < self.acc_y_min else self.acceleration_y
        self.acceleration_y = self.acc_y_max if self.acceleration_y > self.acc_y_max else self.acceleration_y

    def render(self):
        self.screen.blit(self.animations[self.animation_counter], self.img_rect)


