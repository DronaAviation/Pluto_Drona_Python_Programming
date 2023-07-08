import joystick_usb
from Pluto import pluto

joy = joystick_usb.XboxController()

my_pluto = pluto()

def mapping(x, inMin, inMax, outMin, outMax): 
    x = (x - inMin) * (outMax - outMin) / (inMax - inMin) + outMin
    if (x < outMin):
      return int(outMin)
    elif (x > outMax):
      return int(outMax)
    else:
      return int(x)

while True:

    [x, y, a, b, A, B, X, Y, rb, lb] = joy.read()

    my_pluto.rcThrottle = mapping(y, -1, 1, 1000, 2000)    
    my_pluto.rcYaw = mapping(x, -1, 1, 1000, 2000)
    my_pluto.rcPitch = mapping(b, -1, 1, 1000, 2000)
    my_pluto.rcRoll = mapping(a, -1, 1, 1000, 2000)
    
    if A: 
        my_pluto.arm()
        # time.sleep(0.5)
        # print("arming", A)
    elif B:
        my_pluto.disarm() 
        # print("disarming", B)
    elif X:
        my_pluto.take_off()
        # time.sleep(0.5)
        # print("taken off", X)
    elif Y:
        my_pluto.land()
        my_pluto.disarm()
        # print("landing", Y)