# OpenCV-Face-Recognition
Real-time face recognition project with OpenCV and Python
<br><br>
Links for complete Tutorial:
<br>
https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826<br>
https://www.instructables.com/id/Real-time-Face-Recognition-an-End-to-end-Project/
<br>
<p><img src="https://github.com/Mjrovai/OpenCV-Face-Recognition/blob/master/FaceRecogBlock.png?raw=true"></p>
<br><br>

# Dependencies
* Numpy
* OpenCV
* PIL

# Usage
* Clone the repository and navigate to the folder OpenCV-Face-Recognition
* The <b>FaceDetection</b> folder contains code to detect face,eye and smile using haarcascades.Simply run the python program to see this in action.
* The <b>FacialRecognition </b> folder contains code for real time face recognition.To train a face recognizer:<br>
1. As for first step run the <b>01_face_dataset.py</b> code. This will ask you to input the user id. Input a unique id for each user. All the captured images will be stored in the <b>dataset</b> folder. All these images will be the data on which you will train.<br>
2. Next run <b>02_face_training.py</b> code. This will take the images of the different users that you stored in the <b>dataset</b> folder and trains on these images using a LBPHFaceRecognizer. The trained model is then saved into <b>trainer</b> folder as <b>trained.yml</b>.<br>
3. To do real time face recognition run <b>03_face_recognition.py</b> code. This will load the trained model in the previous step and using this recognizes faces on live video feed.
  
