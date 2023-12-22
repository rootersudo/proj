import cv2
import numpy as np
src1=cv2.imread("src3.jpg")
src2=cv2.imread("src3.jpg")
src2=src2/1.00013
diff12=abs(src1-src2)
cv2.imshow("diff",diff12)
kernel = np.ones((5, 5), 'uint8')
kernel[2][2]=3
cleandiff=cv2.dilate(diff12,kernel)
cleandiff=cv2.dilate(cleandiff,kernel)
cv2.imshow("cleandiff",cleandiff)
dirtydiff=cv2.dilate(diff12,kernel)
dirtydiff=cv2.dilate(dirtydiff,kernel)
cv2.imshow("dirtydiff",dirtydiff)
cv2.waitKey(0)