def steer(correction):
    # Adjust motor speeds based on PID correction value
    base_speed = 50  # Base forward speed
    left = base_speed - correction   # Reduce speed on left to turn right
    right = base_speed + correction  # Increase speed on right to turn right
    set_speed(left, right)

def stop():
    # Stop both motors
    set_speed(0, 0)

def forward():
    # Move forward with equal speed on both motors
    set_speed(50, 50)

def search_for_line():
    # Rotate in place slowly to find the line
    # Typically used when line is lost
    set_speed(30, -30)

def set_speed(left, right):
    # Control motor speeds
    # Replace this with real motor control logic (e.g., GPIO, PWM)
    print(f"Motors -> Left: {left}, Right: {right}")