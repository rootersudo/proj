import cv2
import numpy as np

img=np.zeros((100,100))
img[50][50]=255
cv2.imshow("Orig",img)
double=cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow("5x5", cv2.GaussianBlur(img, (5, 5), 0))
cv2.imshow("9x9", cv2.GaussianBlur(img, (9, 9), 0))
cv2.imshow("double 5x5", cv2.GaussianBlur(double, (5, 5), 0))
cv2.waitKey(0)
