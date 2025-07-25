# Dilate
import cv2
import numpy as np

image_read = cv2.imread('./test.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("treshold", image_read)

_,binary_image = cv2.threshold(image_read,127, 255, cv2.THRESH_BINARY)
print("treshold yg digunakan: ", _)

kernels = np.ones((5,5), dtype=np.uint8)

dilated_image = cv2.dilate(binary_image, kernels, iterations=1)

cv2.imshow('dilated image', dilated_image)


# Erode
eroded_image = cv2.erode(binary_image, kernels, iterations=1)
cv2.imshow('eroded image', eroded_image)


# Morphologi
morph_image = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernels)
cv2.imshow('morph image', morph_image)


# Morphologi
morph_gradient = cv2.morphologyEx(binary_image, cv2.MORPH_GRADIENT, kernels)
cv2.imshow('morph gradien image', morph_gradient)


cv2.waitKey(0)
cv2.destroyAllWindows()
