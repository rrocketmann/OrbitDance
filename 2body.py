import pgzrun
import math

m1=10
m2=10
v1=(0,50)
v2=(0,-50)
p1=(500,280)
p2=(100,280)
G=1000000
def draw():
    screen.fill((255 ,255 ,255))
    screen.draw.filled_circle(p2, 25.0, (120, 50, 255))
    screen.draw.filled_circle(p1, 25.0, (150, 200, 100))
def update(dt):
    global p1,v1,p2,v2
    p1 = (p1[0] + dt * v1[0], p1[1] + dt * v1[1])
    p2 = (p2[0] + dt * v2[0], p2[1] + dt * v2[1])
    r = math.sqrt((p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1]))
    f = G * m1 * m2/(r*r)
    a1 = (f/m1 * (p2[0]-p1[0]) / r, f/m1 * (p2[1]-p1[1]) / r)
    v1 = (v1[0] + dt * a1[0],v1[1] + dt * a1[1])
    a2 = (f/m2 * (p1[0]-p2[0]) / r, f/m2 * (p1[1]-p2[1]) / r)
    v2 = (v2[0] + dt * a2[0],v2[1] + dt * a2[1])

pgzrun.go()
