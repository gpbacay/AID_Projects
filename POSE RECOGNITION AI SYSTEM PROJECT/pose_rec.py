#Import Libraries
import cv2
import mediapipe as mp
import time

#Declare Variables
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


#Initialize Video
cap = cv2.VideoCapture('PoseVideos/4.mp4')
pTime = 0
while True:
    _, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    print(results.pose_landmarks)
    
    #Show Model
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(img, (cx, cy), 4, (255, 0, 0), cv2.FILLED)
            
    #Show Frame Rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (60, 40), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1)

    #Show Program Name
    cv2.imshow("Pose Recognition AI System", img)
    # Terminate the Program
    if cv2.waitKey(1) & 0xff ==27:
        break
cap.release()