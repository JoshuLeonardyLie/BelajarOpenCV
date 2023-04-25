import cv2

#ini pilih salah satu
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #digunakan jika line 5 tidak bisa
cap = cv2.VideoCapture(0) 

if not cap.isOpened():
    print("Kamera tidak dapat dibuka")
else:
    print("Kamera berhasil dibuka")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Tidak dapat membaca frame dari kamera")
        break

    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): #tekan Q pada keyboard
        break

cap.release()
cv2.destroyAllWindows()
