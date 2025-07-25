import cv2
import numpy as np

cap = cv2.VideoCapture('../source/video.mp4')

bgframe = None

while True:
    success, img = cap.read()

    if success:
        # resize
        img = cv2.resize(img, (600,500))
        # convert grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Gaussian Blur
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # set frame pertama sebagai background
        if bgframe is None:
            bgframe = gray.copy()
            continue #skip prosess pada frame pertama

        # menghitung perbedaan absolut antara bingkai latar belakang dan bingkai saat ini
        frameDelta = cv2.absdiff(bgframe, gray)
        cv2.imshow("Delta", frameDelta)


        # # Apply treshold to create a binary image
        _, tresh = cv2.threshold(frameDelta, 50, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        cv2.imshow("Treshold", tresh)

        # Dilate the treshold image to fill in samll holes
        tresh =  cv2.dilate(tresh, None, iterations=2)

        # Fin countours from the tresholded image
        contours, _ = cv2.findContours(tresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            

            # Filter out small and extremely large contours
            if 1500 < area < 50000:
                x, y, w, h = cv2.boundingRect(contour)

                # Draw a rectangle around deteced motion
                cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

                # Display motion detection label
                cv2.putText(img, "MOTION DETECTED", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,0,255))
        
        bgframe = cv2.addWeighted(bgframe, 0.7, gray, 0.3, 0)

        cv2.imshow("Original Video", tresh)
        cv2.imshow("Motion Detected Video", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()




# Optical Flow using 
# Ixu + Iyv + Lt=0 : Linear Equation, represent image gradient dan temporal gradient

# Ix and Iy are apstial image gradient
# It-is the temporal image gradient 
# u and v are the optical flow components (motion in x and y directions).

