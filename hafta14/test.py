import cv2  # opencv2 içe aktar

# Resmi içe aktar
# img = cv2.imread("logo.jpeg", cv2.IMREAD_COLOR)
# # renkli resim olarak içe aktar

# img = cv2.imread("logo.jpeg", cv2.IMREAD_GRAYSCALE)
# gri tonlamalı resim olarak içe aktar

# show red channel
# img = cv2.imread("logo.jpeg", cv2.IMREAD_COLOR)
# img[:, :, 2] = 0
# img[200:250, 200:250, 2] = 255  # blue
# img[:, :, 1] = 0  # green
# img[:, :, 0] = 0  # red

# binary image
# img = cv2.imread("logo.jpeg", cv2.IMREAD_GRAYSCALE)
# _, binary_img = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
# 125 altı 0, 125 üstü 255

# resize image
# binary_img = cv2.resize(binary_img, (400, 100))

# Resmi göster
# cv2.imshow("Logo", binary_img)
# cv2.waitKey(0)

# Kenarları belirleme (Canny kenar belirleme)
gray_image = cv2.imread("logo.jpeg", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(gray_image, 100, 200)

# Kenarları göster
cv2.imshow('Edges', edges)
cv2.waitKey(0)
