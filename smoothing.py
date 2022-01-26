import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)


# Averaging
average = cv.blur(img, (7,7))
cv.imshow('Averaged Cats', average)

# Gaussian
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Cats', gauss)

# Median
median = cv.medianBlur(img, 7)
cv.imshow('Median Cats', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 30, 30)
cv.imshow('Bilateral Cats', bilateral)


cv.waitKey(0)