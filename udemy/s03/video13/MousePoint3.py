# code is as it was after 5:44 min in video13
# now the clicked points are saved in a list and redrawn each frame but in wrong place
#  points y-coord fixed by swapping y range in the gluOrtho2D() call ...
#
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('MousePoint3')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    #gluOrtho2D(0, 1000, 0, 800)
    gluOrtho2D(0, 1000, 800, 0)  # one possible fix


def plot_point():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


done = False
init_ortho()
glPointSize(5)
points = []
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            points.append(pygame.mouse.get_pos())

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_point()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
