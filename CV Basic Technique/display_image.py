# import cv2
# import numpy as np

# url = 'https://cctvjss.jogjakota.go.id/atcs/ATCS_sentul.stream/playlist.m3u8'
# cap = cv2.VideoCapture(url)
# if not cap.isOpened():
#     print('Error', "tidak dapat membuka camera")
#     exit()

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     cv2.imshow("images", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()


# ambil gambar nya setiap frame
import cv2
import numpy as np
import os

if not os.path.exists('video_image'):
    os.mkdir('video_image')

url = 'https://cctvjss.jogjakota.go.id/atcs/ATCS_sentul.stream/playlist.m3u8'
cap = cv2.VideoCapture(url)
if not cap.isOpened():
    print('Error', "tidak dapat membuka camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("images", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
