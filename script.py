# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:13:41 2016

@author: alex
TODO:
known issues:
Some circles stick to eachother
    This only happens when I spawn one circle inside the other. 
        create a function to handle spawning so this doesnt happen
Some circles stick to the borders. something to do with edge cases
    This may be fixed, the error is no longer observed
bouncing doesnt always act right. it doesnt bounce at the proper angle
    may just be a limitation of the math
    try single testing bounces from different angles

functionality additions:
make a slow mo function
add ability to add and throw circles by clicking
add gravity
add friction

"""

import main

#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)
background = black
colors = [red, green, blue, white, pink]
#if gameRunning = false, the game will quit 
gameRunning = True

#initialize window
clock, screen = startup(black)

#create the circleArray which holds all of the circles 
circleArray = []

#example: This creates a pink circle with mass of 100, radius 5.
circleArray.append(Circle(100, 5, pink))

for i in range(10):
    circleArray.append(Circle(100, 50, colors[i%5]))
"""
for i in range(5):
    if (random.randrange(0, 2) == 1):
        c = blue
    else:
        c = red    
    circleArray.append(Circle(100, 100, c))
"""

"""
while (not thing.within(dimensions)) or (not thing2.within(dimensions)):
    msElapsed = clock.tick(150)
    for circle in circleArray:
        circle.advance(msElapsed)
   """
   
while gameRunning:    
    msElapsed = clock.tick(150)
    #check if any of the circles are going to bounce 
    checkForCollisions(circleArray, msElapsed)
    #update all items in circleArray, then redraw the screen
    updateRedraw(screen, circleArray, msElapsed)
    checkEvents(gameRunning)
   

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();