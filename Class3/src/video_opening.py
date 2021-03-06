import cv2
import numpy as np

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    while(1):
        # get frame from camera
        ret, frame = cap.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # get image closing manually
        kernel = np.ones((10, 10), np.uint8)
        erosion = cv2.erode(img, kernel, iterations=1)
        dilation = cv2.dilate(dilation, kernel, iterations=1)

        # closing using cv2
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

        # show images
        cv2.imshow('Original image', img)
        cv2.imshow('Manual image', dilation)
        cv2.imshow('Autogenerated image', opening)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
