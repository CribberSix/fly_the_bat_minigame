from win32api import GetSystemMetrics
from src.GameState import GameState
import pygame
pygame.font.init()


# ________________ PYGAME SETUP ________________ #
fullscreen = False
if fullscreen:
    systemWidth = GetSystemMetrics(0)
    systemHeight = GetSystemMetrics(1)
    screen = pygame.display.set_mode((systemHeight, systemWidth), pygame.FULLSCREEN)
else:
    systemWidth = 500
    systemHeight = 500
    screen = pygame.display.set_mode((systemWidth, systemHeight))
pygame.display.set_caption("Sideflyer")

while True:
    game = GameState()
    game.run()



