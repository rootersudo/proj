import cv2
import numpy as np
img=cv2.imread("avriil.jpeg")
cv2.imshow("Orig",img)
k=input()
if k ==1:
    cv2.imshow("smooth 1",cv2.GaussianBlur(img,(9,9),1))
    cv2.imshow("smooth 4",cv2.GaussianBlur(img,(9,9),4))
    cv2.imshow("smooth 6",cv2.GaussianBlur(img,(9,9),6))
    cv2.imshow("smooth 1_0",cv2.GaussianBlur(img,(0,0),1))
    cv2.imshow("smooth 4_0",cv2.GaussianBlur(img,(0,0),4))
    cv2.imshow("smooth 6_0",cv2.GaussianBlur(img,(0,0),6))
else:
    cv2.imshow("smooth 1_9", cv2.GaussianBlur(img, (0, 0), 1,sigmaY=9))
    cv2.imshow("smooth 9_1", cv2.GaussianBlur(img, (0, 0), 9, sigmaY=1))
    cv2.imshow("smooth 0_0", cv2.GaussianBlur(img, (9, 9), 0, sigmaY=0))
cv2.waitKey(0)