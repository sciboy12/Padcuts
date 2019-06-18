import padcuts as pc
#from time import sleep, time, clock
from evdev import ecodes, events, UInput, InputDevice, list_devices
import numpy as np
interp = np.interp
import re
from Xlib.display import Display
from Xlib.ext.xtest import fake_input
#import timeit
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
            #print(device.name)
            if bool(re.search('Touchpad', device.name)) == True:
                    #print(device.path)
                    touchpad = InputDevice(device.path)
                    #pad = InputDevice(device)
                    #return touchpad
                    #print('test')
            if bool(re.search('TouchPad', device.name)) == True:
                    touchpad = InputDevice(device.path)
                    #pad = InputDevice(device)
                    #print(touchpad)
                    return touchpad
                    
    capabilities=device.capabilities(verbose=True)
    abs_info=capabilities.get(('EV_ABS', 3))
    abs_x=dict(abs_info[0:1])
    abs_y=dict(abs_info[1:2])
    return touchpad
    #print(device)
    # Set touchpad path
    #device=touchpad



def detect_capabilities(device):


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
    return abs_x.min, abs_x.max, abs_y.min, abs_y.max
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
    return grid

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


def get_value(pad):
    if not 'pressure' in locals():
        pressure = 0
        
    event = pad.read_one()
    #print(event)
    if event != None:
        if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X:
            valtype = 'x'
            value = event.value
            return valtype, value
        if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_MT_POSITION_X:
            valtype = 'mt_x'
            value = event.value
            return valtype, value
        
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_PRESSURE:
            valtype = 'p'
            value = event.value
        else:
            valtype = 'p'
            value = None
        return valtype, value

def check_position(value, section, section_count, limit_min, limit_max):

    if value != None:

        value = interp(value,[limit_min,limit_max],[0,section_count])

        if section - 1 <= value <= (section):

            return section

def check_position_cycle(pad, value, pressure, threshold, axis, section_count, limit_min, limit_max):
    section = 1
    for x in range(0, section_count):
        result = check_position(value, section, section_count, limit_min, limit_max)
        if result != None and pressure >= threshold:
            result = str(result) + str(result)
            return (result)
        else:
            section = section + 1
    else:
        return None
