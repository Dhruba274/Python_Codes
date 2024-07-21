import matplotlib.pyplot as plt
import numpy as np

# Define the range of x values
x = np.linspace(1, 100, 100)

# Define the y values for the O(n) curve
y_linear = x

# Define the y values for the O(n^2) curve
y_quadratic = x**2

# Create the plot
plt.plot(x, y_linear, label='O(n)')
plt.plot(x, y_quadratic, label='O(n^2)')

plt.legend()
plt.xlabel('n')
plt.ylabel('y')
plt.title('O(n) vs O(n^2)')

# Show the plot
plt.show()