# eyes-face-recognition
This is my second step on face recognition python scripts. The idea here is to push the script to recognize the faces and eyes on a picture.

This is a very simple script to create your first python script in order to recognize a face and eyes on a picture.

Please follow the steps below in order to create your own script !

1. Make sure to have the latest version of python installed (I used Python 3.5)
2. Import numpy and cv2 (make sure to have these two libraries already instlalled or use pip to do so)
3. Create two haar cascade variables to store both xml files for faces and eyes recognition
4. Create two variables to contain the image itself and grayscale image (this is used for the algorithm to analyze the image)
5. Create the function to recognize faces (I have used detectMultiscale and of course grayscale image to be analyzed. Tune other parameters in order to make your function works better)
6. Create two loops the first one that create a rectangle for faces and other loop (embedded) in order to create the rectangle for eyes
7. Print your result
