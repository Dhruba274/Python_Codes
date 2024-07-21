import matplotlib.pyplot as plt

# Data
subjects = ['Math', 'Science', 'English', 'History', 'PE']
student_A = [85, 90, 92, 88, 95]
student_B = [88, 82, 85, 87, 90]

# Create figure and axes
fig, ax = plt.subplots()

# Create bar chart
ax.bar(subjects, student_A, label='Student A')
ax.bar(subjects, student_B, bottom=student_A, label='Student B')

# Add title and labels
ax.set_title('Marks of Two Students in 5 Subjects')
ax.set_xlabel('Subjects')
ax.set_ylabel('Marks')

ax.legend()

# Show plot
plt.show()