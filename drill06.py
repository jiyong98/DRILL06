
import math
from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
x = 300
y = 90
firstrun = True
firstrun2 = True
secondrun = False
threerun = False
fourrun = False
fiverun = False
run = True
run2 = True
d = 200
posx = 0
posy = 0
rx = 0

while run:
    while firstrun:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x , y)
        x = x + 2
            
        if x >= 750:
            firstrun = False
            secondrun = True
        
        delay(0.001)
    while secondrun:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x ,  y)
        y = y + 2
        if y >= 550:
            secondrun = False
            threerun= True
        
        delay(0.001)
    while threerun:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x , y)
        x = x - 2
        if x <= 50:
            threerun = False
            fourrun= True
        
        delay(0.001)
    while fourrun:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        if y <= 90:
            fourrun = False
            firstrun2 = True   
            
            
        delay(0.001)
    while firstrun2:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(x , y)
        x = x + 2  
        if x >= 300:
            firstrun2 = False
            fiverun = True   
            x = 50
            y = 90
        delay(0.001)
    while fiverun:
        clear_canvas()
        grass.draw_now(400, 30)
        character.draw_now(posx, posy )
        posx = x + 300 + math.cos(rx) * d
        posy = y + 200 + math.sin(rx) * d
        rx = rx + 0.005
        if rx >= 6.3:
            rx = 0
            fiverun = False
            firstrun = True
        

        
        
        
        



    



