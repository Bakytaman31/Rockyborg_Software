import random

def is_obstacle_ahead():
    # Replace with actual ultrasonic sensor reading
    return random.choice([False, False, False, True])  # Simulated response

def avoid():
    print("Avoiding obstacle...")
    stop()
    turn_left()
    forward()
    turn_right()

def stop():
    set_speed(0, 0)

def forward():
    set_speed(50, 50)

def turn_left():
    set_speed(-30, 30)

def turn_right():
    set_speed(30, -30)

def set_speed(left, right):
    print(f"Motors -> Left: {left}, Right: {right}")  # Replace with actual motor control logic