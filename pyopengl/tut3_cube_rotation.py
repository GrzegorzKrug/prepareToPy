import numpy as np
import math
import time

from itertools import product, cycle

from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import pygame


pygame.init()
display = 1200, 700
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

glMatrixMode(GL_PROJECTION)
gluPerspective(60, (display[0]/display[1]), 0.1, 500)


glMatrixMode(GL_MODELVIEW)  # Matrix mode we select now
glTranslate(0,0,-10) 
glPushMatrix()  # OpenGL save this matirx


cube_vertices = np.array([
    *product([-1, 1], repeat=3)
])
# pt1, pt2, ....
# [x]
# [y]
# [z] 

edges = [(ind, ind2)
         for ind, vertx in enumerate(cube_vertices)
         for ind2 in np.where(
    np.absolute((cube_vertices - vertx)).sum(axis=1) == 2)[0]
    if ind2 > ind
]

print(edges)

cube_vertices = cube_vertices.T

print(cube_vertices)
faces = (
    (1, 0, 2, 3),
    (7, 5, 4, 6),
    (0, 1, 5, 4),
    (2, 3, 7, 6),
    (0, 4, 6, 2),
    (1, 5, 7, 3),
)

colors = np.random.random((24, 3))
colors = cycle(colors)
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

    glClear(GL_COLOR_BUFFER_BIT |  GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    angle = math.radians(time.time()*30)
    rotMat = np.array([
        [math.cos(angle), 0, -math.sin(angle)],
        [0, 1, 0],
        [math.sin(angle), 0, math.cos(angle)]
    ])

    glColor(1,0,0)
    cubeMat = cube_vertices.copy()    
    cubeMat = np.dot(rotMat, cubeMat)
    cubeMat = cubeMat + np.array([[2, 0, 0]]).T

    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

    transl = [math.cos(angle)*5, math.sin(angle)*3, 0 ]
    glTranslate(*transl)

    glBegin(GL_LINES)
    for edge in edges:
        ind1, ind2 = edge
        glVertex3fv(cubeMat[:, ind1])
        glVertex3fv(cubeMat[:, ind2])
    glEnd()

    glBegin(GL_QUADS)
    for face in faces:
        for vert in face:
            col = next(colors)
            glColor(col)
            glVertex3fv(cubeMat[:, vert])
    glEnd()

    glPopMatrix()

    glDisable(GL_DEPTH_TEST)
    orig_offset = np.array([0,0,0])
    glLineWidth(5)
    glBegin(GL_LINES)
    "X Red"
    glColor(1,0,0)
    glVertex3fv(orig_offset)
    glVertex3fv(orig_offset + [1,0,0])
    "Y Green"
    glColor(0,1,0)
    glVertex3fv(orig_offset)
    glVertex3fv(orig_offset + [0,1,0])
    "Z Blue"
    glColor(0,0,1)
    glVertex3fv(orig_offset)
    glVertex3fv(orig_offset + [0,0,1])
    glEnd()
    

    if end_it:
        break

    if pause:
        pygame.time.wait(300)
    else:
        pygame.time.wait(50)

    pygame.display.flip()

pygame.quit()


