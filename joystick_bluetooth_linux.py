#Only for linux systems


import evdev
import threading

class Joystick(object):
    def __init__(self):
        ## Initializing ##
        self.throttle = 1500
        self.roll = 1500
        self.pitch = 1500
        self.yaw = 1500
        self.A = 0
        self.B = 0

        print("Finding controller...")
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        #Print our the devices list, if you don't find your device check your connection
        #Also make sure you only have one device connected
        esp_gamepad = devices[0].path

        self.gamepad = evdev.InputDevice(esp_gamepad)

        self._monitor_thread = threading.Thread(target=self.read_values, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def main(self):
        return self.throttle, self.yaw, self.pitch, self.roll, self.A, self.B

    def scale(self, value, rangeMax, rangeMin, outMax, outMin, invert=False):
        # Check if the value is within the input range
        if value < rangeMin:
            value = rangeMin
        elif value > rangeMax:
            value = rangeMax

        # Calculate the input range and output range spans
        inSpan = rangeMax - rangeMin
        outSpan = outMax - outMin

        # Convert the input value to a proportion within the input range
        scaledValue = float(value - rangeMin) / inSpan

        # Scale the proportion to the output range
        scaledValue = scaledValue * outSpan + outMin

        # Clamp the scaled value within the output range
        if scaledValue > outMax:
            scaledValue = outMax
        elif scaledValue < outMin:
            scaledValue = outMin

        # Invert the scaled value if specified
        if invert:
            scaledValue = outMax + outMin - scaledValue

        return int(scaledValue)

    def read_values(self):
        #If the values aren't changing according to your joystick movement print out the evdev.ecodes
        #For example your joystick won't have ABS_X and ABS_Y axes and may be mapped to some other axes
        #Download jstest-gtk package on ubuntu and check out your joystick mapping
        #Also check out the values by clicking on caliberation and change them in the call for the scale function
        try:
            for event in self.gamepad.read_loop():
                
                if event.type == evdev.ecodes.EV_ABS:
                    # Handle joystick or analog stick events
                    if event.code == evdev.ecodes.ABS_X:
                        self.throttle = self.scale(event.value, 27165, 1464, 2000, 1000, True)
                    elif event.code == evdev.ecodes.ABS_Y:
                        self.yaw = self.scale(event.value, 32335, 4219, 2000, 1000)
                    elif event.code == evdev.ecodes.ABS_RY:
                        self.A = self.scale(event.value, 32767, 16384, 1, 0)
                    elif event.code == evdev.ecodes.ABS_RZ:
                        self.B = self.scale(event.value, 32767, 16384, 1, 0, True)
                    elif event.code == evdev.ecodes.ABS_Z:
                        self.roll = self.scale(event.value, 29510, 500, 2000, 1000, True)
                    elif event.code == evdev.ecodes.ABS_RX:
                        self.pitch = self.scale(event.value, 31711, 4080, 2000, 1000)
        except BlockingIOError:
            pass

#Uncomment these lines and run this file before running the test file to make sure you are getting correct joystick values
# if __name__ == "__main__":
#     joy = Joystick()
#     while True:
#         print(joy.main())
