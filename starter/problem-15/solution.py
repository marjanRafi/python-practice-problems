student_1 = [40, 35, 70, 90, 56]
student_2 = [57, 45, 80, 98, 46]

def check_average(marks):
    if any(mark < 40 for mark in marks):
        print("FAILED")
    else:
       
        average = sum(marks) / len(marks)
        print("Average Marks:", average)

print("Student 1:")
check_average(student_1)

print("\nStudent 2:")
check_average(student_2)
