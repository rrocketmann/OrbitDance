import pgzrun
import numpy

m1=100
m2=100
v1 = numpy.array([0,50])
v2 = numpy.array([0,-50])
p1 = numpy.array([500,280])
p2 = numpy.array([100,280])
G=100000

def draw():
    screen.fill((255 ,255 ,255))
    screen.draw.filled_circle(p2, 25.0, (120, 50, 255))
    screen.draw.filled_circle(p1, 25.0, (150, 200, 100))

def update(dt):
    global p1,v1,p2,v2
    p1 = p1 + dt * v1
    p2 = p2 + dt * v2
    r = numpy.linalg.norm(p2 - p1)
    f = G * m1 * m2/(r*r)
    a1 = f / m1 * (p2-p1) / r
    v1 = v1 + dt * a1
    a2 = f / m2 * (p1-p2) / r
    v2 = v2 + dt * a2

pgzrun.go()
