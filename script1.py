#batch resize
import cv2
from glob import glob
import os

def resizeimg(imagepath):
    img=cv2.imread(imagepath,1)
    imgshapey=int(img.shape[1]/10)
    imgshapex=int(img.shape[0]/10)
    resized=cv2.resize(img,(imgshapey,imgshapex))
    cv2.imwrite("Resized_"+imagepath,resized)

os.chdir("sample-images//")
dircontents=glob("*.jpg")

for image in dircontents:
    resizeimg(image)

