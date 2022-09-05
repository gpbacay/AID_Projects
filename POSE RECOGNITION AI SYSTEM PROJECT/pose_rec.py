#Import Libraries
import cv2
import mediapipe as mp
import time
import imutils

#Declare Variables
mp_holistic = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
drawing_spec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)
pose = mp_holistic.Pose()


#Initialize Video
cap = cv2.VideoCapture('PoseVideos/5.mp4')

#FPS
fps_start_time = 0
total_frames = 0

# Initialize MediaPipe Holistic.
with mp_holistic.Holistic(
    static_image_mode=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while True:
        success, img = cap.read()
    
        if success:
            #Convert the BGR image to RGB and process it with MediaPipe Pose.
            img = imutils.resize(img, width=600)
            total_frames = total_frames + 1
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = pose.process(imgRGB)
            #Print Pose Coordinates
            print(results.pose_landmarks)
    
            #if results.pose_landmarks:
            #    mpDraw.draw_landmarks(img, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
            #    for id, lm in enumerate(results.pose_landmarks.landmark):
            #        h, w, c = img.shape
            #        print(id, lm)
            #        cx, cy = int(lm.x * w), int(lm.y * h)
            #        cv2.circle(img, (cx, cy), 4, (255, 0, 0), cv2.FILLED)
            
            #Draw Pose Landmarks    
            if results.pose_landmarks:
                annotated_img = img.copy()
        
                mpDraw.draw_landmarks(
                    image=annotated_img,
                    landmark_list=results.pose_landmarks,        
                    connections=mp_holistic.POSE_CONNECTIONS, 
                    landmark_drawing_spec=drawing_spec,
                    connection_drawing_spec=drawing_spec)    
                for id, landmark_list in enumerate(results.pose_landmarks.landmark):
                    h, w, c = img.shape
                    print(id, landmark_list)
                    cx, cy = int(landmark_list.x * w), int(landmark_list.y * h)
                    cv2.circle(img, (cx, cy), 4, (255, 0, 0), cv2.FILLED)
            
            
            #Show FPS
            fps_end_time = time.time()
            time_diff = fps_end_time - fps_start_time
            fps = 1/(time_diff)*10
            fps_start_time = fps_end_time
    
            fps_text = " fps"
            cv2.putText(img, str(int(fps)) + fps_text, (20, 30), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 255), 1)
    

            #Show Program Name
            cv2.imshow("Pose Recognition AI System", img)
            # Terminate the Program
            if cv2.waitKey(1) & 0xff ==27:
                break
        else:
            break

cap.release()
cv2.destroyAllWindows()

#python pose_rec.py  