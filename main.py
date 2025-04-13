from control.pid import PID
import matplotlib.pyplot as plt
import time

# Инициализация PID
pid = PID(0.6, 0.1, 0.05)

# Искусственные значения "смещения от линии"
# Например: сначала отклонение вправо, потом влево, потом стабилизация
offsets = [5, 5, 5, 0, -5, -5, -5]

# Для записи результатов
corrections = []
times = []

# Симуляция
start_time = time.time()
for offset in offsets:
    correction = pid.update(offset)
    corrections.append(correction)
    times.append(time.time() - start_time)
    time.sleep(0.05)  # Имитация 20 Гц (50 мс шаг)

# Построение графика
plt.figure(figsize=(10, 5))
plt.plot(times, offsets, label="Offset (Error)", linestyle='--')
plt.plot(times, corrections, label="PID Correction", linewidth=2)
plt.title("PID Controller Response")
plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()