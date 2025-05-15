import RPi.GPIO as GPIO
import time

# Motor Pins (Example - Update as per your wiring)
LEFT_FORWARD = 17
LEFT_BACKWARD = 18
RIGHT_FORWARD = 22
RIGHT_BACKWARD = 23
LEFT_PWM = 24
RIGHT_PWM = 25

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    
    motor_pins = [LEFT_FORWARD, LEFT_BACKWARD, RIGHT_FORWARD, RIGHT_BACKWARD]
    for pin in motor_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    GPIO.setup(LEFT_PWM, GPIO.OUT)
    GPIO.setup(RIGHT_PWM, GPIO.OUT)

    left_pwm = GPIO.PWM(LEFT_PWM, 100)
    right_pwm = GPIO.PWM(RIGHT_PWM, 100)
    left_pwm.start(0)
    right_pwm.start(0)

    return left_pwm, right_pwm

def set_motor_speed(left_pwm, right_pwm, left_speed, right_speed):
    # speed: 0 to 100
    left_pwm.ChangeDutyCycle(abs(left_speed))
    right_pwm.ChangeDutyCycle(abs(right_speed))
    
    GPIO.output(LEFT_FORWARD, left_speed > 0)
    GPIO.output(LEFT_BACKWARD, left_speed < 0)
    GPIO.output(RIGHT_FORWARD, right_speed > 0)
    GPIO.output(RIGHT_BACKWARD, right_speed < 0)

def stop():
    GPIO.cleanup()