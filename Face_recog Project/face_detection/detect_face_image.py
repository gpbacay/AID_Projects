# Import Libraries
import cv2
import numpy as npy
import face_recognition as face_rec

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#function
def resize(img, size):
    width = int(img.shape[1]*size)
    height = int(img.shape[0] * size)
    dimension =(width, height)
    return cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)

# Read the input image
img = cv2.imread('sample.jpg')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resize(img, 0.50)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()

#Run Command: python detect_face_image.py