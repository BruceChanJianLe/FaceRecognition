import face_recognition
import cv2
import argparse

# Construct the argument parser and parse argument
ap = argparse.ArgumentParser()
ap.add_argument('-i1', '--image1', default='person_1.jpg',
                help='Path to input image 1, the first person you would like to recognize')
ap.add_argument('-i2', '--image2', default='person_2.jpg',
                help='Path to input image 2, the second person you would like to recognize')
ap.add_argument('-i3', '--image3', default='person_3.jpg',
                help='Path to input image 3, the third person you would like to recognize')
ap.add_argument('-i4', '--input', default='unknown_1.jpg',
                help='Path to input image 4, the unknown person you would like to recognize')
args = ap.parse_args()

# Load the known images
img_1 = cv2.imread(args.image1)
img_2 = cv2.imread(args.image2)
img_3 = cv2.imread(args.image3)

# Get the face encoding of each person. This can fail if no one is found in the photo,
# Note that in img_1 img_2 img_3 there is only one face therefore we index a [0].
person_1_face_encoding = face_recognition.face_encodings(img_1)[0]
person_2_face_encoding = face_recognition.face_encodings(img_2)[0]
person_3_face_encoding = face_recognition.face_encodings(img_3)[0]

# Create a list of all known face encodings
known_face_encodings = [
    person_1_face_encoding,
    person_2_face_encoding,
    person_3_face_encoding
]

# Load the image we want to check
unknown_img = cv2.imread(args.input)

# Get face encodings for any people in the picture
unknown_face_encodings = face_recognition.face_encodings(unknown_img)

# There might be more than one person in the photo, so we need to loop over each face we found
for unknown_face_encoding in unknown_face_encodings:

    # Test if this unknown face encoding matches any of the three people we know
    results = face_recognition.compare_faces(known_face_encodings, unknown_face_encoding,
                                             tolerance=0.6)

    name = "Unknown"

    if results[0]:
        name = "Person 1"
    elif results[1]:
        name = "Person 2"
    elif results[2]:
        name = "Person 3"

    print(f"Found {name} in the photo!")
