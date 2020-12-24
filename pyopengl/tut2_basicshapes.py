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

glTranslate(0,0,-10)


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

    "Drawing single red point"
    glBegin(GL_POINTS)
    glColor(1,0,0)
    glVertex3f(0,0,0)
    glEnd()
    
    "Draw single line"
    glLineWidth(5.5)
    glColor(1,1,0)
    glBegin(GL_LINES)
    glVertex3f(-5,0,0)
    glVertex3f(5,0,0)
    glEnd()

    "Draw single traingle"
    glLineWidth(5.5)
    glColor(0.8,0.5,0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-5,1,0)
    glVertex3f(5,1,0)
    glVertex3f(0,4,0)
    glEnd()

    "Draw single quad"
    glLineWidth(5.5)
    glColor(0,0.7,0)
    glBegin(GL_QUADS)
    glVertex3f(-5,-5, 0)
    glVertex3f( 5,-5, 0)
    glVertex3f( 5, 5, 0)
    glVertex3f(-5, 5, 0)
    glEnd()
    
    if end_it:
        break

    if pause:
        pygame.time.sleep(300)

    pygame.display.flip()

pygame.quit()


