import random

def is_obstacle_ahead():
    # Simulate reading from an ultrasonic sensor.
    # In a real robot, replace this with actual sensor input.
    return random.choice([False, False, False, True])  # 25% chance of obstacle ahead

def avoid():
    # Sequence of actions to avoid an obstacle
    print("Avoiding obstacle...")
    stop()         # Stop the robot
    turn_left()    # Turn left to change direction
    forward()      # Move forward a bit
    turn_right()   # Turn right to resume original direction

def stop():
    # Stop both motors
    set_speed(0, 0)

def forward():
    # Move forward with equal speed on both motors
    set_speed(50, 50)

def turn_left():
    # Rotate left by reversing left motor and forwarding right motor
    set_speed(-30, 30)

def turn_right():
    # Rotate right by forwarding left motor and reversing right motor
    set_speed(30, -30)

def set_speed(left, right):
    # Control motor speeds.
    # Replace this print with actual motor control commands for your hardware.
    print(f"Motors -> Left: {left}, Right: {right}")