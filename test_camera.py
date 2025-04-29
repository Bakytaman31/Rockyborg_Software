import cv2

# Try to open /dev/video0
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Failed to open camera!")
    exit()

print("✅ Camera opened successfully!")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to grab frame")
        break

    # Show the frame
    cv2.imshow("Camera Test", frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()