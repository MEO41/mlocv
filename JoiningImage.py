import cv2
import numpy as np

img = cv2.imread('Resources/Me.jpg')
#if we write np.vstack it will stack the images verticaly
imgHor = np.hstack((img,img))

cv2.imshow("Horizontal",imgHor)
cv2.waitKey(0)