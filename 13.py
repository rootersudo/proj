import cv2
import numpy as np
src=cv2.imread("src3.jpg")

re,thresh=cv2.threshold(src,128,255,cv2.THRESH_BINARY)
cv2.imshow("tr",thresh)
ret,thresh1=cv2.threshold(src,128,255,cv2.THRESH_BINARY_INV)
cv2.imshow("tr1",thresh1)
ret1,thresh2=cv2.threshold(src,128,255,cv2.THRESH_TRUNC)
cv2.imshow("tr2",thresh2)
ret2,thresh3=cv2.threshold(src,128,255,cv2.THRESH_TOZERO)
cv2.imshow("tr3",thresh3)
ret3,thresh4=cv2.threshold(src,128,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("tr4",thresh4)
cv2.waitKey(0)