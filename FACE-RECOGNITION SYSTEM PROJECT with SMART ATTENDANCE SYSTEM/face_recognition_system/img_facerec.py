# Import Libraries
import os
import cv2
import numpy as np
import face_recognition
import face_recognition as fr
from datetime import  datetime


class Image_Face_Recognition_System():
    #Clear the CSV file
    #Run Command: python facerec.py
    def ClearCSV():
        import csv
        
        file = open("attendance.csv", "r")
        csvr = csv.reader(file)
        namelist = []
        Header = f'Name, Time'
        Header = Header.split(',')
        namelist.insert(0, Header)
        file = open("attendance.csv", "w", newline = '')
        csvr = csv.writer(file)
        csvr.writerows(namelist)
        file.close()
    ClearCSV()


                
    # Classify Faces
    #Run Command: python facerec.py
    def Classify_Faces(im):
        """
        Scans/Locates all of the faces in a given test image within test folder 
        and labels them with their name if they are known faces
        while, on the other hand, unknown faces are labeled as unknown
        :param im: str of file path
        :return: list of face names
        """
        
        
        #Encode Faces to the Attendance Sheet
        #Run Command: python facerec.py
        def MarkAttendance(name):
            """
            Encode the name of the scanned faces into the attendance sheet
            and the time it was encoded
            """
            with open('attendance.csv', 'r+') as attendance:
                MyDatalist =  attendance.readlines()
                NameList = []
                for line in MyDatalist :
                    entry = line.split(',')
                    NameList.append(entry[0])
                if name not in NameList:
                    now = datetime.now()
                    Time = now.strftime('%H:%M')
                    attendance.writelines(f'\n{name}, {Time}')
        
        # Encode Faces
        def get_encoded_faces():
            """
            Scans through the faces folder 
            and encodes all the faces with their names
            :return: dict of (name, image encoded)
            """
            encoded = {}
            
            for dirpath, dnames, fnames in os.walk("./faces"):
                for f in fnames:
                    if f.endswith(".jpg") or f.endswith(".png"):
                        face = fr.load_image_file("faces/" + f)
                        encoding = fr.face_encodings(face)[0]
                        encoded[f.split(".")[0]] = encoding
            return encoded
        
        
        def unknown_image_encoded(img):
            """
            Encode an unknown face given the file name as known face
            """
            face = fr.load_image_file("faces/" + img)
            encoding = fr.face_encodings(face)[0]
            return encoding
                    
                    
        faces = get_encoded_faces()
        faces_encoded = list(faces.values())
        known_face_names = list(faces.keys())

        # Resize Image
        def resize(img, size) :
            width = int(img.shape[1]*size)
            height = int(img.shape[0] * size)
            dimension = (width, height)
            return cv2.resize(img, dimension, interpolation = cv2.INTER_AREA)

        # Convert the Image Color/Resize the Image
        img = cv2.imread(im, 1)
        img = fr.load_image_file('test/1.jpg')
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = resize(img, 0.50)

        # Find Face Location
        face_locations = face_recognition.face_locations(img)
        unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

        # Identify if the face is a match for the known face(s)
        face_names = []
        for face_encoding in unknown_face_encodings:
            matches = face_recognition.compare_faces(faces_encoded, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)

            # Create a box around the face
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                cv2.rectangle(img, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)

            # Create a label with a name below the face
                cv2.rectangle(img, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_TRIPLEX
                cv2.putText(img, name, (left -20, bottom + 15), font + 1, 1, (255, 255, 255), 1)
                MarkAttendance(name)

        # Display the Resulting Image
        while True:
            cv2.imshow('AI Face Recognition System', img)
            key = cv2.waitKey(30) & 0xff
            if key == 27:
                cv2.destroyAllWindows()
                return face_names
            else:
                continue

    (Classify_Faces("test/1.jpg"))

#Run Command: python img_facerec.py
