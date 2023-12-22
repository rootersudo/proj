import cv2
import numpy as np
img=cv2.imread("src3.jpg")
src= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(src,128,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,5)
cv2.imshow("tr",thresh)
cv2.waitKey(0)
thresh1 = cv2.adaptiveThreshold(src,128,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,5)
cv2.imshow("tr1",thresh1)
'''thresh2=cv2.adaptiveThreshold(src,128,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_TRUNC,11,5)
cv2.imshow("tr2",thresh2)
thresh3 = cv2.adaptiveThreshold(src,128,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_TOZERO,11,5)
cv2.imshow("tr3",thresh3)
thresh4 = cv2.adaptiveThreshold(src,128,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_TOZERO_INV,11,5)
cv2.imshow("tr4",thresh4)'''
cv2.waitKey(0)