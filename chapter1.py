try:
    print("Packages Importing...")
    import cv2
    print("Packages Imported")
except:
    print("Packages cannot imported")

cap = cv2.VideoCapture(0)
#define width
cap.set(3,640)
#define height
cap.set(4,480)
#change brightness
#3, 4, 10, is id for options like brightness or height of the frame
cap.set(10,100)

try:
    print("cam is opening..") 
    while True:
        success, img = cap.read()
   
        
        cv2.imshow("Video",img)
   
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except:
    print("cam did not opened")


 

