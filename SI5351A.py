import time
import board
import busio
import matplotlib.pyplot as plt
import numpy as np
from adafruit_si5351 import SI5351

# Initialize I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize Si5351A
si5351 = SI5351(i2c)

# Set CLK0 to 8.8 MHz
si5351.clock_0.frequency = 8_800_000

# Set CLK1 to 14.175 MHz
si5351.clock_1.frequency = 14_175_000

# Set CLK2 to 60 MHz
si5351.clock_2.frequency = 60_000_000

# Set drive strength
si5351.clock_0.drive_strength = 8
si5351.clock_1.drive_strength = 8
si5351.clock_2.drive_strength = 8

# Enable all outputs
si5351.clock_0.enable = True
si5351.clock_1.enable = True
si5351.clock_2.enable = True

print("CLK0: 8.8 MHz, CLK1: 14.175 MHz, CLK2: 60 MHz set successfully!")

# Setup Matplotlib for real-time plotting
plt.ion()
fig, ax = plt.subplots()
x_data = np.linspace(0, 100, 100)  # Time axis (100 points)
y_data0 = np.zeros(100)  # Frequency data for CLK0
y_data1 = np.zeros(100)  # Frequency data for CLK1
y_data2 = np.zeros(100)  # Frequency data for CLK2

line0, = ax.plot(x_data, y_data0, label="CLK0 (8.8 MHz)")
line1, = ax.plot(x_data, y_data1, label="CLK1 (14.175 MHz)")
line2, = ax.plot(x_data, y_data2, label="CLK2 (60 MHz)")

ax.set_ylim(0, 65)  # Adjust range for frequencies up to 60 MHz
ax.set_xlabel("Time")
ax.set_ylabel("Frequency (MHz)")
ax.legend()

while True:
    # Read real-time frequency values from Si5351
    freq0 = si5351.clock_0.frequency / 1_000_000  # Convert Hz to MHz
    freq1 = si5351.clock_1.frequency / 1_000_000
    freq2 = si5351.clock_2.frequency / 1_000_000

    # Update data arrays
    y_data0 = np.append(y_data0[1:], freq0)
    y_data1 = np.append(y_data1[1:], freq1)
    y_data2 = np.append(y_data2[1:], freq2)

    # Update plot lines
    line0.set_ydata(y_data0)
    line1.set_ydata(y_data1)
    line2.set_ydata(y_data2)

    plt.draw()
    plt.pause(0.1)  # Update every 100ms
