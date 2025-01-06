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
p1 = numpy.array([210.0, 200.0])
p2 = numpy.array([310.0, 200.0])
p3 = numpy.array([90.0, 200.0])
v1 = numpy.array([-25.0, 25.0])
v2 = numpy.array([-100.0, 100.0])
v3 = numpy.array([100.0, -100.0])
G = 5e6 # real one is 6.674e-11
FPS = 90
MIN_R = 40.0
running = True
dt = 0.01

# creating the screen, clock, and dimming surface
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("OrbitDance")
screen.fill((0, 0, 0))
clock = pygame.time.Clock()
draw_surface = pygame.Surface((WIDTH,HEIGHT))
draw_surface.set_alpha(10)
draw_surface.fill((0, 0, 0))

def draw():
    # drawing the astronomical bodies and making the old paths look dimmer
    global p1, p2, p3, screen, draw_surface
    screen.blit(draw_surface, (0, 0))
    pygame.draw.circle(screen, (0, 255, 255), p1, 10)
    pygame.draw.circle(screen, (255, 0, 255), p2, 10)
    pygame.draw.circle(screen, (255, 255, 0), p3, 10)
    pygame.display.flip()

def update(dt):
    global p1, v1, p2, v2, p3, v3, G

    p1 += dt * v1
    p2 += dt * v2
    p3 += dt * v3

    # dealing with crashing
    r12 = max(MIN_R, numpy.linalg.norm(p2 - p1))
    r13 = max(MIN_R, numpy.linalg.norm(p3 - p1))
    r23 = max(MIN_R, numpy.linalg.norm(p2 - p3))

    # computing the forces using the gravitational equation
    f12 = G * m1 * m2 * (p2 - p1) / pow(r12, 3)
    f13 = G * m1 * m3 * (p3 - p1) / pow(r13, 3)
    f23 = G * m2 * m3 * (p3 - p2) / pow(r23, 3)

    # computing the acceleration
    a1 = (f12 + f13) / m1
    a2 = (-f12 + f23) / m2
    a3 = (-f23 + -f13) / m3

    # updating the velocities
    v1 += dt * a1
    v2 += dt * a2
    v3 += dt * a3

while running:
    clock.tick(FPS)

    # in case of exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # drawing and updating everything at 90 FPS
    draw()
    update(dt)
