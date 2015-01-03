import pygame, math, random
from modules.ball import Ball

class TankBarrel(pygame.sprite.Sprite):
    
    firing = False
    firing_timeout = 0
    
    def __init__(self, tank, stage):
        pygame.sprite.Sprite.__init__(self)
        self.stage = stage
        self.tank = tank
        self.image = pygame.image.load("img/tank_barrel.png")
        self.image = pygame.transform.scale(self.image, [400,50])
        self.image_src = self.image
        self.rect = self.image.get_rect()
        self.rect.center = tank.rect.center[0], tank.rect.center[1]
        
        self.r = random.Random()
        self.firing_sound = pygame.mixer.Sound("sounds/gun.wav")
    
    def fire(self):
        b = Ball(
            self.stage, 
            self.tank.barrel_head[0], 
            self.tank.barrel_head[1], 
            velocity=(self.r.choice([-25, -20, -15]), self.barrel_angle)
        )
        b.add(self.stage.ballgroup)
        self.firing_sound.play()
    
    def update(self):
        
        deltaY = self.rect.center[1] - self.stage.mouse_y
        deltaX = self.rect.center[0] - self.stage.mouse_x                
        
        angle = math.atan2(deltaY, deltaX)
        self.image = pygame.transform.rotate(self.image_src, -math.degrees(angle))
        
        self.rect = self.image.get_rect()
        
        width = self.rect[2] - self.rect[0]
        height = self.rect[3] - self.rect[1]
        
        self.rect.center = self.tank.rect.center[0] - 20, self.tank.rect.center[1] - 20

        x1 = 3.5 * math.degrees(math.cos(angle))
        y1 = 3.5 * math.degrees(math.sin(angle))
        
        self.tank.barrel_head = self.rect.center[0] - x1, self.rect.center[1] - y1
        self.barrel_angle = angle
        
        if TankBarrel.firing:
            if TankBarrel.firing_timeout < 5:
                TankBarrel.firing_timeout += 1
            else:
                TankBarrel.firing_timeout = 0
                self.fire()        
                
            
            
        
        
    