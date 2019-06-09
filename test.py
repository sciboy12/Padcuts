import padcuts as pc
from time import sleep
from evdev import ecodes, events, UInput, InputDevice, list_devices
import numpy as np
import re
from Xlib.display import Display
from Xlib.ext.xtest import fake_input
d = Display()

touchpad_x_min = 1266
touchpad_x_max = 5676

touchpad_y_min = 1062
touchpad_y_max = 4690

grid_x = 4
grid_y = 1

'''
a = 1
if a == 1:
    global c
    c = 1/100*10000
print(c)
'''
 

grid_x = len(pc.get_count(pc.gen_array(grid_x)))
grid_y = len(pc.get_count(pc.gen_array(grid_y)))

#rows = rows[1]
#cols = cols[2]
pad = pc.detect_touchpad()
pad = InputDevice(pad)
#print(grid_x)
#print(grid_y)


#print(grid_y)
#section_count_x = grid[3]
#section_count_y = grid[4]
#print(section_count_rows)
#device = pad
#device = 'dev/input/event0"'

#print(device)
#grid_y = tg.gen_grid(touchpad_x_min, touchpad_x_max, touchpad_y_min, touchpad_y_max, cols)

#n = 0
axis = 'x'
#section = 2
#pad.grab()
while True:
    value = pc.get_value(pad, 'x')
    #print(value)
    if value != None:
        print(value)
        #print(value)
        result = pc.check_position_cycle(pad, value, axis, grid_x, touchpad_x_min, touchpad_x_max)
        #result = pc.check_position(pad, value, axis, grid_x, touchpad_x_min, touchpad_x_max)
        print(result)

    #else:
        
    #if result != None:
        #print(result)
    #value = result[1]
    #result = result[2]
    
    #sleep(0.05)
    #print(value)

    #print(result)
    #n = n + 
    #print(result)
    #print(n)
