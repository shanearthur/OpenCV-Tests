import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Park', img)

# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("Grayscale Park", gray)

# blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#cv.imshow("Gaussian Park", blur)]

# edge cascade
canny = cv.Canny(blur, 125, 175)
#cv.imshow("Canny Park", canny)

# dilating
dilated = cv.dilate(canny, (3,3), iterations=1)
#cv.imshow('Dilated Park', dilated)

# eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
#cv.imshow('Eroded Park', eroded)

# resize
resized = cv.resize(img, (500,500))
#cv.imshow('Resized', resized)
resized_2 = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
#cv.imshow('Resized 2', resized_2)
resized_3 = cv.resize(img, (1920,1080), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized 3', resized_3)

# cropping
cropped = img[50:200, 0:200]
cv.imshow('Cropped Park', cropped)

cv.waitKey(0)