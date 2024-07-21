import matplotlib.pyplot as plt

# Sample data
marks = [85, 76, 92, 88, 78]
subject = "Math"

# Create a bar chart
plt.bar(subject, marks[0])
plt.bar(subject, marks[1], bottom=marks[0])
plt.bar(subject, marks[2], bottom=[x + y for x, y in zip(marks[:2], marks[1:])])
plt.bar(subject, marks[3], bottom=[x + y for x, y in zip(marks[:3], marks[2:])])
plt.bar(subject, marks[4], bottom=[x + y for x, y in zip(marks[:4], marks[3:])])

# Add labels and title
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Marks in " + subject)
plt.show()