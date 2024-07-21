import matplotlib.pyplot as plt
import numpy as np

# Generate random marks for two students for 6 unit tests
student1_marks = np.random.randint(0, 10, size=6)
student2_marks = np.random.randint(0, 10, size=6)

# Create a scatter plot to compare the results
plt.scatter(range(1, 7), student1_marks, label='Student 1')
plt.scatter(range(1, 7), student2_marks, label='Student 2')
plt.xlabel('Unit Test')
plt.ylabel('Marks (out of 10)')
plt.title('Comparison of Marks for Two Students')
plt.legend()
plt.show()