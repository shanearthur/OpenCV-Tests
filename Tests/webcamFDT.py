import cv2 as cv

capture = cv.VideoCapture(1)

SENSITIVITY = 11
w_cur, w_las, counter = 0, 0, 0

while True:
    counter += 1

    isTrue, frame = capture.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=4)

    #print(len(faces_rect))

    for (x,y,w,h) in faces_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
        
        w_cur = w
        diff = abs(w_cur - w_las)
        if w_las + SENSITIVITY > w_cur and w_las - SENSITIVITY < w_cur:
            print(f"STABLE [           -->>[]<<--           ] ...Diff: {diff} / Count: {counter}")
        elif w_cur > w_las:
            print(f"CLOSER [               [] -------->>    ] ...Diff: {diff} / Count: {counter}")
        else:
            print(f"FUTHER [    <<-------- []               ] ...Diff: {diff} / Count: {counter}")
        if counter % 5 == 0:
            w_las = w_cur

    cv.imshow('Video Source', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()