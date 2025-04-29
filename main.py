from vision.camera import get_frame
from vision.line_detector import get_line_offset
from control.pid import PID
from control.motor_driver import steer, stop, forward
from control.obstacle_detector import is_obstacle_ahead, avoid
import time

# This code was meant for testing PID
# pid = PID(0.6, 0.1, 0.05)

# 
# 
# offsets = [random.uniform(-5, 5) for _ in range(60)]

# 
# corrections = []
# times = []

# 
# start_time = time.time()
# for offset in offsets:
#     correction = pid.update(offset)
#     corrections.append(correction)
#     times.append(time.time() - start_time)
#     time.sleep(0.05)  # Имитация 20 Гц (50 мс шаг)

# 
# plt.figure(figsize=(10, 5))
# plt.plot(times, offsets, label="Offset (Error)", linestyle='--')
# plt.plot(times, corrections, label="PID Correction", linewidth=2)
# plt.title("PID Controller Response")
# plt.xlabel("Time (s)")
# plt.ylabel("Value")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# Initialize PID controller
pid = PID(Kp=0.4, Ki=0.0, Kd=0.2)

# Start moving forward
forward()

try:
    while True:
        # Get a frame from the camera
        frame = get_frame()

        # Check for obstacles
        if is_obstacle_ahead():
            stop()
            avoid()
            forward()  # Move forward again after avoiding
            continue

        # Get line offset
        offset = get_line_offset(frame)

        if offset is not None:
            # Calculate correction using PID
            correction = pid.update(offset)

            # Apply correction to motors
            steer(correction)
        else:
            # If line is lost, you can define a strategy (optional)
            stop()
            print("Line lost! Stopping...")
            time.sleep(0.5)
            forward()

        time.sleep(0.05)  # 20 Hz control loop

except KeyboardInterrupt:
    # Stop motors safely if user interrupts
    stop()
    print("Program stopped.")