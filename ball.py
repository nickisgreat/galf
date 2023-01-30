import pygame.sprite
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.vel = [0, 0]
        self.Lvel = [0, 0]
        self.velop = 0
        self.Lvelop = 0
        self.image = pygame.Surface((15, 15))
        self.rect = self.image.get_rect()
        self.shoot = False
        self.shootT = [False, False]
        pygame.draw.circle(self.image, (255, 255, 255), self.rect.center, 7.5, 15)
    def update(self):
        if self.shoot:
            self.vel = [(self.velop/self.Lvelop)*self.Lvel[0], (self.velop/self.Lvelop)*self.Lvel[1]]

            self.rect.x += self.vel[0]
            self.rect.y += self.vel[1]

            if self.velop > 0:
                self.velop -= 5
            else:
                self.shoot = False
                self.velop = 0
                self.vel = [0, 0]
