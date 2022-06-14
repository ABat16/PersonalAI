import numpy as np
import cv2 as cv
from takeAPic import scweenshot
from time import time

scweenshot().list_window_names()

poparazzi = scweenshot("Counter-Strike: Global Offensive")

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = poparazzi.doThePic()

    cv.imshow('Computer Vision', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
