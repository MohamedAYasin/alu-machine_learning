#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Create a line plot
plt.plot(x, y)

# Set the y-axis to logarithmic scale
plt.yscale('log')

# Optional: Add labels and title
plt.xlabel('Time (years)')  # Replace with your X-axis label
plt.ylabel('Fraction Remaining')  # Replace with your Y-axis label
plt.title('Exponential Decay of C-14')  # Replace with your title

# Display the plot
plt.show()
