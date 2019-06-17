#author:shuaihu
# -*- coding:utf-8 -*-
#It may take another three or five years for me to truly become the 'great' version of myself that I am,
#and how happy I would be to have you around all the time.

import pygame,sys


pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption("Pygame游戏之旅")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()
