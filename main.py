# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 11:51:20 2016

@author: alexa
"""
from datetime import datetime
import pygame
import sys
import random
random.seed()

class Matter:
    """Everything originates from matter. In my engine I treat it as a single point (1 pixel), and it can be assigned a mass"""
    def __init__(self, mass):
        self.mass = mass
        self.x = [0, 0, 0] #position, velocity, accelleration in x direction
        self.y = [0, 0, 0] #position velocity accelleration in y direction
        self.dob = datetime.now().time() #imported from datetime
        self.justBounced = False
        self.jbcounter = 0
    #setters and getters
    def setmax(self, mass):
        self.mass = mass
        
    def getmax(self):
        return self.max
        
    def setx(self, x):
        self.x = x

    def getx(self):
        return self.x

    def sety(self, y):
        self.y = y

    def gety(self):
        return self.y
    
    def reborn(self):
        """
        resets date of birth to current time
        """
        self.dob = datetime.now().time()
        
    def advance(self, msElapsed):
        """
        self.x[0] = int(self.x[0] + self.x[1]*(msElapsed/1000.0))
        self.y[0] = int(self.y[0] + self.y[1]*(msElapsed/1000.0))
        
        """
        self.x[0] = int(self.x[0] + self.x[1]*(1/150))
        self.y[0] = int(self.y[0] + self.y[1]*(1/150))
                
        #add accelleration

    def within(self, dimensions):
        """
        bounds checking for display dimensions
        """
        if self.x[0] < 0 or self.x[0] > dimensions[0]:
            return False
        if self.y[0] < 0 or self.y[0] > dimensions[1]:
            return False
        return True
        
class Circle(Matter):
    """ 
    use: Circle(mass, radius, color)
    returns: a Circle Object    
    inherits from matter: 
        mass, 
        x, 
        y, 
        and dob. 

        additional things:
        radius,
        color
        """
    def __init__(self, mass, radius, color):
        """ 
        Currently overwrites mass to 100, I was simulating as many colliding circles as possible, and 
        wanted a constant mass
        Also it is currenlty initializing circles with a random position and velocity
        """
        mass = 100
        super().__init__(mass) 
        self.radius = radius
        self.color = color
        #these lists are {position, velocity, acceleration}
        #acceleration is not yet implemented. S
        self.x[0] = random.randrange(radius+10, 1500, radius*2+10 ) 
        self.y[0] = random.randrange(radius+10, 1000, radius*2+10 )
        self.x[1] = random.randrange(1, 400, 100)
        self.y[1] = random.randrange(1, 400, 100)
        assert self.mass >= 0
        assert radius >= 0

    def getPos(self):
        #returns the center of the circle
        return (self.x[0], self.y[0])
        
    def within(self, dimensions):
        #bounds checking for the display dimensions
        if self.x[0] - self.radius < 0 or self.x[1] + self.radius > dimensions[1]:
            return False
        if self.y[0] - self.radius < 0 or self.y[0] + self.radius > dimensions[0]:
            return False
        return True
    
    def collision(self, other):
        #find the distance from the center of the two circles
            
        x1, y1 = self.getPos()
        x2, y2 = other.getPos()
        #a*a is faster than a**2 in python. I looked for a carmack-y solution to make this faster but none exist (yet)
        d = ((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))**(1/2)
        #if the distance between the center of the two circles is less than or e
        #equal to their radius combined, then a collision has ocurred!
        #may have to pad this incase things start moving faster. Check here if circles are moving closer than I want to allow them.
        if d <= self.radius + other.radius:
            self.bounce(other)
            return True
        else:
            return False
    
    def bounce(self, other):
        #uses the conservation law of linear momentum
        #http://www.myphysicslab.com/collideSpring.html#collisions
        massT = self.mass + other.mass
        dx = (2 * (self.mass*self.x[1] + other.mass*other.x[1] )/massT)
        dy = (2 * (self.mass*self.y[1] + other.mass*other.y[1])/massT)
        self.x[1] = -self.x[1] + dx
        self.y[1] = -self.y[1] + dy
        other.x[1] = -other.x[1] + dx
        other.y[1] = -other.y[1] + dy
        return

    def bounce2(self, other):
        #new and improved version of bounce. it uses Elastic Collision!
        #also keeps balls from sticking together (old bounce sometimes did this)
        if (not self.justBounced) and (not other.justBounced):
            self.justBounced = True
            other.justBounced = True
            sx1 =  (self.x[1] * (self.mass - other.mass) + (2 * other.mass * other.x[1])) / (self.mass + other.mass)
            sy1 =  (self.y[1] * (self.mass - other.mass) + (2 * other.mass * other.y[1])) / (self.mass + other.mass)
            ox1 = (other.x[1] * (other.mass - self.mass) + (2 * self.mass * self.x[1])) / (self.mass + other.mass)
            oy1 = (other.y[1] * (other.mass - self.mass) + (2 * self.mass * self.y[1])) / (self.mass + other.mass)
            self.x[1] = sx1
            self.y[1] = sy1
            other.x[1] = ox1
            other.y[1] = oy1
        if self.justBounced and other.justBounced:
            print("not this time!")            
        return

    def borderBounce(self, dimensions):
        if ( self.x[0] - self.radius <= 0 ) or ( self.x[0] + self.radius >= dimensions[1]) :
            if (self.x[1] < 0):#left border colission
                self.x[1] = abs(self.x[1]) + 10
            elif (self.x[1] > 0) and (self.x[0] + self.radius > dimensions[1]):#right border colission
                self.x[1] = -abs(self.x[1])
        if (self.y[0] - self.radius <= 0) or (self.y[0] + self.radius >= dimensions[0]):
            if (self.y[1] < 0):#top border colission            
                self.y[1] = abs(self.y[1])
            elif (self.y[1] > 0) and (self.y[0] - self.radius > 0):#bottom border collision
                self.y[1] = -abs(self.y[1])
        return
        
    def collisionIsNear(self, other):
        #check for overlaps before calculating for d, which is more efficient than the depricated collision  
        if((self.x[0] + self.radius + other.radius) > other.x[0]) and (self.x[0] < (other.x[0] + self.radius + other.radius)) and ((self.y[0] + self.radius + other.radius) > other.y[0]) and (self.y[0] < (other.y[0] + self.radius + other.radius)):
            x1, y1 = self.getPos()
            x2, y2 = other.getPos()
            #a*a is faster than a**2 in python. I looked for a carmack-y solution to make this faster but none exist (yet)
            d = ((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))**(1/2)
            #if the distance between the center of the two circles is less than or e
            #equal to their radius combined, then a collision has ocurred!
            #may have to pad this incase things start moving faster. Check here if circles are moving closer than I want to allow them.
            if d <= self.radius + other.radius:
                self.bounce2(other)
                return True
            else:
                return False            
        else:
            self.justBounced = False
            other.justBounced = False
            return 0
        
    def blackHole(position, allCircles):
        return 0
        """ 
        In Progress
        for c in allCircles:
            #if within a 300 px of the click
             k = c.getPos()
             if (abs(k[0] - position[0]) < 300) and (abs(k[1 - position[0]]) < 300):
                 #use pythagoreans theorem to calculate the new velocities
             
            #pull the circles to the click
             
             """