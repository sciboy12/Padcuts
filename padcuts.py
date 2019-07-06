import padcuts as pc
from time import sleep, time, clock
from evdev import ecodes, events, UInput, InputDevice, list_devices
import numpy as np
interp = np.interp
import re
from Xlib.display import Display
from Xlib.ext.xtest import fake_input
d = Display()

def detect_touchpad():

    # Detect touchpad
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
            if bool(re.search('Touchpad', device.name)) == True:
                    print(device.path)
                    touchpad = InputDevice(device.path)
                    return touchpad
                
            if bool(re.search('TouchPad', device.name)) == True:
                    print(device.path)
                    touchpad = InputDevice(device.path)
                    return touchpad

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

# Generates the grid to be used for the button array
# Each square within the grid corresponds to a button
# There are two 1D arrays, one for each axis
def gen_grid(rows, cols):
    rows = gen_array(rows)
    cols = gen_array(cols)
    grid = (rows, cols)
    return grid

def get_count(n):
    # Get the total rows or columns for an axis
    count = len(n)
    return n

def gen_array(n):
    # Generates the array for an axis
    #rows = 1
    grid = []
    for i in range(n):
        grid.append([])
        # Extends the array downward into 2D
        # This may not be needed depending on how the Y axis will be implemented
        #for j in range(cols):
         #   grid[i].append(0)
    return(grid)

# Not used yet
def click_mouse(button, release_delay):
    #Press the button
    fake_input(d, X.ButtonPress, button)
    d.sync()
    sleep(release_delay)
    #Release the button
    fake_input(d, X.ButtonRelease, button)
    d.sync()

# For testing purposes
#device = detect_touchpad()
#print(device)

# Returns aboslute X from the touchpad
# Also returns the pressure for touch detection, multitouch coordinates and slot
# Y axis not implemented yet as the rest of the code can't properly handle it in conjunction with the X axis yet
def get_value(pad):
    if not 'pressure' in locals():
        pressure = 0
    # Get the most recent event
    event = pad.read_one()
    #print(event)
    if event != None:
        
        # Get X axis
        if event.type == ecodes.EV_ABS and event.code == ecodes.ABS_X:
            valtype = 'x'
            #value = event.value
            return valtype, event.value
        
        # Get multitouch X axis
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_MT_POSITION_X:
            valtype = 'mt_x'
            #value = event.value
            return valtype, event.value
        
        # Get pressure
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_PRESSURE:
            valtype = 'p'
            #value = event.value
            return valtype, event.value

        # Get slot
        elif event.type == ecodes.EV_ABS and event.code == ecodes.ABS_MT_SLOT:
            valtype = 'mt_s'
            #slot_id = event.value
            return valtype, event.value


def check_position(value, section, section_count, limit_min, limit_max):
    if value != None:
        
        # Map the value to the total number of columns or rows
        value = interp(value,[limit_min,limit_max],[0,section_count])
        
        # Check if value is within range of section to section - 1 (which is the range corresonding to a single button)
        if section - 1 <= value <= (section):
            # If so, return it as the button being pressed
            return section

# Loop over running check_position() and checking the value
def check_position_loop(pad, value, pressure, threshold, axis, section_count, limit_min, limit_max):
    # Placeholder to prevent error
    section = 1
    
    # Loop, with the number of loops being equal to section_count
    for x in range(0, section_count):
        
        # Map the value to section_count as the resulting value
        result = check_position(value, section, section_count, limit_min, limit_max)
        
        # Return result only if pressure passes the threshold
        if result != None and pressure >= threshold:
            return (result)
        
        # Otherwise, move on to check if result is within the next square
        else:
            section = section + 1
            
    #else:
        #return None
