import os
import sys
import keyboard_control

#####################################################
# Key Controls
# spacebar : arm or disarm
# w : increase height
# s : decrease height
# q : take off
# e : land
# a : yaw left
# d : yaw right
# n: To enter developer mode
# Up arrow : go forward
# Down arrow : go backward
# Left arrow : go left
# Right arrow : go right
# e: to quit
#####################################################

if os.name == 'nt':  # Windows
    import msvcrt

    def getKey():
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\xe0':  # Check for arrow key
                key = msvcrt.getch()
                if key == b'H':
                    return '[A'             
                elif key == b'P':
                    return '[B'  # Down arrow
                elif key == b'K':
                    return '[D'  # Left arrow
                elif key == b'M':
                    return '[C'  # Right arrow
                # else:
                #     return ''
            elif key == b'\x1b':  # Handle escape key
                return key.decode('ascii')
            else:
                return key.decode('ascii')
        # else:
        #     return ''

else:  # Unix-based systems (Linux, macOS, etc.)
    import tty
    import termios
    import select

    def getKey():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
            if rlist:
                key = sys.stdin.read(1)
                if key == '\x1b':
                    # Handle escape sequences if necessary
                    key += sys.stdin.read(2)
            else:
                key = ''
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return key



keyboard={  #dictionary containing the key pressed and value associated with it
                      '[A': 10,
                      '[D': 30,
                      '[C': 40,
                      'w':50,
                      's':60,
                      ' ': 70,
                      'r':80,
                      't':90,
                      'p':100,
                      '[B':110,
                      'n':120,
                      'q':130,
                      'e':140,
                      'a':150,
                      'd':160,
                      '+' : 15,
                      '1' : 25,
                      '2' : 30,
                      '3' : 35,
                      '4' : 45}

while True:
    key = getKey()
    # print(key) 
    if key == 'e':
        print("stopping")
        break
    if key in keyboard.keys():
        msg = keyboard[key]
        keyboard_control.identify_key(msg)
    else:
        msg = 80    
        keyboard_control.identify_key(msg)
