#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Assuming 'student_grades' is your data array
np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Define the bins for the histogram, where each bin corresponds to a range of 10 units
bins = np.arange(0, 101, 10)  # Bins from 0 to 100, with a step of 10

# Plot the histogram
plt.hist(student_grades, bins=bins, edgecolor='black')

# Set the title and labels
plt.title('Project A')
plt.xlabel('Grades')
plt.ylabel('Number of Students')

# Set the y-axis to range from 0 to 30
plt.ylim(0, 30)

# Set the x-axis ticks to be from 0 to 100, increasing by 10
plt.xticks(bins)

# Display the plot
plt.show()
