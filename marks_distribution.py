#  Display the marks of two students for 5 subjects using suitable graphical tools.

import matplotlib.pyplot as plt

def display_student_marks(student1, student2, subjects):

    num_subjects = len(subjects)
    
    marks_student1 = [85, 90, 78, 92, 88]
    marks_student2 = [78, 85, 80, 88, 75]

    
    width = 0.35
    bar_positions_student1 = range(num_subjects)
    bar_positions_student2 = [pos + width for pos in bar_positions_student1]

    plt.bar(bar_positions_student1, marks_student1, width=0.35, label='Student 1')
    plt.bar(bar_positions_student2, marks_student2, width=0.35, label='Student 2')

    plt.xlabel('Subjects')
    plt.ylabel('Marks')
    plt.title('Marks of Students in 5 Subjects')
    plt.legend()

    
    plt.show()


subjects = ['Math', 'English', 'Science', 'History', 'Computer Science']
display_student_marks("Student 1", "Student 2", subjects)