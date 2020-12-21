import cv2
import process as pro

img1 = cv2.imread("./img1.png")
img2 = cv2.imread("./img2.png")
img3 = cv2.imread("./img3.png")
img4 = cv2.imread("./img4.png")
img5 = cv2.imread("./img5.png")

cv2.imshow("img2src", img2)

# 去噪
testImg = pro.denoise(img2)
# rgb通道处理
pro.rgbProcess(testImg)
# 权重分配
pro.weightProcess(testImg)
# rgb通道分离
(blue, green, red) = cv2.split(testImg)
# 红色通道去噪
reded = pro.denoise(red, 2)
# 形态学——膨胀
# shapeImg=pro.shapeProcess(reded)

cv2.imshow("img2", reded)
# cv2.imshow("img2-shape", shapeImg)

# 测试其他用例
pro.test(img1, "img1")
pro.test(img3, "img3")
pro.test(img4, "img4")
pro.test(img5, "img5")

cv2.waitKey()
