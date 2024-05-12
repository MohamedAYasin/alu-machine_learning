#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# Create a line plot
plt.plot(x, y1, linestyle='--', color="red", label='C-14')
plt.plot(x, y2, color="green", label='Ra-226')

# Set the y-axis range from 0 to 1
plt.ylim(0, 1)

# Optional: Add labels and title
plt.xlabel('Time (years)')  # Replace with your X-axis label
plt.ylabel('Fraction Remaining')  # Replace with your Y-axis label
plt.title('Exponential Decay of C-14')  # Replace with your title

# Add a legend in the upper right corner
plt.legend(loc='upper right')

# Display the plot
plt.show()
