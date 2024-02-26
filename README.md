
# PLUTO PYTHON WRAPPER

Pluto can be operated using Python for various tasks. Python is a versatile programming language known for its simplicity and readability.
This is a simple python wrapper for your Pluto Drone so that you can write your own python script to make your drone move around. You can create your own projects by using the predefined functions.

Go ahead and pull up the terminal and type: 
```bash
  git clone https://github.com/DronaAviation/Pluto_Drona_Python_Programming.git
```

## Basic Flight Controls/ Commands:
![image](https://github.com/csaail/PLUTO_PYTHON_WRAPPER/assets/87662482/0c2c1fd0-8676-4b9c-ab87-48ce3d7c87af)
Pitch => Forward/Back.<br/> Roll => Left/right.<br/>  Yaw => Left/right rotation around the centre of the frame.<br/>  Throttle => Changed altitude/speed.


## Usage

The `drone.py` script provides a wrapper class for controlling the drone. To use the wrapper, follow the instructions below:

   ```python
   from drone import drone
   my_pluto = drone()

   Connect The drone:  my_pluto.connect() 

   my_pluto.trim(Roll, Pitch, Throttle, Yaw)

   Trim the drone:  my_pluto.trim(Roll, Pitch, Throttle, Yaw)
   #Example: my_pluto.trim(0, 0, 0, 0)
  
   Arm the drone:  my_pluto.arm()
   Disarm the drone:  my_pluto.disarm()

   Set throttle speed:  my_pluto.throttle_speed(value, Duration)
   #Example: my_pluto.throttle_speed(5, 1) # Increase throttle speed by 5 for 1 second

   Takeoff:  my_pluto.takeoff()
   Land the drone:  my_pluto.land()

  Roll, Pitch, Yaw:
  Functions like roll_speed, pitch_speed, and yaw_speed are available for controlling the drone's movements.
  my_pluto.roll_speed(50, 2)   # Increase roll speed by 50 for 2 sec
  my_pluto.pitch_speed(50, 2)  # Increase pitch speed by 50 for 2 sec
  my_pluto.yaw_speed(50, 2)    # Increase yaw speed by 50 for 2 sec
  ```
   

## Keyboard Controls:

To set up keyboard controls for your Pluto drone, follow these general steps:

1. Locate Keyboard Control Files:
   - Navigate to the appropriate directory based on your operating system:
     - For Windows users: Keyboard/windows
     - For Linux/Mac users: Keyboard/linux,mac

2. Run Keyboard Control Script:
   - Locate the keyboard.py file in the respective directory and run it.

### Specific Instructions:

#### For Windows Users:
- Navigate to the Keyboard/windows directory.
- Run the ```keyboard.py``` script.

#### For Linux/Mac Users:
- Navigate to the Keyboard/linux_mac directory.
- Run the ```keyboard.py``` script.

![W](https://github.com/DronaAviation/Pluto_Drona_Python_Programming/assets/16723168/0d2592a5-3f2b-4de1-8297-35a3505bb1ab)

## Joystick Controls Setup:

To set up joystick controls for your Pluto drone, follow these general steps:

1. Ensure Necessary Libraries:
   - Make sure you have the required libraries installed for your operating system.

2. Locate Joystick Control Files:
   - Navigate to the appropriate directory based on your operating system:
     - For Windows users: Joystick/windows
     - For Ubuntu (Linux) users: Joystick/linux
     - For macOS users: Joystick/mac

3. Run Joystick Control Script:
   - Locate the ```joystick.py``` file in the respective directory and run it.

### Specific Instructions:

#### For Windows Users:
- Ensure that you have the necessary libraries installed.
- Navigate to the Joystick/windows directory.
- Run the joystick.py script.

#### For Ubuntu (Linux) Users:
- Make sure you have the Evdev library installed on your system.
- Navigate to the Joystick/linux directory.
- Run the joystick.py script.

#### For macOS Users:
- Ensure that you have the Pygame library installed.
- Navigate to the Joystick/mac directory.
- Run the joystick.py script.

Currently the default settings are: (Note: you can change them according to your need)
![joystick](https://github.com/csaail/PLUTO_PYTHON_WRAPPER/assets/87662482/17bdba11-c7b0-4a49-a892-8efce235e57e)
![joystick tp](https://github.com/csaail/PLUTO_PYTHON_WRAPPER/assets/87662482/79608307-4590-41d0-8d1b-ab737c30b94a)

## Voice Controlled Drone

We've developed a script that enables you to control your Pluto drone using your voice!

1. **Download Pre-trained Voice Model:**
   - Visit [Vosk Models](https://alphacephei.com/vosk/models) to download a pre-trained voice model.
   - Recommended models: `vosk-model-small-en-us-0.15` or `vosk-model-en-in-0.5`.

2. **Configure Voice Command Script:**
   - Copy the path where you've stored your downloaded model.
   - Paste the path into the `voice_cmd.py` file located in the "voice" folder.

3. **Run Voice Command Script:**
   - Navigate to the "voice" folder.
   - Run the file:
     `
     voice_cmd.py
     `

Currently, the drone responds to the following voice commands:
- "hello" to arm the drone.
- "take off" to initiate takeoff.
- "land" to initiate landing.

Feel free to customize these commands according to your preferences.


## Structure of the Wrapper:
![image](https://github.com/csaail/PLUTO_PYTHON_WRAPPER/assets/87662482/927591e8-36cd-4f2d-ae88-0016fa9479c9)

## Frequently Faced Errors
