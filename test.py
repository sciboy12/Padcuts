import padcuts as pc
from time import sleep
from Xlib.display import Display
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
#print(capabilities)
touchpad_x_min = capabilities[0]
touchpad_x_max = capabilities[1]

# Axis to use
# Note that the Y axis is not yet implemented in Padcuts
axis = 'x'

keydown1 = False
keydown2 = False
keydown3 = False
keydown4 = False

keydown1alt = False
keydown2alt = False
keydown3alt = False
keydown4alt = False

keydown = False


#pad.grab()
while True:
    # Get touchpad values
    value = pc.get_value(pad)
   
    # Set values to 0 if they do not exist yet
    # This is to get the code to start without a NameError
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

        if value[0]  == 'mt_s' and value[1] != None:
            s = value[1]
            s_set = True
        elif not 'mt_s_set' in locals():
            s = 0
        
        result = pc.check_position_loop(pad, x, p, threshold, axis, grid_x, touchpad_x_min, touchpad_x_max)

        # End of example code and start of Taiko code
        # This will not work fully until multitouch is properly implemented

        # Key down statments
        if result == 1 and keydown1 == False and s == 0:
            call(['xdotool', 'keydown', key_katsu_l])
            keydown1 = True
            
        elif result == 2 and keydown2 == False and s == 0:
            call(['xdotool', 'keydown', key_katsu_r])
            keydown2 = True

        elif result == 3 and keydown3 == False and s == 0:
            call(['xdotool', 'keydown', key_don_l])
            keydown3 = True

        elif result == 4 and keydown4 == False and s == 0:
            call(['xdotool', 'keydown', key_don_r])

        #############################################################
        
        elif result == 1 and keydown2alt == False and s == 1:
            call(['xdotool', 'keydown', key_katsu_r])
            keydown2alt = True

        elif result == 2 and keydown1alt == False and s == 1:
            call(['xdotool', 'keydown', key_katsu_l])
            keydown1alt = True

        elif result == 3 and keydown4alt == False and s == 1:
            call(['xdotool', 'keydown', key_don_r])
            keydown4alt = True

        elif result == 4 and keydown3alt == False and s == 1:
            call(['xdotool', 'keydown', key_don_l])
            keydown3alt = True

        # Key up statments
        elif result == None:
            call(['xdotool', 'keyup', key_katsu_l])
            call(['xdotool', 'keyup', key_katsu_r])
            call(['xdotool', 'keyup', key_don_l])
            call(['xdotool', 'keyup', key_don_r])
            keydown1 = False
            keydown2 = False
            keydown3 = False
            keydown4 = False
            keydown1alt = False
            keydown2alt = False
            keydown3alt = False
            keydown4alt = False

        elif result == None and s == 1:
            call(['xdotool', 'keyup', key_katsu_l])
            call(['xdotool', 'keyup', key_katsu_r])
            call(['xdotool', 'keyup', key_don_l])
            call(['xdotool', 'keyup', key_don_r])
            keydown1alt = False
            keydown2alt = False
            keydown3alt = False
            keydown4alt = False

        # Old code, kept for reference
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
            # More old code
            #elif result == None:
                #call(['xdotool', 'keyup',  key_katsu_l, key_katsu_r, key_don_l, key_don_r])
                #keydown = False
