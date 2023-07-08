#Only for windows systems


import threading
import pygame

class Joystick(object):
    def __init__(self):
        ## Initializing ##
        self.throttle = 1500
        self.roll = 1500
        self.pitch = 1500
        self.yaw = 1500
        self.A = 0
        self.B = 0

        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() > 0:
            # Get the first joystick
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            # Make sure your joystick is connected

            # Get the number of axes
            self.num_axes = self.joystick.get_numaxes()


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
        while True:
            # Process events
            # Print out the axis values and map them accordingly, change the index of the axes list
            # JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION 
            # These are the events taken by pygame, add another conditional statement for accessing button values. 
            # Example: elif event.type == pygame.JOYBUTTONDOWN: 
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    # Read the axes values
                    axes = [self.joystick.get_axis(i) for i in range(self.num_axes)]
                    # print("Axes:", axes[5])
                    self.throttle = self.scale(axes[0], 1, -1, 2000, 1000, True)
                    self.yaw = self.scale(axes[1], 1, -1, 2000, 1000)
                    self.pitch = self.scale(axes[3], 1, -1, 2000, 1000)
                    self.roll = self.scale(axes[6], 1, -1, 2000, 1000)
                    self.A = axes[5]

#Uncomment these lines and run this file before running the test file to make sure you are getting correct joystick values
# if __name__ == "__main__":
    # joy = Joystick()
    # while True:
    #     print(joy.main())
