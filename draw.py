import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

# change color
blank[200:300, 300:400] = 0,255,0
#cv.imshow('Green', blank)

# draw rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, 250), (0,255,0), thickness=2)
#cv.imshow('Rectangle', blank)

# draw circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1)
#cv.imshow('Circle', blank)

# draw line
cv.line(blank, (0,0), (250,250), (0,200,200), thickness=3)
#cv.imshow('Line', blank)

# write text
cv.putText(blank, 'First OpenCV render?', (10,350), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0) 