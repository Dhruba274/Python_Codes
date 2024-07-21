import matplotlib.pyplot as plt

# Data
subjects = ['Math', 'Science', 'English', 'History', 'PE']
student_A = [85, 90, 92, 88, 95]
student_B = [88, 82, 85, 87, 90]
plt.plot(subjects,student_A,marker="o",ms=10,mfc="red")
plt.plot(subjects,student_B,marker="o",ms=10,mfc="blue")
plt.title("Marks of two student")
plt.xlabel("Subjects")
plt.ylabel("marks")
plt.show()