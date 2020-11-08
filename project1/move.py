import cv2
import numpy as np

# 平移
# 算法描述：
# 用相应的库读取图片信息，获取图片的大小，遍历每个像素点，将每个像素点移动固定（向右移动100px）的位置，即可实现图像移动
img = cv2.imread("image01.jpg", 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]
cv2.imshow('original-image', img)

dst = np.zeros(imgInfo, np.uint8)

for i in range(height):
    for j in range(width - 100):
        dst[i, j + 100] = img[i, j]

cv2.imshow('moved-image', dst)
cv2.waitKey(0)
