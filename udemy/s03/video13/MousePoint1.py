# code is as it was after 3:30 min in video13
# two problems here
# 1) points disappear direct after been drawn because window is cleared and fliped
# 2) points displayed at wrong position
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('MousePoint1')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)


def plot_point(point):
    glBegin(GL_POINTS)
    glVertex2f(point[0], point[1])
    glEnd()


done = False
init_ortho()
glPointSize(5)
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    if p is not None:
        plot_point(p)
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
