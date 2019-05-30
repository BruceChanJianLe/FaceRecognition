# Face Recognition

There are two steps in face regconition, first face detection, second face recognition.

Currently, there are four ready to use face detector out there:
- Haar Cascade Face Detector in OpenCV
- Deep Learning based Face Detector in OpenCV
- Histogram of Oriented Gradient (HOG) Face Detector in Dlib
- Deep Learning based Face Detector in Dlib

The one used in this this project is HOG face detector as it is the fastest among all and the accuracy is good. However, it needs faces that face the camera. The algorithm of this project will output a result image of the input file. Use argparser to input a picture.

Below I shall discuss the pros and cons of the 4 different methods.

## 1. Haar Cascade Face Detector in OpenCV

### Pros

- Works almost real-time on CPU
- Simple Architecture
- Detects faces at different scales

### Cons

- The major drawback of this method is that it gives a lot of False predictions.
- Doesn¡¯t work on non-frontal images.
- Doesn¡¯t work under occlusion

## 2. DNN Face Detector in OpenCV

### Pros

- Most accurate out of the four methods
- Runs at real-time on CPU
- Works for different face orientations ¨C up, down, left, right, side-face etc.
- Works even under substantial occlusion
- Detects faces across various scales ( detects big as well as tiny faces )

### Cons

- Slow

## 3. Histogram of Oriented Gradient Face Detector by Dlib

### Pros

- Fastest method on CPU
- Works very well for frontal and slightly non-frontal faces
- Light-weight model as compared to the other three.
- Works under small occlusion

### Cons

- The major drawback is that it does not detect small faces as it is trained for minimum face size of 80¡Á80. Thus, you need to make sure that the face size should be more than that in your application. You can however, train your own face detector for smaller sized faces.
- The bounding box often excludes part of forehead and even part of chin sometimes.
- Does not work very well under substantial occlusion
- Does not work for side face and extreme non-frontal faces, like looking down or up.

## 4. CNN Face Detector in Dlib

### Pros

- Works for different face orientations
- Robust to occlusion
- Works very fast on GPU
- Very easy training process

### Cons

- Very slow on CPU
- Does not detect small faces as it is trained for minimum face size of 80¡Á80. Thus, you need to make sure that the face size should be more than that in your application. You can however, train your own face detector for smaller sized faces.
- The bounding box is even smaller than the HOG detector.

## Reference

https://www.learnopencv.com/face-detection-opencv-dlib-and-deep-learning-c-python/

## Face Recognition

To preform face recognition, in this project I am using face encodings.
Face encoding is transforming the facial feature into a set of numbers which may, for example, represent the distance of the cheeck bones, distance of each eyes and so on. 128 set of them.
And then euclidean distance between two encodings, those that are less that the threshold (0.6) will result in same faces, while those larger than threshold (0.6) will be considered as different faces.

### To use the algorithm
Input 3 image of 3 person you know, and input one image that you would like to recognize. The algorithm will output the result at the terminal. Note that if the image is too small, you may want to resize fisrt below feeding into the algorithm.

## Refernce

https://www.lynda.com/Python-tutorials/Representing-face-set-measurements/628706/788536-4.html?srchtrk=index%3a2%0alinktypeid%3a2%0aq%3adeep+learning%0apage%3a1%0as%3arelevance%0asa%3atrue%0aproducttypeid%3a2

## Others

### or create a new repository on the command line

echo "# FacialRecognition" >> README.md

git init

git add README.md

git commit -m "first commit"

git remote add FR https://github.com/BruceChanJianLe/FaceRecognition.git

git push -u FR master

### or push an existing repository from the command line

git remote add FR https://github.com/BruceChanJianLe/FaceRecognition.git

git push -u FR master
