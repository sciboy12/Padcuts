import numpy as np
import re
from evdev import ecodes, events, UInput, InputDevice, list_devices
#import evdev

#from matplotlib import pyplot as plt
from Xlib.display import Display
from Xlib.ext.xtest import fake_input
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
                    #print('test')
            if bool(re.search('TouchPad', device.name)) == True:
                    touchpad = InputDevice(device.path)
    #print(device)
    # Set touchpad path
    device=touchpad

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
    return rows, cols
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

    rows = 1
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


def get_position(device, section_count, padorlimits):
    loop_count = 0
    while loop_count <= section_count:
        if axis == 'x':
            event = devicel.read_one()
            print(event)
            #for event in device.read_one():
            #print(event.type)
            if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X:
                print(value)
                print(True)
                value = np.interp(event.value,[x_min,x_max],[0,rows])
                #check_position(None, )
        #else:
            print('l')
            #return None
def check_position(device, grid, axis, section, limit_min, limit_max):
    section_count = len(grid)

    
    pad = InputDevice(device)
    value = get_position(pad, section_count)

    print(value)

    print(grid)

    if value != None:
        if section <= value <= section + 1:
            result = True   
        else:
            result = False


            #loop_count = loop_count + 1
            #return result
