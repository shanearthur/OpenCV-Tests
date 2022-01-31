from time import ctime
import cv2 as cv
import mediapipe as mp
import time


mpHolistic = mp.solutions.holistic
hol = mpHolistic.Holistic()

#drawing utility
mpDraw = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

cap = cv.VideoCapture(1)
print(cap)
pTime = 0

while True:
    success, img = cap.read()
    #mg = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = hol.process(imgRGB)
    #print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpHolistic.POSE_CONNECTIONS)
        #mpDraw.draw_landmarks(img, results.pose_world_landmarks)
        mpDraw.draw_landmarks(img, results.face_landmarks, mpHolistic.FACEMESH_TESSELATION,
                                landmark_drawing_spec=None,
                                connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
        mpDraw.draw_landmarks(img, results.left_hand_landmarks, mpHolistic.HAND_CONNECTIONS)
        mpDraw.draw_landmarks(img, results.right_hand_landmarks, mpHolistic.HAND_CONNECTIONS)
        mpDraw.draw_landmarks(img, results.segmentation_mask)
        for i, lm, in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(i, lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv.circle(img, (cx,cy), 5, (255,0,255), -1)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    cv.imshow('Source', img)
    
    if cv.waitKey(20) & 0xFF==ord('d'): 
        break