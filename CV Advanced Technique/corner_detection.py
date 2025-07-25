import cv2
import numpy as np

image_read = cv2.imread('../CV Basic Technique/test.jpeg', cv2.IMREAD_GRAYSCALE)

gray = np.float32(image_read)

# 3. Deteksi sudut (corner) menggunakan metode Harris
corner = cv2.cornerHarris(gray, blockSize=3, ksize=3, k=0.04)
print("corner shape:", corner.shape)  # output: sama dengan (h, w)
print("corner max value:", corner.max())  # nilai maksimum sudut

# 4. Ubah gambar grayscale jadi BGR agar bisa ditandai warna
bgr_image = cv2.cvtColor(image_read, cv2.COLOR_GRAY2BGR)
print("bgr_image shape:", bgr_image.shape)  # output: (h, w, 3)

# 5. Tandai sudut yang terdeteksi dengan warna merah
bgr_image[corner>0.0001*corner.max()] = [0,0,255]
cv2.imshow("test", bgr_image)

cv2.waitKey(0)
cv2.destroyAllWindows()