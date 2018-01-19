import cv2
import sys
import numpy as np
import urllib
import http.client
import json
params = urllib.parse.urlencode({
    'returnFaceId': "true",
    'returnFaceLandmarks': 'false',
}) 
headers = {
    'Content-type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': 'ecb0bcf4f955494b90c7b76d31821986',
}

def detect(filename):
    path='../ptt_beauty_download/newDownload/'+filename
    image=cv2.imread(path)
    f = open(path, "rb")
    body = f.read()
    f.close()
    try:
        conn = http.client.HTTPSConnection('eastasia.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    face_images=[]
    
    json_data=json.loads(data)
    for face in json_data:
        (x, y, w, h)=(face['faceRectangle']['left'],face['faceRectangle']['top'],face['faceRectangle']['width'],face['faceRectangle']['height'])
        face_images.append(image[y:y+h,x:x+w])
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return image,face_images
