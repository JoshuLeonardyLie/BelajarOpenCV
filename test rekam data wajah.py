import cv2, os

face_cascade = cv2.CascadeClassifier(r'D:\SEMESTER 6\PENGOLAHAN CITRA\BELAJAR CV2\haarcascade_frontalface_default.xml')
eyeDetector = cv2.CascadeClassifier(r'D:\SEMESTER 6\PENGOLAHAN CITRA\BELAJAR CV2\haarcascade_eye.xml')

wajahDir = (r'D:\SEMESTER 6\PENGOLAHAN CITRA\BELAJAR CV2\datawajah')
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceID = input("Masukkan Face ID yang akan direkam datanya[kemudian tekan ENTER] : ")
print("Tatap wajah anda ke depan dala webcam. Tunggu proses pengambilan data wajah selesai...")
ambilData = 1 

while True :
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces :
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,255), 2)
        namaFile = 'wajah.' + str(faceID)+ '.' + str(ambilData) +'.jpg'
        cv2.imwrite(wajahDir + '/' + namaFile, frame)
        ambilData += 1

        roiAbuAbu = gray[y:y+h,x:x+w]
        roiWarna = frame[y:y+h,x:x+w]
        mata = eyeDetector.detectMultiScale(roiAbuAbu)

        for (xe,ye,we,he) in mata :
            cv2.rectangle(roiWarna,(xe,ye),(xe+we, ye+he),(0,0,255),1)

    cv2.imshow('Webcamku', frame)
    k = cv2.waitKey(1) & 0xFF
    if  k == 27 or k == ord('q') :
        break
    elif ambilData>30:
        break

print('Pengambilan data selesai')
cam.release()
cv2.destroyAllWindows()