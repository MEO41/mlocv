try:
    import cv2
    import numpy as np
    print("Packages Imported")
except: 
    print("Packages Not Imported")   

img = cv2.imread("Resources/Me.jpg")
kernel = np.ones((5,5), np.uint8)
#cvtColor is changes images color
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#last two commas are let us play with edges
imgCanny = cv2.Canny(img, 100, 150)
#Dialation is making the canny image more thick
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("Gray Image", imgGray)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialeted Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)