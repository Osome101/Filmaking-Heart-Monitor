import pygame
from pygame.locals import *
import pygame.freetype  # Import the freetype module.
import numpy as np
from pysinewave import SineWave
#import simpleaudio as sa
import sys
import os

ni = "102/69"
ni1 = "102"
ni2 = "69"
bp = "70"
sp = "97"
alive = True
x = 0

#define display surface
W, H = 1900, 1035
HW, HH = W / 2, H / 2
AREA = W * H

#setup pygame
sinewave = SineWave(pitch = 13)
#wave_obj = sa.WaveObject.from_wave_file("ecg.wav")
#wave_obj.play()

pygame.init()

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
ecg = pygame.mixer.Sound("./data/ecg.wav")
ecg.play()

myfont = pygame.freetype.SysFont('Fixedsys Regular', 220)

CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("MONITOR CODED BY OHAD MAMET 4/9/20")
FPS = 170

bkgd = pygame.image.load("./data/ecg3.png").convert()
stats = pygame.image.load("./data/stats.png").convert()
flat = pygame.image.load("./data/flat.png").convert()

def flatline():
    print("flatlining")
    ecg.stop()
    sinewave.play()
    while True:
        FPS = 15
        events()
        DS.blit(flat, (0, 0))
        DS.blit(stats, (1200, 0))
        global sp
        global bp
        global ni1
        global ni2
        if int(sp) > 0:
            sp = str(int(sp)-1)
        if int(bp) > 0:
            bp = str(int(bp)-1)
        if int(ni1) > 0:
            ni1 = str(int(ni1)-1)
        if int(ni2) > 0:
            ni2 = str(int(ni2)-1)
        ni = ni1 + "/" + ni2
        myfont.render_to(DS, (1585, 815), sp, (222, 202, 61))
        myfont.render_to(DS, (1300, 480), ni, (195, 29, 212))
        myfont.render_to(DS, (1585, 135), bp, (23, 251, 23))
        pygame.display.update()
        CLOCK.tick(FPS)


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            ecg.stop()
            sinewave.stop()
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            flatline()

#main loop
while True:
    events()

    rel_x = x % bkgd.get_rect().width
    DS.blit(bkgd, (rel_x - bkgd.get_rect().width, 0)) 
    if rel_x < W:
        DS.blit(bkgd, (rel_x, 0))
    x -= 1
    DS.blit(stats, (1200, 0))
    if (rel_x == 300 or rel_x == 800) and alive:
        sp = str(np.random.randint(low=96, high=98, size=1))[1:-1]
    if rel_x == 1150 and alive:
        ni1 = str(np.random.randint(low=90, high=99, size=1))[1:-1]
        ni2 = str(np.random.randint(low=62, high=75, size=1))[1:-1]
        ni = ni1 + "/" + ni2
    if (rel_x == 700 or rel_x == 100) and alive:
        bp = str(np.random.randint(low=65, high=72, size=1))[1:-1]
    myfont.render_to(DS, (1585, 815), sp, (222, 202, 61))
    myfont.render_to(DS, (1300, 480), ni, (195, 29, 212))
    myfont.render_to(DS, (1585, 135), bp, (23, 251, 23))
    pygame.display.update()
    CLOCK.tick(FPS)


