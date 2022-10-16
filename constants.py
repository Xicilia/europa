import pygame

pygame.init()
pygame.font.init()

WIDTH = 800
HEIGHT = 600

PLAYERSPRITEWIDTH = 75
PLAYERSPRITEHEIGHT = 75
STANDARDPLAYERSPEED = 5
STANDARDPLAYERPOS = (400, 400)
PLAYERNAME = "Колян"

WEAPONWIDTH = 25
WEAPONHEIGHT = 25

BULLETWIDTH = 25
BULLETHEIGHT = 25
BULLETSPEED = 8

THROWABLEWEAPONSPEED = 8

FPS = 60

COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255),
    "GREEN": (0, 255, 0)
}

LEFTDIRECTION = -1
RIGHTDIRECTION = 1


comicSans = pygame.font.SysFont("Comic Sans MS", 25)

DOWNPOS = 1
UPPOS = -1

HITTINGSPRITECOLLIDEWITHGARAGE = pygame.USEREVENT + 1
HITTINGSPRITECOLLIDEWITHBOMJ = pygame.USEREVENT + 2
GARAGEATTACKED = pygame.USEREVENT + 3
ATTACKPRESSEDWITHNOTENOUGHTIMEELAPSED = pygame.USEREVENT + 4
ULTPRESSEDWITHNOTENOUGHTIMEELAPSED = pygame.USEREVENT + 5

SIMPLEBOMJ = 1
BOMJMAGE = 2
BOMJWARRIOR = 3

BOMJSPEED = 1

ROCKETSPEED = 5

WALLHIT = 0
