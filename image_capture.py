#Random Python Scripts
#(c) 2017 Maroko Gideon
#www.gmaroko.me
#marokogideon@gmail.com
#question by Joseph August, 2017

#uses opencv to capture a colored image

import cv2 as cv
import time
import numpy as np    #required for open cv, importing it makes our script faster

def captureImage():
    randomfileName = str(round(time.time()))
    capture = cv.VideoCapture(0)
    #frameName = 'some_window_name'      #uncomment and change it if you wish
    taken = False
    while not taken:
        val, frame = capture.read()
        image = cv.cvtColor(frame, cv.IMREAD_COLOR)
        taken = True
        dir = input("Save image to> ") #directory
        cv.imwrite('%s%s.jpg' % (dir,randomfileName), image)  #create a random image name ~ using the current time (epoch) ~ can use it for reference
        cv.destroyAllWindows()

def main():
    captureImage()
    print("Done!")

if __name__ == '__main__':
    main()





