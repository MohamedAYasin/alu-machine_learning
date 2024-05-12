mport numpy as np
import matplotlib.pyplot as plt

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x, y = np.random.multivariate_normal(mean, cov, 2000).T
y += 180

# Plotting x against y as a scatter plot
plt.scatter(x, y, color="magenta")

# Optional: Add labels and title
plt.xlabel('Height (in)')  # Replace with your X-axis label
plt.ylabel('Weight (lbs)')  # Replace with your Y-axis label
plt.title("Men's Height vs Weight")  # Replace with your title

# Optional: Customize the grid
plt.grid(True)

# Display the plot
plt.show()
