import cv2
import numpy as np

# 缩放
# 算法：
# 利用最近插值法，取相近的像素点信息
img = cv2.imread('image01.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
dstHeight = int(2*height)
dstWidth = int(2*width)
cv2.imshow('original-image', img)

dstImage = np.zeros([dstHeight, dstWidth, 3], np.uint8)
for i in range(dstHeight):
    for j in range(dstWidth):
        iNew = i * (height * 1.0 / dstHeight)
        jNew = j * (width * 1.0 / dstWidth)

        dstImage[i, j] = img[int(iNew), int(jNew)]

cv2.imshow('resize-image', dstImage)
cv2.waitKey(0)
