## physicsSimulator
A physics simiulator utilizing the pygame module to display the result of at most two colliding objects.
Handles up to 1600 circles with random mass, position, and velocity (on my machine).
The circles collide and bounce using elastic, incompressible, collision, in 0 gravity. I plan on including gravity as a global on/off. 

Main.py holds the library of the simulator. 
I plan on using this simulator to create a few games for fun.

###TODO:
re-implement the checkForCollisions function to be more readable. The function has to be O(n^2), but I should allow the user
to disable circle to circle collision for certain effects. This will allow performance improvements if the user doesnt care about circle 
to circle collision.



###Useful functions if you want to get started using my library:
####startup((int, int, int))
Input  (RGB)      : Color
Return Type Tuple : (clock, screen)
example: to initialize a screen with a black background -> clock, screen = startup((0,0,0))

###Use clock.tick to set a constant framerate 
from pygame: 
clock.tick(framerate)
msElapsed = clock.tick(60)

###Call updateRedraw on each frame. 
Input       : screen, list of objects to update, the time (clock.tick(60), I call it msElapsed)
returns     : nothing
result      : overwrites the screen in black



updateRedraw(screen, list, time)
updateRedraw(screen, circleArray, msElapsed)

###circle creation
####current version makes mass 100 until I need to make use of different mass circles
circle(radius, color)
