#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

#!/usr/bin/env python3

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Names for each of the 4 types of fruits
fruit_types = ['apples', 'bananas', 'oranges', 'peaches']

# Names for each of the 3 persons (e.g., years, regions)
persons = ['Farrah', 'Fred', 'Felicia']

# Bottom value for stacking
bottom_value = np.zeros(3)

# Specific colors for each fruit type
# Colors for apples, bananas, oranges, peaches
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Plotting each row of fruit as a stacked bar
for i, (fruits, label, color) in enumerate(zip(fruit, fruit_types, colors)):
    plt.bar(persons, fruits, label=label, color=color,
            width=0.5, bottom=bottom_value)
    bottom_value += fruits

# Setting y-axis limit
plt.ylim(0, 80)

# Adding legends, title, etc.
plt.xlabel('Persons')
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')
plt.legend()

# Display the plot
plt.show()
