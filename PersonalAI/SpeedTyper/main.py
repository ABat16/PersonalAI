import cv2 as cv
import numpy as np
import csv
import pyautogui as py
import time
from windowcapture import WindowCapture
from vision import Vision


# Uses New Style At 300 Percent screen size
wincap = WindowCapture()
vision = Vision()
needle = 'needles/error.jpg'
haystack = wincap.get_screenshot()
vals = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t = 0
input("Place Cursor In Speed Race")
time.sleep(2)
#while t < 1000:
for i in range(len(vals)):
    py.press(vals[i])
    time.sleep(1)
    points = vision.find(haystack, needle, threshold = .80,debug_mode = 'rectangles')
    print(points)
    time.sleep(1)
    if len(points) != 0:
        py.press('backspace')
    else:
        continue
#    t += 1

