import time

class PID:
    def init(self, Kp, Ki, Kd):
        # Initialize PID coefficients
        self.Kp = Kp  # Proportional gain
        self.Ki = Ki  # Integral gain
        self.Kd = Kd  # Derivative gain

        # Initialize state variables
        self.last_error = 0.0       # Last error value
        self.integral = 0.0         # Integral of the error
        self.last_time = None       # Last time update was called

    def update(self, error):
        current_time = time.time()  # Get current time in seconds

        if self.last_time is None:
            # First update call, assume small delta time
            delta_time = 0.05       # Assume 50 ms as default time step
            delta_error = 0.0       # No previous error to compare with
        else:
            # Compute time and error differences
            delta_time = current_time - self.last_time
            delta_error = error - self.last_error

            # Protect against division by zero or negative time intervals
            if delta_time <= 0:
                delta_time = 1e-16

        # Accumulate the integral term
        self.integral += error * delta_time

        # Compute the derivative term
        derivative = delta_error / delta_time

        # Compute the PID output
        output = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)

        # Debug output for monitoring internal state
        print(f"[PID] error={error:.2f}, dt={delta_time:.4f}, "
              f"integral={self.integral:.2f}, derivative={derivative:.2f}, output={output:.2f}")

        # Update state for next iteration
        self.last_error = error
        self.last_time = current_time

        return output