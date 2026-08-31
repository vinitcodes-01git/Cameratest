import cv2 

cap = cv2.VideoCapture(0)

if not cap.isOpened():
   print("Could not access the camera")
   exit()

print("Camera opened Successfully")
print("Press Q to quit")

while True:
      success, frame = cap.read()
      
      if not success:
             print("Could not read camera frame")
             break

      frame = cv2.flip(frame, 1)
      cv2.imshow("Camera Test", frame)
      
      if cv2.waitKey(1) & 0xFF == ord("q"):
          break

cap.release()
cv2.destroyAllWindows()



