import numpy as np
import math
import time

from itertools import product

from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import pygame



pygame.init()

display = 1200, 700

pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

glMatrixMode(GL_PROJECTION)
gluPerspective(60, (display[0]/display[1]), 0.1, 500)

pause = False
end_it = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_it = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end_it = True
            if event.key == pygame.K_SPACE:
                pause ^= True
        
    if end_it:
        break

    if pause:
        pygame.time.sleep(300)

pygame.quit()


