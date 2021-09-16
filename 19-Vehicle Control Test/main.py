from pynput.keyboard import Key, Listener
import serial
import os
#Note: if you will not use alphanumeric characters in the values of the dictionary p, then you need to change the value from string to Key.#The Key Name#. For an example if you want to change from the charectar a to the up arrow, than change "a" to Key.up or if you want to change from the number 4 to escape than change "4" to Key.esc. if you want to know the name of the non-alphanumeric character than make the value of the key "printValue" to True so that you could see how it is named on the console. if you are controlling from Windows PC choose the right value of portWindows key and ignore portLinux and vise versa. Note that the port for linux is either /dev/ttyUSB#Number# or /dev/ttyACM#Number# for an example /dev/ttyUSB1 or /dev/ttyACM0

p={

"steeringStepperMotorCW": Key.up,  
"steeringStepperMotorCCW":Key.down,

"speedStepperMotorCW":"q",
"speedStepperMotorCCW":"d",

"breakStepperMotorCW":"b",
"breakStepperMotorCCW":"o",

"portWindows":'COM3',
"portLinux":"/dev/ttyACM0",

"baudrate":9600,
"timeout":1,

"stopListening":Key.esc,

"printValue": False

}



try:
    arduino = serial.Serial(p["portLinux"],baudrate=p["baudrate"],timeout=p["timeout"])
except:
    try:
        arduino = serial.Serial(p["portLinux"],baudrate=p["baudrate"],timeout=p["timeout"])
    except:
        print("Make sure to make portWindows or portLinux equal to the port connected to Arduino")
        exit()
we



def on_press(key):
    if p["printValue"]==True:
        print(key)
    
    

    try:
        if key.char==p["steeringStepperMotorCW"]:

            steer="s1"
            arduino.write(bytes(steer, 'utf-8'))
        
            print("steercw char")
    except AttributeError:
        if key==p["steeringStepperMotorCW"]:

            steer="s1"
            arduino.write(bytes(steer, 'utf-8'))
            
            print("steercw not")


    try:
        if key.char==p["steeringStepperMotorCCW"]:

            steer="s-1"
            arduino.write(bytes(steer, 'utf-8'))

            print("steerccw char")
    except AttributeError:
        if key==p["steeringStepperMotorCCW"]:

            steer="s-1"
            arduino.write(bytes(steer, 'utf-8'))

            print("steerccw not")


    try:
        if key.char==p["speedStepperMotorCW"]:

            steer="v1"
            arduino.write(bytes(steer, 'utf-8'))

            print("speedcw char")
    except AttributeError:
        if key==p["speedStepperMotorCW"]:

            steer="v1"
            arduino.write(bytes(steer, 'utf-8'))

            print("speedcw not")


    try:
        if key.char==p["speedStepperMotorCCW"]:

            steer="v-1"
            arduino.write(bytes(steer, 'utf-8'))

            print("speedccw char")
    except AttributeError:
        if key==p["speedStepperMotorCCW"]:

            steer="v-1"
            arduino.write(bytes(steer, 'utf-8'))

            print("speedccw not")


    try:
        if key.char==p["breakStepperMotorCW"]:

            steer="b1"
            arduino.write(bytes(steer, 'utf-8'))

            print("breakcw char ")
    except AttributeError:
        if key==p["breakStepperMotorCW"]:

            steer="b1"
            arduino.write(bytes(steer, 'utf-8'))

            print("breakcw not")

    try:
        if key.char==p["breakStepperMotorCCW"]:

            steer="b-1"
            arduino.write(bytes(steer, 'utf-8'))

            print("breakccw char")
    except AttributeError:
        if key==p["breakStepperMotorCCW"]:

            steer="b-1"
            arduino.write(bytes(steer, 'utf-8'))

            print("breakccw not")        

   
    

def on_release(key):
    try:
        if key.char==p["stopListening"]:
            print("no listen char")
            return False
    except AttributeError:
        if key==p["stopListening"]:
            print("no listen not")
            return False

     


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()


#https://www.youtube.com/watch?v=TbMKwl11itQ
#https://www.youtube.com/watch?v=iKGYbMD3NT8&list=PLb1SYTph-GZJb1CFM7ioVY9XJYlPVUBQy