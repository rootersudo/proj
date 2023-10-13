import cv2
import numpy as np




#-----------ex 1------------------


img=cv2.imread("11.jpeg")
cv2.imshow("Orig",img)
cv2.imshow("3x3",cv2.GaussianBlur(img,(3,3),0))
cv2.imshow("5x5",cv2.GaussianBlur(img,(5,5),0))

double=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("double 5x5",cv2.GaussianBlur(double,(5,5),0))
cv2.imshow("11x11",cv2.GaussianBlur(img,(11,11),0))
cv2.waitKey(0)




