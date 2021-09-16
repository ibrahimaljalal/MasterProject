#!/usr/bin/env python3

from rplidar import RPLidar
import rplidar
import sys

p={
"range":90,
"obstacleDistance":1000,

#for windows com#number# (for example com1 or com2 etc) for linux /dev/ttyACM0 (0 or more) or  /dev/ttyUSB0 (0 or more) 
"port":"com6",

#115200 or 256000
"baudrate":115200,

#It is recommended to not change the values below
######################################
#in seconds
"timeout":1,
#False or an integer
"maximumBufferMeasurements":False,
#minimum samples allowed for on rotation (or one scan) (Note: if you set it to a high number the lidar might not give you any results)
"minimumMeasurementsPerScan":50
######################################

}

lowerAngle=p["range"]/2
upperAngle=360-p["range"]/2

if len(sys.argv)>1:
            p["port"]=sys.argv[1]

try:
    lidar = RPLidar(port=p["port"],baudrate=p["baudrate"],timeout=p["timeout"])
except rplidar.RPLidarException:
    print("Please choose the right port.\nif you are using Linux you should write on the terminal sudo chmod 666 /dev/ than the device name.\nFor an example  sudo chmod 666 /dev/ttyUSB0 or sudo chmod 666 /dev/ttyACM0\n(Note: the last number might not be 0 for an example ttyUSB2)")
    sys.exit()


def startTestLidar():
    try:           
        for scan in lidar.iter_scans(scan_type='normal', max_buf_meas=p["maximumBufferMeasurements"], min_len=p["minimumMeasurementsPerScan"]):
            for quality, angle, distance in scan:
                if ((angle<lowerAngle) or (angle>upperAngle)) and distance<p["obstacleDistance"]:
                    description="angle: "+"{:.2f}".format(angle)+" degrees,"+" distance: "+"{:.2f}".format(distance)+" mm"
                    print(description)
                    break
                    #return True
                    
                else:
                    return False
    except KeyboardInterrupt:
        lidar.stop()
        lidar.stop_motor()
        lidar.disconnect()



