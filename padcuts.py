import padcuts as pc
from time import sleep, time, clock
from evdev import ecodes, events, UInput, InputDevice, list_devices
import numpy as np
interp = np.interp
import re
from Xlib.display import Display
from Xlib.ext.xtest import fake_input
import timeit
d = Display()

'''
def detect_touchpad():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    
    for device in devices:
            #global touchpad
            if bool(re.search('Touchpad', device.name)) == True:
                    #print(evdev.InputDevice(device.path))
                    touchpad = evdev.InputDevice(device.path)
                    capabilities=device.capabilities(verbose=True)
                    abs_info=capabilities.get(('EV_ABS', 3))
                    abs_x=dict(abs_info[0:1])
                    abs_y=dict(abs_info[1:2])
                    return touchpad, abs_x, abs_y

            if bool(re.search('TouchPad', device.name)) == True:
                    #print(evdev.InputDevice(device.path))
                    touchpad = evdev.InputDevice(device.path)
                    #print(touchpad)
                    capabilities=device.capabilities(verbose=True)
                    abs_info=capabilities.get(('EV_ABS', 3))
                    abs_x=dict(abs_info[0:1])
                    abs_y=dict(abs_info[1:2])

                    return touchpad, abs_x, abs_y
'''

def detect_touchpad():

    # Detect touchpad
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
            if bool(re.search('Touchpad', device.name)) == True:
                    #print(device.path)
                    touchpad = InputDevice(device.path)
                    pad = InputDevice(device)
                    return touchpad
                    #print('test')
            if bool(re.search('TouchPad', device.name)) == True:
                    touchpad = InputDevice(device.path)
                    pad = InputDevice(device)
                    return pad
    #print(device)
    # Set touchpad path
    #device=touchpad



def detect_capabilities():


    # Detect min and max touchpad values
    capabilities=device.capabilities(verbose=True)
    abs_info=capabilities.get(('EV_ABS', 3))
    abs_x=dict(abs_info[0:1])
    abs_y=dict(abs_info[1:2])

    abs_x=abs_x.get(('ABS_X', 0))
    abs_y=abs_y.get(('ABS_Y', 1))

    # Set min and max touchpad values
    x_min=abs_x.min
    x_max=abs_x.max
    y_min=abs_y.min
    y_max=abs_y.max
    return touchpad, abs_x.min, abs_x.max, abs_y.min, abs_y.max
'''
def detect_touchpad():
# Detect touchpad


    # Set touchpad path
    device = detect_touchpad_path()
    #print(device)
    print(device)
    # Detect min and max touchpad values
    #capabilities=device.capabilities(verbose=True)
    #abs_info=capabilities.get(('EV_ABS', 3))
    #abs_x=dict(abs_info[0:1])
    #abs_y=dict(abs_info[1:2])

#    abs_x=abs_x.get(('ABS_X', 0))
 #   abs_y=abs_y.get(('ABS_Y', 1))


    return device, abs_x.min, abs_x.max, abs_y.min, abs_y.max
'''
def gen_grid(rows, cols):
    rows = gen_array(rows)
    cols = gen_array(cols)
    grid = (rows, cols)
    #section_count_rows = len(rows)
    #section_count_cols = len(cols)
    return grid

#def get_rows(n):

#def get_cols(n):

def get_count(n):
    count = len(n)
    return n
def gen_array(n):
    '''
    #b = int(np.cos(10)*-5)
    #b = rows * 3
    a = 4
    b = 25/100
    c = b * 3 * 100
    print(b)
    print(c)
    d = np.arange(x_min,x_max,c)
    print(d)
    print()
    #a1 = np.tile(a, (7,1))
    #print(a1)
    #np.dstack((a1, a1.T)).reshape(-1, 2)
    '''

    #rows = 1
    grid = []
    for i in range(n):
        grid.append([])
        #for j in range(cols):
         #   grid[i].append(0)
    return(grid)


#def gen_zones():
    
#def check():



#def in_range():
#    check_pos():

        
def parse_grid(value, grid, quadrant_x_min, quadrant_x_max):
    
    loop = True
    #section = 0
    
    while loop == True:
            
        section = grid[0 + 1]
        
        #print(section)

def click_mouse(button, release_delay):
    fake_input(d, X.ButtonPress, button)
    d.sync()
    sleep(release_delay)
    fake_input(d, X.ButtonRelease, button)
    d.sync()

# For testing purposes
#device = detect_touchpad()
#print(device)


def get_value(pad, axis):
    loop_count = 0
    #while loop_count <= section_count:
        #if axis == 'x':
    event = pad.read_one()
    if event != None:
        global value
        global touch
    #if event != None and axis == 'x' and event.code == ecodes.ABS_X:
        #if axis == 'x' and event.code == ecodes.ABS_X:

        #if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X:
            
        if event.code == ecodes.ABS_X:
            #print(value)
            #print(True)
            #check_position(None, )
            
            value = event.value
            #print(event.value)
            
        else:
            value = None
            
        #if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_PRESSURE:
        if event.code == ecodes.ABS_PRESSURE:


            pressure = event.value
        else:
            return None
        return value, pressure
#    else:
 #       return None

def check_position(value, section, section_count, limit_min, limit_max):

    
    #pad = InputDevice(pad)
    #value = get_position(pad, axis)
    #value = np.interp(raw_value,[limit_min,limit_max],[0,section_count])
    #print(value)

    #print(grid)

    if value[0] != None:
        #start = time()
        value = interp(value[0],[limit_min,limit_max],[0,section_count])
        
        #print(time() - start)

        #print(value)    
        #print(value)
        if section - 1 <= value <= section:
        
        #if value <= section:
            #result = True
            return value
    #if 
    else:
        #result = False
        return False
        #section = section + 1
        #check()
    
    
    

            #loop_count = loop_count + 1
            


def check_position_cycle(pad, value, axis, section_count, limit_min, limit_max):
    
    
    #section = 2
    #loop = True 
    #while True:
    section = 0
    for x in range(0, section_count):
        #if value[1] != None:
        #start = time()
        result = check_position(value, section, section_count, limit_min, limit_max)
        #print(start - time())
        if result == True:
            return result
        else:
            section = section + 1
            print(section)
            #return
            
            #if section >= section_count:
            #    loop = False
            #    return section
            #else:
            #    return None
            #else:
            #    return
        #elif value == None:
        #    button = None
        #    loop  = False
        #    return None

        

