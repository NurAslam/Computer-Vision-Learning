# ================= MENAMPILKAN SATU FRAME ====================
import cv2
import numpy as np

# cap = cv2.VideoCapture('../../source/input1.mp4')

# # shi-Tomasi corner detection parameters
# feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7 )

# # Lucas-Kanada optical flow parameters
# lk_params = dict(winSize=(15,15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# # Ambil frame pertama
# ret, old_frame = cap.read()
# if not ret:
#     print('Gagal membaca frame pertama')
#     cap.release()
#     exit()

# # konversi ke grayscale
# old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# # deteksi sudut
# p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# # buat mask kosong untuk menggambar jejaknya
# mask = np.zeros_like(old_frame)

# # OUTPUT
# cv2.imshow('frame pertama (color)', old_frame)

# cv2.imshow('Grayscale Frame pertama', old_gray)

# # Sudut hasil Shi-Tomasi pada Frame pertama
# frame_with_corners = old_frame.copy()
# if p0 is not None:
#     for pt in p0:
#         x, y = pt.ravel()
#         cv2.circle(frame_with_corners, (int(x), int(y)), 5, (0, 255, 0), -1)
# cv2.imshow('Frame dengan sudut (corners)', frame_with_corners)

# cv2.imshow('Mask Kosong', mask)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ======================== LUKAS CANADE METHOD ===========================

cap = cv2.VideoCapture('../../source/input1.mp4')
# Shi-Tomasi corner detection parameters
feature_params = dict(maxCorners=90, qualityLevel=0.1, minDistance=10, blockSize=7)

# Lucas-Kanade optical flow parameters
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Read first frame and find initial points
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

# Create mask for drawing
mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculate Optical Flow
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    # Select good points
    if p1 is not None:
        good_new = p1[st == 1]
        good_old = p0[st == 1]

        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(mask, (int(a), int(b)), (int(c), int(d)), (0, 255, 0), 2)
            frame = cv2.circle(frame, (int(a), int(b)), 5, (0, 0, 255), -1)

        img = cv2.add(frame, mask)
        cv2.imshow("Lucas-Kanade Optical Flow", img)

        # Update for next iteration
        old_gray = frame_gray.copy()
        p0 = good_new.reshape(-1, 1, 2)

    if cv2.waitKey(1) & 0xFF == ord("q"):  # Press ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
