import cv2
import numpy as np

class CameraProcessor:
    def __init__(self, source=0):
        """
        Initialize video capture.
        'source' can be:
            - 0 for webcam
            - 'test_videos/track2_video.mp4' for video file
        """
        self.cap = cv2.VideoCapture(source)
        self.cap.set(cv2.CAP_PROP_FPS, 30)  # Try to set 30 FPS

    def process_frame(self, frame):
        """
        Process a single video frame:
        - Detect lines
        - Return the frame with drawings and line center positions
        """
        # Step 1: Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Step 2: Apply Gaussian blur
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Step 3: Detect edges using Canny
        edges = cv2.Canny(blurred, 50, 150)

        # Step 4: Detect lines using Hough Transform
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=30, maxLineGap=10)

        line_positions = []

        if lines is not None:
            for line in lines:
                x1, y1, x2, y2 = line[0]
                # Calculate center point of the line
                line_center_x = (x1 + x2) // 2
                line_center_y = (y1 + y2) // 2

                # Draw the detected line (green)
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Draw center point (red)
                cv2.circle(frame, (line_center_x, line_center_y), 5, (0, 0, 255), -1)

                # Save the center position
                line_positions.append((line_center_x, line_center_y))

        return frame, line_positions

    def run(self):
        """
        Main loop to capture frames and process them.
        """
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            # Process the frame
            processed_frame, positions = self.process_frame(frame)

            # Display the frame
            cv2.imshow('Line Detection', processed_frame)

            # Print detected line centers
            print("Detected line centers:", positions)

            # Exit when 'q' key is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release everything when done
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Initialize processor with video file
    processor = CameraProcessor(source='test_videos/track2_video.mp4')
    processor.run()
