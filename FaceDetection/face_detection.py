import cv2
import numpy as np
import dlib
import argparse

# Construct the argumnet parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', default='people.jpg', help='path to input image file')
ap.add_argument('-s', '--shapepath', default='shape_predictor_68_face_landmarks.dat'
                , help='path to shape predictor')
args = ap.parse_args()

# Load the jpg file
img = cv2.imread(args.image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Face Detector
face_detector = dlib.get_frontal_face_detector()

# Face Landmark Detector
face_landmark = dlib.shape_predictor(args.shapepath)

# Print the faces found in the image
faces = face_detector(gray)
print(f'{len(faces)} face(s) was(were) found by the detector')



# Define the parameters
colour = (0, 255, 0)
thickness = 3
for face in faces:
    cv2.rectangle(img, (face.left(), face.top()), (face.right(), face.bottom()),
                  color=colour, thickness=thickness)

    # Obtain the face landmarks
    landmarks = face_landmark(gray, face)

    for n in range(68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(img, (x, y), 2, (255, 0, 0), -1)

cv2.imwrite(f'result_{args.image}', img)
