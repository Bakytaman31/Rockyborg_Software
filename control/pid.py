# control/pid.py

import time

class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd

        self.last_error = 0.0
        self.integral = 0.0
        self.last_time = None  # None для обработки первого вызова

    def update(self, error):
        current_time = time.time()

        if self.last_time is None:
            delta_time = 0.05  # предположим, что 1-й шаг = 50 мс
            delta_error = 0.0
        else:
            delta_time = current_time - self.last_time
            delta_error = error - self.last_error
            if delta_time <= 0:
                delta_time = 1e-16  # защита от деления на ноль

        # Интегральная составляющая
        self.integral += error * delta_time

        # Дифференциальная составляющая
        derivative = delta_error / delta_time

        # Итоговое значение PID
        output = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * derivative)

        # Отладочный вывод
        print(f"[PID] error={error:.2f}, dt={delta_time:.4f}, "
              f"integral={self.integral:.2f}, derivative={derivative:.2f}, output={output:.2f}")

        # Обновление состояний
        self.last_error = error
        self.last_time = current_time

        return output