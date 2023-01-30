import pygame
from pygame.locals import *

from ball import Ball
import math
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("galf- by nikols")
clock = pygame.time.Clock()
mD = False
galf = Ball(500, 500)
galf.rect.x = 400
galf.rect.y = 400
allSpritesList = pygame.sprite.Group()

allSpritesList.add(galf)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == MOUSEBUTTONDOWN and galf.rect.collidepoint(pygame.mouse.get_pos()):
            mD = True
        if event.type == MOUSEBUTTONUP and mD:
            mousePosOnRelease = pygame.mouse.get_pos()
            galf.vel[0] = galf.Lvel[0] = (galf.rect.x - mousePosOnRelease[0]) / 20
            galf.vel[1] = galf.Lvel[1] = (galf.rect.y - mousePosOnRelease[1]) / 20
            galf.velop = galf.Lvelop = math.sqrt((abs(mousePosOnRelease[0] - galf.x) ** 2) + (abs(mousePosOnRelease[1] - galf.y) ** 2))
            galf.shoot = True
            galf.shootT = [True, True]
            mD = False

    screen.fill((0, 0, 0))
    allSpritesList.update()

    allSpritesList.draw(screen)
    clock.tick(60)
    pygame.display.flip()
