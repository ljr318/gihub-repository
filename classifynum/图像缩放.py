import numpy as np
import cv2 as cv

img = cv.imread('Lenna.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst1 = cv.warpAffine(img,M,(cols,rows))

M=cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst2=cv.warpAffine(img,M,(cols,rows))

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M=cv.getAffineTransform(pts1,pts2)
dst3 = cv.warpAffine(img,M,(cols,rows))

M1 = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),0,0.5)
M2 = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),0,2)
dstS = cv.warpAffine(img,M1,(cols,rows))
dstB = cv.warpAffine(img,M2,(cols,rows))

cv.imshow('original',img)
cv.imshow('rotation',dst2)
cv.imshow('translation',dst1)
cv.imshow('Affine Transformation',dst3)
cv.imshow('big',dstB)
cv.imshow('small',dstS)


cv.waitKey(0)
cv.destroyAllWindows()