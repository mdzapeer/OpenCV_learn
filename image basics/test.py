#batch resize
import cv2

class Image():
    
    def __init__(self,imagepath):
        print(imagepath)
        self.img=cv2.imread(imagepath,1)
        print(self.img)
        
    def resize(self):
        self.resized=cv2.resize(self.img,(int(self.img.shape[1]/10),int(self.img.shape[0]/10)))
        print(self.resized)

    def write(self,writename):
        cv2.imwrite(writename+"_resized.jpg",self.resized)

image=Image("Lighthouse.jpg")

image.resize()
image.write("Lighthouse")



