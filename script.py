# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:13:41 2016

@author: alex
TODO:
add ability to add and throw circles by clicking
add gravity

known issues:
bouncing doesnt always act right. it doesnt bounce at the proper angle
may just be a limitation of the math
try single testing bounces from different angles

functionality:
make a slow mo function


"""

import main

WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 1500
dimensions = (WINDOW_HEIGHT, WINDOW_WIDTH)

#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

gameRunning = True

#initialize window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(black)
thing = Circle(100, 5, blue)
thing2 = Circle(1000, 5, white)

thing.x[0] = 0
thing.y[0] = 0
thing.x[1] = 500 #pixels per second
thing.y[1] = 500
thing2.x[0] = WINDOW_WIDTH
thing2.y[0] = WINDOW_HEIGHT
thing2.x[1] = -500
thing2.y[1] = -500

circleArray = []
circleArray.append(thing)
circleArray.append(thing2)
circleArray.append(Circle(100, 5, pink))
for i in range(100):
    if (random.randrange(2) % 2 == 0):
        c = blue
    else:
        c = red    
    circleArray.append(Circle(100, 5, c))
 
#eventually also make accelleration act on velocity
#draw circle to screen

while (not thing.within(dimensions)) or (not thing2.within(dimensions)):
    msElapsed = clock.tick(150)
    for circle in circleArray:
        circle.advance(msElapsed)
        
    #thing.advance(msElapsed)
    #thing2.advance(msElapsed)
    
while gameRunning:    
    #check if any of the circles are going to bounce 
    for i in range(len(circleArray) - 1):
        for j in range(i+1, (len(circleArray) - 1)):
            (circleArray[i]).collisionIsNear(circleArray[j])
        (circleArray[i]).borderBounce(dimensions)
        (circleArray[i]).advance(msElapsed)
    (circleArray[-1]).borderBounce(dimensions)
    (circleArray[-1]).advance(msElapsed)
    
#    thing.collisionIsNear(thing2) #check for collisions!
#    thing.borderBounce(dimensions)
#    thing2.borderBounce(dimensions)
#    thing.advance(msElapsed)
#    thing2.advance(msElapsed)

    #redraw the screen!
    screen.fill(black)
    for c in circleArray:
        pygame.draw.circle(screen, c.color, c.getPos(), c.radius, 3)
    #pygame.draw.circle(screen, thing2.color, thing2.getPos(), thing2.radius, 3)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
            gameRunning = False

    msElapsed = clock.tick(150)
    
    #print(thing.getPos())
    #print(str(thing.getPos()[0] + thing.radius))
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();