import pygame, math
from modules.world_object import WorldObject
class ConcreteSlab(pygame.sprite.Sprite, WorldObject):            
    def __init__(self, stage, x, y, image="img/concrete_slab1.jpg"):
        pygame.sprite.Sprite.__init__(self)
        self.stage = stage
        self.image_src = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image_src, [int(stage.width*.05), int(stage.height*.05)])
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        
    def update(self):
        if self.alive():
            if WorldObject.world_moving:
                if self.stage.fast:
                    self.rect.center = self.rect.center[0] - 10, self.rect.center[1]
                else:
                    self.rect.center = self.rect.center[0] - 1, self.rect.center[1]
                    
                if self.rect.right < 0:
                    self.kill()
            
class ConcreteSlab2(ConcreteSlab):
    def __init__(self, stage, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.stage = stage
        self.image_src = pygame.image.load("img/concrete_slab2.jpg")
        self.image = pygame.transform.scale(self.image_src, [int(stage.width*.02), int(stage.height*.08)])
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        