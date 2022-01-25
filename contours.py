import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

#cv.imshow('Cats', img)

# blank image of same shape for drawing
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray Cats', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

#canny = cv.Canny(blur, 125, 175)
#cv.imshow('Canny Cats', canny)

# threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

# now that we have an edge detected frame, we can find contours
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)