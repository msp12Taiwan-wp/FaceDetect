import face_detect_faceapi_version as face_detect
from os import listdir
from os.path import isfile, isdir, join
import cv2
# 指定要列出所有檔案的目錄
mypath = "D:\\Documents\\桌面\\WinterProject\\ptt_beauty_download\\newDownload"

# 取得所有檔案與子目錄名稱
files = listdir(mypath)

# 以迴圈處理
for f in files:
    # 產生檔案的絕對路徑
    fullpath = join(mypath, f)
    print(fullpath)
    # 判斷 fullpath 是檔案還是目錄
    if isfile(fullpath):
        image,face_images = face_detect.detect(f)
        cv2.imshow('Video', image)
    cv2.waitKey(0)
    for face_image in face_images:
        cv2.imshow('Video', face_image)
        cv2.waitKey(0)
    
    if cv2.getWindowProperty('Video', 0) >= 0:
        pass
    else:
        break


cv2.destroyAllWindows()