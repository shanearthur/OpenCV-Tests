import cv2 as cv

capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=4)

    print(len(faces_rect))

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv.imshow('Video Source', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()