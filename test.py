import padcuts as pc
from time import sleep

touchpad_x_min = 1266
touchpad_x_max = 5676

touchpad_y_min = 1062
touchpad_y_max = 4690

rows = 5
cols = 1

'''
a = 1
if a == 1:
    global c
    c = 1/100*10000
print(c)
'''
 

grid = pc.gen_grid(rows, cols)
pad = pc.detect_touchpad()
#device = pad
#device = 'dev/input/event0"'

#print(device)
#grid_y = tg.gen_grid(touchpad_x_min, touchpad_x_max, touchpad_y_min, touchpad_y_max, cols)

n = 1
axis = 'x'
section = 3
while True:
    
    result = pc.check_position(pad, grid[1], axis, section, touchpad_x_min, touchpad_x_max)
    sleep(0.05)
    
    #n = n + 
    #print(result)
    #print(n)
