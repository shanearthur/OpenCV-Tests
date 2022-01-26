import cv2 as cv
import matplotlib.pyplot as plt

capture = cv.VideoCapture(1)

while True:
    isTrue, frame = capture.read()
    canny = cv.Canny(frame, 125, 175)
    # lab = cv.cvtColor(frame, cv.COLOR_BGR2LAB)
    # cv.imshow('Video', lab)
    cv.imshow('Canny', canny)
    cv.imshow('Video Source', frame)
    
    # plt.figure()
    # colors = ('b', 'g', 'r')
    # for i, col in enumerate(colors):
    #     hist = cv.calcHist([frame], [i], None, [256], [0,256])
    #     plt.plot(hist, color=col)
    #     plt.xlim([0,256])

    # plt.show()
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()