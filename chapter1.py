try:
    print("Packages Importing...")
    import cv2
    print("Packages Imported")
except:
    print("Packages cannot imported")


img = cv2.imread("Resources/me.jpg")  

cv2.imshow("Output",img)
cv2.waitKey(0) & 0xFF == ord("q")

 

