import numpy as np
import cv2


# 去噪（中值滤波）
def denoise(img, num=1):
    midImg = img
    for i in range(num):
        midImg = cv2.medianBlur(midImg, 3)

    return midImg


# rgb通道处理（二值化处理）
def rgbProcess(img):
    # blue图层
    for i in range(img[:, :, 0].shape[0]):
        for j in range(img[:, :, 0].shape[1]):
            if img[:, :, 0][i][j] > 147:
                img[:, :, 0][i][j] = 0
                img[:, :, 1][i][j] = 0
                img[:, :, 2][i][j] = 0
            else:
                img[:, :, 0][i][j] = 255

    # green图层
    for i in range(img[:, :, 1].shape[0]):
        for j in range(img[:, :, 1].shape[1]):
            if img[:, :, 1][i][j] > 150:
                img[:, :, 1][i][j] = 255
            else:
                img[:, :, 1][i][j] = 0

    # red图层
    for i in range(img[:, :, 2].shape[0]):
        for j in range(img[:, :, 2].shape[1]):
            if img[:, :, 2][i][j] > 155:
                img[:, :, 2][i][j] = 255
            else:
                img[:, :, 2][i][j] = 0


# 根据权重计算灰度值
def weightProcess(img):
    BW = 0.2
    RW = 0.4
    GW = 0.4

    bWeight = np.zeros((300, 300), dtype=np.int)
    rWeight = np.zeros((300, 300), dtype=np.int)
    gWeight = np.zeros((300, 300), dtype=np.int)
    for i in range(img[:, :, 2].shape[0]):
        for j in range(img[:, :, 2].shape[1]):
            gWeight[i][j] = img[:, :, 1][i][j] * GW
            bWeight[i][j] = 255 - img[:, :, 0][i][j] * BW
            rWeight[i][j] = img[:, :, 2][i][j] * RW

    for i in range(img[:, :, 2].shape[0]):
        for j in range(img[:, :, 2].shape[1]):
            if img[:, :, 2][i][j] != 0:
                if 210 < gWeight[i][j] + bWeight[i][j] + rWeight[i][j]:
                    img[:, :, 0][i][j] = 255
                    img[:, :, 1][i][j] = 255
                    img[:, :, 2][i][j] = 255
                else:
                    img[:, :, 0][i][j] = 0
                    img[:, :, 1][i][j] = 0
                    img[:, :, 2][i][j] = 0
            else:
                img[:, :, 1][i][j] = 0
                img[:, :, 2][i][j] = 0


# 形态学处理
def shapeProcess(img):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    dilated = cv2.dilate(img, kernel)
    return dilated


# 统一处理函数
def test(img, title):
    testImg = denoise(img)
    rgbProcess(testImg)
    weightProcess(testImg)
    (blue, green, red) = cv2.split(testImg)
    reded = denoise(red, 2)

    cv2.imshow(title, reded)
