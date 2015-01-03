import pygame, math
import modules.game_utils as utils 
class Tank(pygame.sprite.Sprite):
    
    audio_playing = False
    
    m = 5
    
    def __init__(self, stage):
        pygame.sprite.Sprite.__init__(self)  
        self.moving_left = False
        self.moving_right = False  
        self.jumping = False
        self.barrel_head = 0,0
        self.stage = stage
        self.image = pygame.image.load("img/tank_main.png")
        self.image = pygame.transform.scale(self.image, [200,100])
        self.rect = self.image.get_rect()
        self.rect.center = self.screen.get_width() / 2, self.screen.get_height() / 2       
        self.idle_sound = pygame.mixer.Sound('sounds/tank_idle.wav')
        self.idle_sound.play(-1)
        self.G = (self.m * ((9.8*.08)**2), math.radians(90)) 
        self.v = 0, 0
    
    def jump(self):    
                
        if not self.jumping:    
            self.rect.y -= 20
            self.jumping = True         
            self.v = utils.addVectors(self.v, (40, math.radians(270)))
                        
    def update(self):
        if self.moving_right and not self.jumping:
            self.v = utils.addVectors(self.v, (5, math.radians(0)))
        elif self.moving_left and not self.jumping:
            self.v = utils.addVectors(self.v, (-5, math.radians(0)))                    
                
        
        self.v = utils.addVectors(self.v, self.G) 
        
        
        dx = self.v[0] * math.cos(self.v[1])
        dy = self.v[0] * math.sin(self.v[1])
        
        self.rect = self.rect.move(dx, dy)
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > self.stage.width:
            self.rect.x = self.stage.width - self.rect.width
        elif self.rect.bottom > self.stage.height:
            self.rect.bottom = self.stage.height
        
        
    
        
    