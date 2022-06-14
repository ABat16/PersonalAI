import pandas as pd
import cv2 as cv
import numpy as np
import csv
import pyautogui,sys
from time import time
from windowcapture import WindowCapture
from vision import Vision
from puzzle import Puzzle
from backtrack import Backtrack_AC

wincap = WindowCapture()


needles = ['needles/1.jpg','needles/2.jpg','needles/3.jpg','needles/4.jpg','needles/5.jpg','needles/6.jpg','needles/7.jpg','needles/8.jpg','needles/9.jpg']
haystack = wincap.get_screenshot()

vision = Vision()
grid = [['?']*9 for i in range(9)]
for i in range(len(needles)):
    points = vision.find(haystack,needles[i],threshold = .9,debug_mode = 'rectangles')
    for point in points:
        if point[0] > 350 and point[0] < 405:
            y = 0
        elif point[0] > 405 and point[0] < 460:
            y = 1
        elif point[0] > 460 and point[0] < 515:
            y = 2
        elif point[0] > 515 and point[0] < 570:
            y = 3
        elif point[0] > 570 and point[0] < 625:
            y = 4
        elif point[0] > 625 and point[0] < 680:
            y = 5
        elif point[0] > 680 and point[0] < 735:
            y = 6
        elif point[0] > 735 and point[0] < 790:
            y = 7
        elif point[0] > 790 and point[0] < 845:
            y = 8

        if point[1] > 200 and point[1] < 255:
            x = 0
        elif point[1] > 255 and point[1] < 310:
            x = 1
        elif point[1] > 310 and point[1] < 365:
            x = 2
        elif point[1] > 365 and point[1] < 420:
            x = 3
        elif point[1] > 420 and point[1] < 475:
            x = 4
        elif point[1] > 475 and point[1] < 530:
            x = 5
        elif point[1] > 530 and point[1] < 585:
            x = 6
        elif point[1] > 585 and point[1] < 640:
            x = 7
        elif point[1] > 640 and point[1] < 695:
            x = 8
        grid[x][y] = str(i + 1)

    
with open('puzzle.csv','w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(grid)


"""
grid:

(391,246) () (501,245) () () () () (778,245) ()
() () () () (610,299) (667,301) (723,301) () (833,301)
(389,354) (446,355) () (558,354) (612,355) () () () ()
(390,412) (446,412) (499,410) (557,411) () (667,411) () (778,410) (833,412)
(391,466) () (501,466) (557,465) (612,467) (668,465) (721,465) (777,467) (833,466)
() (447,520) () (555,520) () () () (778,522) (833,521)
() () (501,578) (557,577) () (667,577) (722,578) (779,576) ()
() () (500,633) (557,633) (612,633) () (723,632) () ()
() (444,686) () () () () () (778,687) ()

x starts at 350ish and jumps by 55
y starts at 200ish and jumps by 55
"""

key = [[[390, 265], [449, 262], [497, 267], [555, 266], [601, 261], [674, 266], [722, 267], [772, 267], [830, 267]],
       [[390, 318], [444, 319], [497, 319], [556, 319], [614, 319], [675, 320], [738, 320], [771, 322], [826, 324]],
       [[383, 374], [440, 376], [498, 376], [565, 375], [606, 375], [665, 375], [722, 375], [773, 380], [831, 376]],
       [[389, 432], [432, 432], [492, 429], [564, 434], [611, 432], [657, 432], [725, 431], [776, 431], [821, 432]],
       [[394, 484], [448, 485], [488, 485], [561, 483], [607, 481], [667, 484], [723, 488], [780, 490], [838, 489]],
       [[394, 535], [436, 537], [500, 546], [559, 542], [606, 543], [668, 544], [711, 542], [768, 542], [827, 546]],
       [[381, 597], [439, 597], [498, 595], [558, 599], [606, 598], [666, 598], [722, 592], [776, 597], [838, 597]],
       [[389, 651], [445, 648], [489, 649], [563, 650], [611, 651], [665, 653], [717, 651], [767, 652], [833, 653]],
       [[384, 701], [444, 705], [499, 704], [552, 704], [602, 707], [667, 708], [713, 709], [775, 708], [828, 710]]]


df = pd.read_csv("puzzle.csv", header = None)

puzzle = Puzzle(df)

solved = Backtrack_AC(puzzle).solve()

for i in range(9):
    for j in range(9):
        if grid[i][j] == '?':
            sol = solved.board.iloc[i][j]
            pyautogui.moveTo(key[i][j][0],key[i][j][1])
            #cv.waitKey(1)
            pyautogui.click()
            #cv.waitKey(1)
            pyautogui.keyDown(str(sol))
            #cv.waitKey(1)
            
