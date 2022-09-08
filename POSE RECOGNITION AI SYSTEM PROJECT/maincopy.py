#Import Libraries
import mediapipe as mp
import os
import datetime
import imutils
import face_recognition as fr
import cv2
import face_recognition
import numpy as np


# Encode Faces
def get_encoded_faces():
    encoded = {}
    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding
    return encoded

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture('PoseVideos/6.mp4')

#Frames Per Second
fps_start_time = datetime.datetime.now()
fps = 0
total_frames = 0
# Initialize MediaPipe Holistic
with mp_holistic.Holistic(
    static_image_mode=True, min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while True:

        success, image =cap.read()

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
                f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].x * image_width}, '
                f'{results.pose_landmarks.landmark[mp_holistic.PoseLandmark.NOSE].y * image_hight})'
              )

        # Draw Landmarks
            annotated_image = image.copy()
            #LEFT_HAND
            mp_drawing.draw_landmarks(
                annotated_image, 
                results.left_hand_landmarks, 
                mp_holistic.HAND_CONNECTIONS,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1))
            #RIGHT_HAND
            mp_drawing.draw_landmarks(
                annotated_image, 
                results.right_hand_landmarks, 
                mp_holistic.HAND_CONNECTIONS,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1))
            
            #FACE
            faces = get_encoded_faces()
            faces_encoded = list(faces.values())
            known_face_names = list(faces.keys())
            
            """ Find Face Location """
            face_locations = face_recognition.face_locations(img)
            unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

            """ Identify if the face is a match for the known face(s) """
            face_names = []
            for face_encoding in unknown_face_encodings:
                matches = face_recognition.compare_faces(faces_encoded, face_encoding)
                name = "Unknown"

                """ Use the known face with the smallest distance to the new face """
                face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

                """ Create a label with a name below the face """
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_TRIPLEX
                    cv2.putText(img, name, (left -20, bottom + 15), font + 1, 1, (255, 255, 255), 1)

            """Draw FaceMesh Tesselation"""
            mp_drawing.draw_landmarks(
                image=annotated_image, 
                landmark_list=results.face_landmarks, 
                connections=mp_holistic.FACEMESH_TESSELATION,
                landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=1, circle_radius=1),
                connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1))

            #POSE
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    image=annotated_image, 
                    landmark_list=results.pose_landmarks, 
                    connections=mp_holistic.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0,255,0), thickness=4, circle_radius=1),
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


#Run command: python maincopy.py
