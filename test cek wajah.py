import cv2
# memasukkan klasifikasi
# untuk bagian cv2.CascadeClassifier masukkan lokasi penyimpanan dari file 'haarcascade_frontalface_default.xml' dan 'haarcascade_eye.xml'
# untuk file frontalface dapat diunduh pada link berikut : https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# untuk file frontalface dapat diunduh pada link berikut : https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

face_cascade = cv2.CascadeClassifier(r'D:\SEMESTER 6\PENGOLAHAN CITRA\BELAJAR CV2\haarcascade_frontalface_default.xml') # untuk wajah
eyeDetector = cv2.CascadeClassifier(r'D:\SEMESTER 6\PENGOLAHAN CITRA\BELAJAR CV2\haarcascade_eye.xml') #untuk mata

# membuat perintah untuk kamera
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2) # dimana (B,G,R) : Blue, Green, Red (0,255,0) rentan nilai 0 - 255 menyatakan warna kotak
        roiAbuabu = gray[y:y+h,x:x+w]
        roiWarna = frame[y:y+h,x:x+w]
        mata = eyeDetector.detectMultiScale(roiAbuabu)
        for (xe,ye,we,he) in mata :
            cv2.rectangle(roiWarna,(xe,ye),(xe+we,ye+he),(0,0,255),1)
        
    cv2.imshow('deteksi wajah dan mata', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27 or key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
