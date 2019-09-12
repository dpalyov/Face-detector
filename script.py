import cv2

def detectAndDisplay(frame):
    frame_grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame_grey = cv2.equalizeHist(frame_grey)

    classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = classifier.detectMultiScale(frame_grey)

    for x,y,w,h in faces:
        center = (x - w//2, y - h//2)
        axes = (w//2, h//2)
        ellipse_color = (255,0,255)
        frame = cv2.ellipse(frame,center,axes,0,0,360,ellipse_color,4)

    cv2.imshow('Capture',frame)

 
cap = cv2.VideoCapture(0)

if not cap.isOpened: 
      print('--(!)Error opening video capture')
      exit(0)

while True:
    capture, frame = cap.read()
    if frame is None: 
         print('--(!) No captured frame -- Break!')
         break

    detectAndDisplay(frame)

    if cv2.waitKey(10) == 27:
        break
