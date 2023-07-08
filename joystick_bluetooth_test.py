from Pluto import pluto
import time
from joystick_bluetooth_linux import * #Currently it imports the linux version for bluetooth joystick

#For windows uncomment the line below
# from joystick_bluetooth_win import *

my_pluto = pluto()# This commands creates an object of pluto() where you can connect your hardware to. my_pluto is literally your plutodrone

joy = Joystick()

while True:
    [my_pluto.rcThrottle, my_pluto.rcYaw, my_pluto.rcPitch, my_pluto.rcRoll, A, B] = joy.main() 

    # print([my_pluto.rcThrottle, my_pluto.rcYaw, my_pluto.rcPitch, my_pluto.rcRoll, A, B])
    # You can change the way your drone arms and disarms by changing these conditonal statements
    if A and my_pluto.rcThrottle < 1050: 
        my_pluto.arm()
        # print("arming", A)
    elif A and my_pluto.rcPitch < 1050 and my_pluto.rcRoll < 1050:
        my_pluto.take_off()
        # print("taken off", B)
    elif B and my_pluto.rcThrottle < 1050 and my_pluto.rcYaw < 1050:
        my_pluto.land()
        my_pluto.disarm()
        # print("landing", B)
    elif B:
        my_pluto.disarm() 
        # print("disarming", B)
