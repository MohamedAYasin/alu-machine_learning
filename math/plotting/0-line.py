#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


y = np.arange(0, 11) ** 3

# Assuming you want to plot y against its index
x = np.arange(0, 11)

# Create the plot
plt.plot(x, y, color='red')

# Optional: Add labels and title
plt.xlabel('X axis label')  # Replace with your X-axis label
plt.ylabel('Y axis label')  # Replace with your Y-axis label
plt.title('Title of the Graph')  # Replace with your title

# Optional: Customize the grid
plt.grid(True)

# Display the plot
plt.show()

# your code here
