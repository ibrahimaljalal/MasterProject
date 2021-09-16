Brief Description:
----------------------------------------------------------------------
This program will detect if there is an obstacle in a certain angle range and within a cretin distance. if there is an obstacle it will return True otherwise it will return False. just like most projects the starting point is at main.py file. Note that you could also get the exact distance of the obstacle (in mm) instead of True by a very small change in the code.
----------------------------------------------------------------------


Software:
----------------------------------------------------------------------
Operating System: tested on Linux Ubunto 20.04.2 LTS. Note: in Windows it works then an error occurs
Programming language(s): Python 3.8.10
Libraries: rplidar (version 0.9.5 )
----------------------------------------------------------------------


Instructions and Notes:
----------------------------------------------------------------------
sudo apt install python3 (for Linux if you don't have python) (Assuming you already have python on Windows)
sudo apt install python3-pip (for Linux if you have pip) (Assuming you already have pip on Windows)
pip install rplidar-roboticia (or pip3)
Make sure you change the value p["port] in main.py file to mach the port of the Lidar (for Windows it is com than a number for an example "com6" you can see the port in the device manager) (For Linux it is either /dev/ttyUSB then a number or /dev/ttyACM than a number for an example /dev/ttyUSB0 or dev/ttyACM0)
sudo chmod 666 /dev/ttyUSB0 (for Linux) (usually in my case it is ttyUSB0) (Note in winodws you do not need to use this command)
----------------------------------------------------------------------


Parts:
----------------------------------------------------------------------
1-SLAMTEC RPLIDAR A2M8
2-Raspberry pi 4/PC
----------------------------------------------------------------------


Parameters:
----------------------------------------------------------------------
range: the angle range in degrees. Note that the middle of the angle range will be at zero degrees (which is in the opposite direction of the Lidar wire). since the Lidar rotates clockwise the angle will increase by using the left hand rule. So, for an example of you put the range as 90 then the range will be from 0 to 45 and 0 to 315 (please refer to the Illustrations Folder).
obstacleDistance: this is the maximum distance in mm required to detect an obstacle (Note that from zero to 200mm the lidar can not get a reading)
port: the port to the lidar sensor (it was explained in details in the Instructions and Notes section)
baudrate: bits per second transferred by using UART serial communication. in our Lidar (A2M8) it is either 115200 or 256000
----------------------------
It is not recommended to change the last three parameters:
timeout: Serial port connection timeout in seconds (the default is 1)
maximumBufferMeasurements: Maximum number of measures to be stored inside the buffer. Once number exceeds this limit buffer will be emptied out.
minimumMeasurementsPerScan: Minimum number of measures in the scan for it to be yielded.
----------------------------------------------------------------------
