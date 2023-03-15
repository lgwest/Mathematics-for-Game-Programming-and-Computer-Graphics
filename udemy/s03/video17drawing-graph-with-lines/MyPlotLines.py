# challenge after 1:24 min in video 17
import math

import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

screen_width = 1000
screen_height = 800
ortho_width = 640
ortho_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Graphs in PyOpenGL')


def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_height)
    #gluOrtho2D(0, 4, -1, 1)

def plot_graph():
    glBegin(GL_POINTS)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(0, 4, 0.005):
        py = math.exp(-px) * math.cos(2 * math.pi * px)
        glVertex2f(map_value(0, 4, 0, ortho_width, px), map_value(-1, 1, 0, ortho_height, py))
        #glVertex2f(px, py)
    glEnd()


def plot_point():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_lines():
    for l in points:
        glBegin(GL_LINE_STRIP)
        for coords in l:
            glVertex2f(coords[0], coords[1])
        glEnd()

def plot_lines_tst():
    poly = [
        (4, 7),
        (40, 470),
        (320, 240),
        (630, 460),
        (635, 5),
        (7, 8),
    ]
    glBegin(GL_LINES)
    for point in poly:
        glVertex2i(point[0], point[1])
    glEnd()


done = False
init_ortho()
glPointSize(5)
points = []
line = []
mouse_down = False

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #plot_graph()
    plot_lines_tst()
    pygame.display.flip()
    # pygame.time.wait(100)
pygame.quit()
