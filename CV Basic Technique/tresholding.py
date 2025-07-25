# TRESHOLD
# import cv2

# image_read = cv2.imread('./test.jpeg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow("treshold", image_read)

# treshold = 127
# _, binary_image = cv2.threshold(image_read, treshold,255,cv2.THRESH_BINARY)

# cv2.imshow('binary image', binary_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# import cv2

# img = cv2.imread('test.jpeg', 0)
# _, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# # Kalau ingin tahu nilainya:
# threshold_value, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# print("Threshold yang digunakan:", threshold_value)

# ADAPTIVE TRESHHOLD
# import cv2

# image_read = cv2.imread('./test.jpeg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow("treshold", image_read)

# treshold = 127
# binary_image = cv2.adaptiveThreshold(image_read,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11,2)

# cv2.imshow('binary image', binary_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# OTSU
import cv2

image_read = cv2.imread('../source/download (1) copy.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("treshold", image_read)

_,binary_image = cv2.threshold(image_read,0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("treshold yg digunakan: ", _)
cv2.imshow('binary image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
