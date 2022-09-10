try:
    print("Packages are Installed")
    import cv2
    import numpy as np
except:
    print("ERROR::::Packages are not Installed")    
#we can  think as a creating a 512x512 boxes -> pixels
#if we want to give color functionality we need to give 3 channel
img = np.zeros((512,512, 3),np.uint8)
#print(img)
#The colon on the middle is limits the height and width of the image
#img[:] = 255 , 0, 0

#first Parenthes is starting point second paranthes is ending point
#third paranthes is colod end the finaly paranthes is thickness
cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)
#You can use cv2.filled or you can write any thickness you want
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
#30 is radius
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)
cv2.putText(img, " OPENCV ", (300,100), cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)