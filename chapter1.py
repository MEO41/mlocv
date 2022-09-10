from sre_constants import SUCCESS


try:
    print("Packages Importing...")
    import cv2
    print("Packages Imported")
except:
    print("Packages cannot imported")

cap = cv2.VideoCapture("Resources/meVid.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



 

