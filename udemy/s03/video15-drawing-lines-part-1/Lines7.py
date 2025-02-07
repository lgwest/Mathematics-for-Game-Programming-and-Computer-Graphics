# at end of video my solution to: "draw new line segment when key pressed"
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


def plot_point():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_line(line):
    glBegin(GL_LINE_STRIP)
    for p in line:
        glVertex2f(p[0], p[1])
    glEnd()


def plot_lines():
    for line in lines:
        plot_line(line)


init_ortho()
glPointSize(5)

points = []
lines = []
done = False
mouse_down = False
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == MOUSEBUTTONUP:
            mouse_down = False
            lines.append(points)
            points = []

        elif event.type == MOUSEMOTION and mouse_down:
            p = pygame.mouse.get_pos()
            points.append((map_value(0, screen_width, 0, ortho_width, p[0]),
                           map_value(0, screen_height, ortho_height, 0, p[1])))


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_line(points)
    plot_lines()
    pygame.display.flip()
    #pygame.time.wait(100)
pygame.quit()
