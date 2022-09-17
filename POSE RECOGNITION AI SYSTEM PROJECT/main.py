#Import Libraries
import mediapipe as mp
import cv2
import datetime
import imutils

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture('PoseVideos/2.mp4')
#cap =cv2.VideoCapture(0)

#Frames Per Second
fps_start_time = datetime.datetime.now()
fps = 0
total_frames = 0
# Initialize MediaPipe Holistic
with mp_holistic.Holistic(
    static_image_mode=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while True:
        success, image = cap.read()
        
        if success:
            #Convert the BGR image to RGB and process it with MediaPipe Pose
            img = imutils.resize(image, width=600)
            total_frames = total_frames + 1
            results = holistic.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

            #Print Nose Coordinates.
            image_hight, image_width, _ = image.shape
            if results.pose_landmarks:
                print(
                f'Nose Coordinates: ('
                f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x * image_width},'
                f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].y * image_hight})'
              )

            # Draw Landmarks
            annotated_image = image.copy()
            #LEFT_HAND
            mp_drawing.draw_landmarks(
                annotated_image, 
                results.left_hand_landmarks, 
                mp_holistic.HAND_CONNECTIONS,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=1),
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=1))
            #RIGHT_HAND
            mp_drawing.draw_landmarks(
                annotated_image, 
                results.right_hand_landmarks, 
                mp_holistic.HAND_CONNECTIONS,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=1),
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,255), thickness=1, circle_radius=1))
            #FACE
            mp_drawing.draw_landmarks(
                image=annotated_image, 
                landmark_list=results.face_landmarks, 
                connections=mp_holistic.FACEMESH_TESSELATION,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,0), thickness=1, circle_radius=1),
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 0), thickness=1, circle_radius=1))
            #POSE
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    image=annotated_image, 
                    landmark_list=results.pose_landmarks, 
                    connections=mp_holistic.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
                    connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1))
            
            #Show Frames Per Second
            fps_end_time = datetime.datetime.now()
            time_diff = fps_end_time - fps_start_time
            if time_diff.seconds == 0:
                fps = 0
            else:
                fps = (total_frames / time_diff.seconds)*10
        
            fps_text = " fps"
        
            cv2.putText(annotated_image, str(int(fps)) + fps_text, (20, 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 1)
            
            #Program Name
            cv2.imshow("Pose Recognition AI System", annotated_image)

            # Terminate the Program
            if cv2.waitKey(1) & 0xFF ==27:
                break
        else:
            break
        
cap.release()
cv2.destroyAllWindows()

#Run command: python main.py
