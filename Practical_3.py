import cv2 as cv
cap = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
font = cv.FONT_HERSHEY_COMPLEX

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor = 1.1, minNeighbors = 5, minSize = (30,30))
    blurred_frame = cv.GaussianBlur(frame,(99,99),30)
    
    for(x,y,w,h) in faces:
        face_roi = frame[y:y+w, x:x+w]
        # blurred_face = cv.GaussianBlur(face_roi, (99,99), 30)
        
        # frame[y:y+w. x:x+w] = blurred_face
        blurred_frame[y:y+w, x:x+w] = face_roi
        
        cv.putText(blurred_frame,"Hacker detected!", (x,y), font, 1, (0,0,255), 2, cv.LINE_AA)
        # cv.circle(img, lacation, size(radius), colour, mode of fill)
        cv.circle(blurred_frame, ((x+(x+w))//2,(y+(y+h))//2), w//2, (0,0,255), 1)

    cv.imshow("My Face", blurred_frame)
    # cv.imshow("My Face - Gray",gray)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
