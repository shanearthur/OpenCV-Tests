import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    #canny = cv.Canny(frame, 125, 175)
    lab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    cv.imshow('Video', lab)
    cv.imshow('Video Source', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()