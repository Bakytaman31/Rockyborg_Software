def steer(correction):
    base_speed = 50
    left = base_speed - correction
    right = base_speed + correction
    set_speed(left, right)

def stop():
    set_speed(0, 0)

def forward():
    set_speed(50, 50)

def search_for_line():
    # Rotate or move forward slowly to search for line
    set_speed(30, -30)

def set_speed(left, right):
    print(f"Motors -> Left: {left}, Right: {right}")  # Replace with actual motor control logic