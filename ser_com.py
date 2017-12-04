#Random Python Scripts
#(c) 2017 Maroko Gideon
#www.gmaroko.me
#marokogideon@gmail.com
#question by Jose Aug, 2017

import serial, time
from image_capture import captureImage

#setup
baudrate = 9600
port = input(">") #'COM13' #~I used COM13 on my machine
ser = serial.Serial()

def configure():
    ser.baudrate = baudrate
    ser.port = port
    ser.open()
    return True

def signal():
    while True:
        try:
            data = ser.read()
            if data == b'\01':     #1 bit of data from arduino
                #print('Image..')  #uncomment to keep track of when an image is taken
                captureImage()
                time.sleep(5)
                break
            else:
                #print('No signal..')  #uncomment to keep track of the wait time before receiving a signal
                signal()
        except Exception as e:
            print(e)
            
def main():
    try:     #incase the board is not configured correctly
        configure()
        signal()
    except Exception as e:
        print(e)
        
if __name__ == '__main__':
    main()
