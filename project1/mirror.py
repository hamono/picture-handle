import cv2
import numpy as np

# 镜像
# 算法：
# 遍历所有像素点，同时在两倍高度（或宽度）的地方（具体位置见代码）复制同样的像素信息
img = cv2.imread('image01.jpg', 1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep = imgInfo[2]
cv2.imshow('original-image', img)

dst = np.zeros([height * 2, width, deep], np.uint8)

for i in range(height):
    for j in range(width):
        dst[i, j] = img[i, j]
        dst[height * 2 - i - 1, j] = img[i, j]

for i in range(width):
    dst[height, i] = (0, 0, 255)
cv2.imshow('mirror-image', dst)
cv2.waitKey(0)
