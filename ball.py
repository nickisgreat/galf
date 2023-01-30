import pygame.sprite
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.vel = [0, 0]
        self.image = pygame.Surface([15, 15])
        self.rect = self.image.get_rect()
        self.shoot = False
        pygame.draw.rect(self.image, (255, 255, 255), [0, 0, 15, 15])
    def update(self):
        if self.shoot:
            if self.vel[0] < 0:
                self.vel[0] += 0.1 * abs(self.vel[0] / self.vel[1])
                if self.vel[0] > 0:
                    self.vel[0] = 0
                    self.shoot = False
                    return
            elif self.vel[0] > 0:
                self.vel[0] -= 0.1 * abs(self.vel[0] / self.vel[1])
                if self.vel[0] < 0:
                    self.vel[0] = 0
                    self.shoot = False
                    return
            if self.vel[1] > 0:
                self.vel[1] -= 0.1 * abs(self.vel[1] / self.vel[0])
                if self.vel[1] < 0:
                    self.vel[1] = 0
                    self.shoot = False
                    return
            elif self.vel[1] < 0:
                self.vel[1] += 0.1 * abs(self.vel[1] / self.vel[0])
                if self.vel[1] > 0:
                    self.vel[1] = 0
                    self.shoot = False
                    return
            self.rect.x += self.vel[0]
            self.rect.y += self.vel[1]