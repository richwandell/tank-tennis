import pygame, math
import modules.game_utils as utils
from collections import deque
from modules.world_object import WorldObject

class Ball(pygame.sprite.Sprite, WorldObject):        
    
    m = 1   
    
    balls = deque()
    
    max_balls = 50
    
    rotation = 0
    
    
    
    def __init__(self, stage, x, y, velocity={}):
        pygame.sprite.Sprite.__init__(self)
        self.stage = stage  
        
        if len(Ball.balls) > Ball.max_balls:
            b = Ball.balls.popleft()
            self.stage.ballgroup.remove(b)
        
        Ball.balls.append(self)
        
        self.G = (self.m * ((9.8*.08)**2), math.radians(90)) 
        
                 
        self.v = velocity
        self.image_src = pygame.image.load("img/tennis_ball.png")
        self.image_src = pygame.transform.scale(self.image_src, [20,20])
        self.image = self.image_src
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        
        
        
    def boundsReachedHandler(self, side):      
        if side == "top":                
            self.v = self.v[0], math.radians(360) - self.v[1]
        elif side == "bottom":            
            self.v =self.v[0] - 1, math.radians(360) - self.v[1]
        elif side == "left" or side == "right":
            self.v = self.v[0], math.radians(180) - self.v[1]
    
    
    
    def update(self):            
   
        self.v = utils.addVectors(self.v, self.G)        
        
        dx = self.v[0] * math.cos(self.v[1])
        dy = self.v[0] * math.sin(self.v[1])
        
        self.rect = self.rect.move(dx, dy)
        
        self.checkScreenBounds()
            