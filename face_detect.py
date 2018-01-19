import cv2
import sys
import numpy as np
 
#cascPath = sys.argv[1]
# cascPath = 'haarcascade_profileface.xml'
# profileFaceCascade = cv2.CascadeClassifier(cascPath)
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)

def detect(filename):
    path='../ptt_beauty_download/newDownload/'+filename
    image=cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # faces = profileFaceCascade.detectMultiScale(
    #     gray,
    #     scaleFactor=1.1,
    #     minNeighbors=15,
    #     minSize=(30, 30)
    # )
    face_images=[]
    # Draw a rectangle around the faces
    # for (x, y, w, h) in faces:
    #     face_images.append(image[y:y+h,x:x+w])
    #     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=20,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        face_images.append(image[y:y+h,x:x+w])
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return image,face_images
