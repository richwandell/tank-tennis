import pygame, math
from os import listdir
from modules.ball import Ball
from modules.tank import Tank
from modules.tank_barrel import TankBarrel
from modules.level import Level
from modules.osd import OSD

class Stage:
    
    fast = False
    
    loading_frames = []
    
    TRANSPARENT = (255,0,255)
    
    def __init__(self, screen, level):        
        self.mouse_x, self.mouse_y = 0,0
        self.screen = screen
        
        pygame.mouse.set_visible(False)

        Ball.screen = self.screen
        Tank.screen = self.screen
        self.clock = pygame.time.Clock()
        
        self.play = True
        
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.overlay = pygame.Surface((100, 100))
        self.overlay.set_colorkey(self.TRANSPARENT)
        self.overlay.set_alpha(100)
        
        bg_ = pygame.image.load('img/outerspace.jpg').convert()
        self.bg = pygame.transform.scale(bg_, (self.width, self.height))
        
        self.ballgroup = pygame.sprite.RenderPlain([])
        tank = Tank(self)
        self.tank = tank
        self.tankgroup = pygame.sprite.RenderPlain([
            tank,
            TankBarrel(tank, self)
        ])
        
#        music = pygame.mixer.music.load("sounds/Tranceformer.wav")
#        pygame.mixer.music.play(-1)
        
        
        self.cLevel = Level(level, self)
        self.osd = OSD(self)
        while self.play:
            self.clock.tick(60)
            self.handleEvents()
            self.drawThings()
        pygame.quit()
        
    def handleEvents(self):
        for event in pygame.event.get():                                        
            if event.type == pygame.KEYDOWN:
                if event.key == 27: #esc
                    self.play = False
                elif event.key == pygame.K_f:
                    self.fast = True
                elif event.key == pygame.K_w:
                    self.tank.jump()
                elif event.key == pygame.K_a:
                    self.tank.moving_left = True
                elif event.key == pygame.K_d:
                    self.tank.moving_right = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    self.fast = False
                elif event.key == pygame.K_a:
                    self.tank.moving_left = False
                elif event.key == pygame.K_d:
                    self.tank.moving_right = False                
            elif event.type == pygame.MOUSEMOTION:
                self.mouse_x, self.mouse_y = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                TankBarrel.firing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                TankBarrel.firing = False           

    def drawThings(self):
        self.cLevel.checkCollisions()      
        self.screen.fill([0,0,0])#clear the screen
        self.screen.blit(self.bg, (0,0))#draw background
        #draw level
        self.cLevel.update()
        self.cLevel.draw(self.screen)
        #draw player 
        self.tankgroup.update()
        self.tankgroup.draw(self.screen)
        #draw balls
        self.ballgroup.update()
        self.ballgroup.draw(self.screen)
          
        self.osd.update()
        self.osd.draw()
        pygame.display.flip()
        
        
        
        