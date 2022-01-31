import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
#cv.imshow('Group', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray Group', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

    
cv.imshow('Detection', img)

cv.waitKey(0)