import pygame, math

class OSD:
    
    
    target_rotation = 0
    
    
    def __init__(self, stage):
        self.stage = stage
    
    def update(self):
        self.target_rotation += 5
        self.fps = self.stage.clock.get_fps()
        self.tank_angle = self.stage.tank.v[1]
        
        self.stage.overlay.fill(self.stage.TRANSPARENT)                        
        for x in range(4):
            pygame.draw.circle(
                self.stage.overlay, 
                pygame.Color(0, 0, 255, 100), 
                (
                    50 + int(25 * math.cos(math.radians(self.target_rotation + x*90))), 
                    50 + int(25 * math.sin(math.radians(self.target_rotation + x*90)))
                ), 
                5                
            )
             
        
    def draw(self):
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(str(self.fps), 1, (255,255,0))
        self.stage.screen.blit(label, (100, 100))
        
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render(str(math.degrees(self.tank_angle)%360), 1, (255,255,0))
        self.stage.screen.blit(label, (100, 150))
        self.stage.screen.blit(self.stage.overlay, (self.stage.mouse_x, self.stage.mouse_y))