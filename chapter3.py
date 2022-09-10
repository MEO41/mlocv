try:
    import cv2
    import numpy as np
    print("Packages Imported")
except: 
    print("ERROR::::Packages are not Imported")

img = cv2.imread("Resources/lambo.png")
print(img.shape)
#In opencv function width come first
imgResize = cv2.resize(img, (320,135))
#It matricies height comes first
imgCropped = img[0:100, 200:500]

cv2.imshow("image", img)
cv2.imshow("image Resize", imgResize)
cv2.imshow("image Cropped", imgCropped)

cv2.waitKey(0)