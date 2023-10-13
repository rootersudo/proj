

import cv2
import numpy as np
img=cv2.imread('avriil.jpeg')
b,g,r = cv2.split(img)
cv2.imshow('Original', img)
#cv2.imshow('blue',b)
gr=cv2.imshow("green", g)

green=img[:,:,1]
#cv2.imwrite('gr.jpeg',green)
gr=cv2.minMaxLoc(green)
clone1=green.copy()
clone2=green.copy()
print(gr[0],gr[1])
tresh = np.array(0,dtype='B')
tresh=int((gr[1]-gr[0])/2.0)
clone1=tresh
#print(clone1)
clone2=0
clone2=cv2.compare(green,clone1,clone2,cv2.CMP_GE)
res=cv2.subtract(green,tresh/2,np.float32(green),clone2)
cv2.imshow('result',res)

#cv2.imshow("red", r)
cv2.waitKey(0)
