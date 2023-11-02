import pygame
import os

SIZESCREEN = WIDTH, HEIGHT = 1920, 1020

LIGHTBLUE = pygame.color.THECOLORS['lightblue']

screen = pygame.display.set_mode(SIZESCREEN)

path = os.path.join(os.pardir, 'images')
file_names = sorted(os.listdir(path))

file_names.remove('background.png')
BACKGROUND = pygame.image.load(os.path.join(path, 'background.png')).convert()
for file_name in file_names:
    image_name = file_name[:-4].upper()
    globals()[image_name] = pygame.image.load(os.path.join(path, file_name)).convert_alpha(BACKGROUND)
