# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:13:41 2016

@author: alex
TODO:
known issues:
    Some circles stick to eachother
    Some items can spawn inside eachother, fix the creation function to check for this
        
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
circleArray = [Circle(100, 50, colors[i%5]) for i in range(10)]

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