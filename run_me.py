from src.GameState import GameState
import pygame
pygame.font.init()


# ________________ PYGAME SETUP ________________ #
systemWidth = 750
systemHeight = 750
screen = pygame.display.set_mode((systemWidth, systemHeight))
pygame.display.set_caption("A bat's flight")
gameIcon = pygame.image.load('resources/icon.png')
pygame.display.set_icon(gameIcon)

while True:
    game = GameState()
    game.run()



