Brief Description:
----------------------------------------------------------------------
In this project the user keyboard input will be taken from the main.py file and will be sent to the Arduino (arduino.ino) using UART serial communication through a USB. The Arduino will then control 3 stepper motors. 
----------------------------------------------------------------------



Software:
----------------------------------------------------------------------
Operating System used: tested on Linux Ubunto 20.04.2 LTS and Ubuntu MATE (on the Raspberry pi 4) (Note: It should also work on Windows and MAC)

Programming language(s): Python 3.8.10 and c++ (Arduino 1.8.15)

Python Libraries: pynput version 1.7.3, pyserial (or serial) 3.5, and <Stepper.h> (Arduino)
----------------------------------------------------------------------

Instructions:
----------------------------------------------------------------------
sudo apt install python3-pip
pip install pynput
pip install pyserial
sudo chmod a+rw /dev/ttyACM0



----------------------------------------------------------------------




Parts:
----------------------------------------------------------------------
1-microprocessor (Raspberry pi 4)
2-microcontroller (Arduino MEGA)
3-stepper motors (one NEMA 23 and two NEMA 17)
4-stepper motor driver (DM542T)
5-h-bridges (two L298N)
6-USB cable type A/B
7-wireless keyboard (Rii i8+)
8-wires
----------------------------------------------------------------------