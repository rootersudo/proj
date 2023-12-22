import cv2
import numpy as np

src1=cv2.imread("src3.jpg")
coff=cv2.imread("coff.jpg")
cv2.imshow("orig",coff)
src1=src1/2
coff=coff/2
diff=abs(coff-src1)
cv2.imshow("diff",diff)
kernel=np.ones((3,3),'uint8')
ret,diff=cv2.threshold(diff,35,255,0)
cv2.imshow("diff1",diff)
diff=cv2.morphologyEx(diff, cv2.MORPH_OPEN, kernel)
cv2.imshow("Morph",diff)

cv2.waitKey(0)