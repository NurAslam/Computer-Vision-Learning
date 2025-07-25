# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# image_read = cv2.imread('../CV Basic Technique/test.jpeg', cv2.IMREAD_GRAYSCALE)

# ksize = 31       # Ukuran kernel (harus ganjil), misalnya 31x31
# sigma = 5.0      # Standar deviasi Gaussian envelope
# theta = np.pi/4  # Arah orientasi filter (π/4 = 45°)
# lambd = 10       # Panjang gelombang sinus (jarak antar garis)
# gamma = 0.5      # Rasio aspek (0.5 artinya lebih ramping secara vertikal)
# psi = 0          # Fase offset dari gelombang sinus

# # Menghasilkan matriks kernel Gabor berukuran (31, 31). Ini adalah semacam filter detektor tekstur.
# gabor_kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, psi, ktype=cv2.CV_32F)

# # Menerapkan filter Gabor ke image_read dan menghasilkan gambar yang menonjolkan fitur-fitur sesuai arah theta.
# filtered_image = cv2.filter2D(image_read, cv2.CV_8UC3, gabor_kernel)

# print("Gabor kernel shape:", gabor_kernel.shape)
# print("Filtered image shape:", filtered_image.shape)
# print("Max kernel value:", np.max(gabor_kernel))

# plt.imshow(filtered_image, cmap='gray')
# plt.title("Gabor Kernel")
# plt.show()

# # percobaan setiap theta
# for theta in [0, np.pi/4, np.pi/2, 3*np.pi/4]:
#     kernel = cv2.getGaborKernel((ksize, ksize), sigma, theta, lambd, psi, ktype=cv2.CV_32F)
#     filtered = cv2.filter2D(image_read, cv2.CV_8UC3, kernel)
#     plt.imshow(filtered, cmap='gray')
#     plt.title(f"Gabor Filter (theta={theta:.2f} rad)")
#     plt.show()



import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import local_binary_pattern

image_read = cv2.imread('../CV Basic Technique/test.jpeg', cv2.IMREAD_GRAYSCALE)

radius = 10
n_points = 8*radius

lbp_image = local_binary_pattern(image_read,radius, n_points, method='uniform')

plt.imshow(lbp_image)
plt.title('Local Binary Pattern')
plt.show()

