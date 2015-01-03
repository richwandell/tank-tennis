from modules.stage import Stage
from modules.main_menu import MainMenu
import json, pygame
pygame.init()
pygame.mixer.init()

screen, world = pygame.display.set_mode((0, 0),), {}

def showMenu():
    global world, screen 
    world = MainMenu(screen)

def playLevel(level):
    global world, screen
    level1 = json.loads("".join(open("levels/level%s.json" % str(level)).readlines()))
    world = Stage(screen, level1)

if __name__ == "__main__":
    playLevel(1)
    
