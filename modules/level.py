import pygame, math
from modules.concrete_slab import *
import modules.game_utils as utils

class Level:
    
    level_objects = pygame.sprite.RenderPlain([])
    
    def __init__(self, level_data, stage):
        self.level_data = level_data
        self.stage = stage
        for obj in level_data:
            for key, value in obj.items():
                if key == "ConcreteSlab": 
                    for _obj in obj["ConcreteSlab"]["coords"]:
                        ConcreteSlab(
                            stage,
                            stage.width * _obj[0],
                            stage.height * _obj[1]
                        ).add(self.level_objects)   
                elif key == "ConcreteSlab2":
                    for _obj in obj["ConcreteSlab2"]["coords"]:
                        ConcreteSlab2(
                            stage,
                            stage.width * _obj[0],
                            stage.height * _obj[1]
                        ).add(self.level_objects)
                elif key == "ConcreteSlabDarkTop":
                    for _obj in obj["ConcreteSlabDarkTop"]["coords"]:
                        ConcreteSlab(
                            stage,
                            stage.width * _obj[0],
                            stage.height * _obj[1],
                            image="img/concrete_slab1_dark_top.jpg"
                        ).add(self.level_objects)               
    
    def checkCollisions(self):
        colliders = pygame.sprite.spritecollide( 
            self.stage.tank,
            self.level_objects,
            False
        )

        tank = self.stage.tank

        if len(colliders) > 0:                                         
            
            dx = tank.v[0] * math.cos(tank.v[1])
            dy = tank.v[0] * math.sin(tank.v[1])
            
            for obj in colliders:                                                                                                                                   
                                                
                if math.fabs((tank.rect.bottom-dy) - obj.rect.top) < obj.rect.height / 2:                    
                    tank.v = utils.addVectors(tank.v, (-tank.v[0], tank.v[1]))
                    tank.rect.bottom = obj.rect.top
                    tank.jumping = False
                elif tank.rect.bottom > obj.rect.center[1] and math.fabs(tank.rect.right - obj.rect.left) < math.fabs(tank.rect.left - obj.rect.right):
                    tank.rect.right = obj.rect.left
                    tank.v = tank.v[0], math.radians(180) - tank.v[1]
                elif tank.rect.bottom > obj.rect.center[1]:
                    tank.rect.left = obj.rect.right
                    tank.v = tank.v[0], math.radians(180) - tank.v[1]

        colliders = pygame.sprite.groupcollide(
            self.stage.ballgroup, 
            self.level_objects, 
            False, 
            False
        )
            
        if len(colliders) > 0:            
            for ball in colliders:         
                       
                c = colliders[ball][0]
                if math.fabs(ball.rect.bottom - c.rect.top) < c.rect.height / 2:                    
                    ball.rect.bottom = c.rect.top
                    ball.v = ball.v[0], math.radians(360) - ball.v[1]                    
                elif math.fabs(ball.rect.right - c.rect.left) < c.rect.width / 2:
                    ball.rect.right = c.rect.left
                    ball.v = ball.v[0], math.radians(180) - ball.v[1]
                elif math.fabs(ball.rect.left - c.rect.right) < c.rect.width / 2:
                    ball.rect.left = c.rect.right
                    ball.v = ball.v[0], math.radians(180) - ball.v[1]
                
                
        
                
                
            
            
    def update(self):
        self.level_objects.update()
    
    def draw(self, screen):
        self.level_objects.draw(screen)