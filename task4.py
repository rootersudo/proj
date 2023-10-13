import cv2
import numpy as np
img=cv2.imread("avriil.jpeg")
cv2.imshow("Orig",img)
cv2.imshow("smooth 1",cv2.GaussianBlur(img,(9,9),1))
cv2.imshow("smooth 4",cv2.GaussianBlur(img,(9,9),4))
cv2.imshow("smooth 6",cv2.GaussianBlur(img,(9,9),6))
cv2.imshow("smooth 1_0",cv2.GaussianBlur(img,(0,0),1))
cv2.imshow("smooth 4_0",cv2.GaussianBlur(img,(0,0),4))
cv2.imshow("smooth 6_0",cv2.GaussianBlur(img,(0,0),6))
cv2.waitKey(0)