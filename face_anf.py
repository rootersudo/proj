import cv2 as cv
import numpy as np
img= cv.imread('face.jpeg')
im=img
print(img.size)
for x in range(225):
    for y in range(224):
        for j in range(3):
            if img[x][y][j]>255/2:
                img[x][y][j]=255-img[x][y][j]
            elif img[x][y][j]<255/2:
                img[x][y][j] = img[x][y][j]+127

cv.imshow("invert",img)


img1 = cv.Laplacian(img,3,ksize=7)

cv.imshow("Laplas",img1)
def find(img):
    im=img

    for x in range(1,224):
        for y in range(1,224):
            for j in range(3):

                if (abs(float(img[x][y][j])-float(img[x-1][y-1][j])))>200:

                    img[x][y][j]=img[x][y][j]

                    #img=cv.inpaint(img,im,inpaintRadius=3,flags=1)
                elif(abs(float(img[x][y][j])-float(img[x-1][y-1][j])))<=100:
                    img[x][y][j] = 0
    cv.imshow('paint',img)
find(img1)
cv.waitKey(0)