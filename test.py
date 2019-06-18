# Example code
import padcuts as pc
from time import sleep
from evdev import ecodes, events, UInput, InputDevice, list_devices
import numpy as np
import re
from Xlib.display import Display
from Xlib.ext.xtest import fake_input
from subprocess import call
d = Display()

#touchpad_x_min = 1266
#touchpad_x_max = 5676

#touchpad_y_min = 1062
#touchpad_y_max = 4690



# Key config
key_katsu_l = 'e'
key_katsu_r = 'r'
key_don_l = 'u'
key_don_r = 'i'



# Pressure threshold to trigger keypress
threshold = 30

# Grid settings
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
#print(grid_x)
grid_y = len(pc.get_count(pc.gen_array(grid_y)))
pad = pc.detect_touchpad()
capabilities = pc.detect_capabilities(pad)
print(capabilities)
touchpad_x_min = capabilities[0]
touchpad_x_max = capabilities[1]
axis = 'x'
key1 = False
key2 = False
key3 = False
key4 = False
keydown = False
pad.grab()
while True:
    value = pc.get_value(pad)
   

    if value != None:
        if value[0]  == 'x' and value[1] != None:
            x = value[1]
            x_set = True
        elif not 'x_set' in locals():
            x = 0
            
        if value[0]  == 'p' and value[1] != None:
            p = value[1]
            p_set = True
        elif not 'p_set' in locals():
            p = 0

        result = pc.check_position_cycle(pad, x, p, threshold, axis, grid_x, touchpad_x_min, touchpad_x_max)
        #print(result)
        print(result)
        #if result != None:
            #print(result)

        # End of example code and start of TaikoPad

        
        
        # Key down statments
        #while result != False:
        if keydown == False:
            if result == 1:
                call(['xdotool', 'key', key_katsu_l])
                keydown = True
                
            elif result == 2:
                call(['xdotool', 'key', key_katsu_r])
                keydown = True

            elif result == 3:
                call(['xdotool', 'key', key_don_l])
                keydown = True

            elif result == 4:
                call(['xdotool', 'key', key_don_r])
                keydown = True
        elif result == None:
            keydown = False

        
        '''
        if key1 or key2 or key3 or key4 == False:
            if result == 1:
                call(['xdotool', 'keydown', key_katsu_l])
                key1 = True
                
            elif result == 2:
                call(['xdotool', 'keydown', key_katsu_r])
                key2 = True

            elif result == 3:
                call(['xdotool', 'keydown', key_don_l])
                key3 = True

            elif result == 4:
                call(['xdotool', 'keydown', key_don_r])
                key4 = True
        elif key1 or key2 or key3 or key4 == True:

            if result == None:
                call(['xdotool', 'keyup', key_katsu_l])
                key1 = False
                
            elif result == None:
                call(['xdotool', 'keyup', key_katsu_r])
                key1 = False

            elif result == None:
                call(['xdotool', 'keyup', key_don_l])
                key1 = False
                
            elif result == None:
                call(['xdotool', 'keyup', key_don_r])
                key1 = False
        '''
        

            
        #elif result == None:
         #   call(['xdotool', 'keyup',  key_katsu_l, key_katsu_r, key_don_l, key_don_r])
          #  keydown = False
