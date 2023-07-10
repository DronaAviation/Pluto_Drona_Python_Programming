
# Pluto Python Wrapper

This is a simple python wrapper for your Pluto Drone so that you can write your own python script to make your drone move around. You can create your own projects by using the predefined functions.

Go ahead and pull up the terminal and type: 
```bash
  git clone https://github.com/MalayPhadke/Pluto_Python_Wrapper
```


## Usage

The Pluto.py has the class with which we need to create drone Object. Look into the example script and replicate the same. The script arms the drone and keeps it spinning for 5 seconds before disarming.

In the script, my_pluto is the object created. Assuming that the name of the object created is my_pluto, follow the lines below for using the wrapper.

```python
To arm : my_pluto.arm()

To disarm : my_pluto.disarm()

To Takeoff : my_pluto.take_off()

To land : my_pluto.land()

To move the drone forward() : my_pluto.forward()

To move the drone backward() : my_pluto.backward()

To move the drone left : my_pluto.left()

To move the drone right : my_pluto.right()

To rotate the drone right : my_pluto.right_yaw()

To rotate the drone left : my_pluto.left_yaw()
```
ENSURE YOU WRITE ALL THE PYTHON FILES IN THE SAME DIRECTORY WHERE plutoMultiwii and Pluto SCRIPTS ARE PRESENT

YOU WILL NOT NEED PLUTO_WRAPPER DIRECTORY displayed here. You will only need Pluto.py and plutoMultiwii.py

They other python script are also created to control your drone with a keyboard or a joystick.


## Installation
To run the keyboard and joystick scripts go ahead and pull the the required modules by opening up your terminal and type:

```bash
 pip install -r requirements.txt
```
    
## Joystick Control

I have created two different scripts for getting
joystick values for linux and windows namely joystick_bluetooth_linux.py and joystick_bluetooth_win.py so make sure you use them according to your OS.

To test your joystick inputs follow the instructions in joystick_bluetooth or joystick_usb scripts. Make sure to map your joystick properly.

To control your drone after checking your joystick run:

```bash
python joystick_usb_test.py 
``` 
or 
```bash
python joystick_bluetooth_test.py 
```

Currently the default settings are: 

For bluetooth and usb joystick:

![Bluetooth Joystick Control](https://helpdeskgeek.com/wp-content/pictures/2020/12/5.-Mode-2.jpg)

For bluetooth joystick:

To arm the drone: Press A and move throttle down

To disarm the drone: Press B 

To takeoff: Press A and move Pitch and Roll to lowest values

To land: Press B and move Throttle and Yaw to lowest values

For usb joystick:

To arm the drone: Press A 

To disarm the drone: Press B 

To takeoff: Press X

To land: Press Y

## Keyboard Control

The keyboard_control.py scripts is used for mapping the drone commands to keys pressed. To control your drone with your Keyboard run the following command in your terminal:

```bash
python keyboard_test.py 
```

It uses following keys to control drone:

    spacebar : arm or disarm
    w : increase height
    s : decrease height
    q : take off
    e : land
    a : yaw left
    d : yaw right
    n: To enter developer mode
    Up arrow : go forward
    Down arrow : go backward
    Left arrow : go left
    Right arrow : go right
    Ctrl-C: to quit




## Receive Data 

You can receive the following data from the drone by running the command

```bash
python plutoReceiveData.py
```

Make sure the drone is connected to your laptop by running the keyboard or joystick test script.

Data Received:

```
GyroX GyroY GyroZ
AccX  AccY  AccZ
MagX  MagY  MagZ
Roll  Pitch Yaw
Altitude  Battery
Signal Strength(RSSI)
Throttle Pitch Roll Yaw
RCAux1 RCAux2 RCAux3 RCAux4
```




## Voice Controlled Drone

Yes, we have created a script to control your pluto with your voice!

Firstly, go ahead and download a vosk pre trained voice model to recognize your voice.

https://alphacephei.com/vosk/models

I suggest you download either the vosk-model-small-en-us-0.15 or vosk-model-en-in-0.5.

Copy the path where you have downloaded your model and paste it in the voice_cmd.py file and now run:
```bash
python voice_cmd.py 
```

Currently, the drone will arm when you speak 'hello'.
It will take off on 'take off' and land on 'land'.
Feel free to change it as you want.

## Frequently Faced Errors

