import cv2

def get_line_offset(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Convert the image to binary (invert: line becomes white on black background)
    _, binary = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Find the largest contour (assumed to be the line)
        largest = max(contours, key=cv2.contourArea)
        
        # Compute the moments of the contour
        M = cv2.moments(largest)
        
        if M["m00"] != 0:
            # Calculate the x-coordinate of the contour's centroid
            cx = int(M["m10"] / M["m00"])
            
            # Calculate the offset from the center of the frame
            offset = cx - (frame.shape[1] // 2)
            return offset
    
    # If no contour is found, return None
    return None