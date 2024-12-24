# importing libraries
import pygame
import numpy
import sys

# setting constants
WIDTH = 420
HEIGHT = 400
m1 = 10
m2 = 10
m3 = 10
v1 = numpy.array([-25, 25])
v2 = numpy.array([-100, 100])
v3 = numpy.array([100, -100])
p1 = numpy.array([210, 200])
p2 = numpy.array([310, 200])
p3 = numpy.array([90, 200])
G = 15 ^ 10000000
FPS = 90
MIN_R = 40.0
running = True
dt = 0.01

# creating the screen and clock
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("hello_world")
screen.fill((0, 0, 0))
clock = pygame.time.Clock()

def draw():
    # drawing the astronomical bodies and clearing the screen
    global p1, p2, p3, screen
    pygame.draw.circle(screen, (0, 255, 255), p1, 1)
    pygame.draw.circle(screen, (255, 0, 255), p2, 1)
    pygame.draw.circle(screen, (255, 255, 0), p3, 1)
    pygame.display.flip()

def update(dt):
    # updating the positions
    global p1, v1, p2, v2, p3, v3
    p1 = p1 + dt * v1
    p2 = p2 + dt * v2
    p3 = p3 + dt * v3
    # dealing with crashing
    r12 = max(MIN_R, numpy.linalg.norm(p2 - p1))
    r13 = max(MIN_R, numpy.linalg.norm(p3 - p1))
    r23 = max(MIN_R, numpy.linalg.norm(p2 - p3))
    f12 = G * m1 * m2 * (p2 - p1) / pow(r12, 3)
    f13 = G * m1 * m3 * (p3 - p1) / pow(r13, 3)
    f23 = G * m2 * m3 * (p3 - p2) / pow(r23, 3)
    #updating the velocities
    v1 = v1 + dt * (f12 + f13) / m1
    v2 = v2 + dt * (-f12 + f23) / m2
    v3 = v3 + dt * (-f23 + -f13) / m3

while running:
    clock.tick(FPS)
    # in case of exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # drawing and updating at 90 FPS
    draw()
    update(dt)
