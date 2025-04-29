import cv2

def get_frame():
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)
    
    # Read a single frame from the camera
    ret, frame = cap.read()
    
    # Release the camera resource immediately after reading
    cap.release()
    
    # Return the frame if read was successful, else return None
    return frame if ret else None