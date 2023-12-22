import cv2
import numpy as np
src=cv2.imread("src3.jpg")
for x in range(1):
    src=cv2.resize(src,(0,0),fx=0.5,fy=0.5)
cv2.imshow("resize",src)
src=cv2.imread("src3.jpg")
for x in range(1):
    src=cv2.pyrDown(src)
cv2.imshow("pyrDowm",src)
cv2.waitKey(0)