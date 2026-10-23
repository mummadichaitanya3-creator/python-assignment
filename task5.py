# Student Marks Matrix Analysis

students = ["Arun", "Bala", "Charan", "Divya", "Eswar"]
subjects = ["Maths", "Physics", "Chemistry", "English"]

# Marks matrix: rows represent students, columns represent subjects
marks = [
    [85, 90, 78, 88],
    [70, 65, 72, 75],
    [95, 92, 96, 90],
    [60, 55, 58, 65],
    [80, 75, 82, 78]
]

# 1. Display the marks matrix
print("STUDENT MARKS MATRIX")
print("Student", *subjects)

for i in range(len(students)):
    print(students[i], *marks[i])

# 2. Calculate row-wise statistics
print("\nSTUDENT-WISE STATISTICS")

student_averages = []

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    highest = max(marks[i])
    lowest = min(marks[i])

    student_averages.append(average)

    print(f"{students[i]}: Total = {total}, "
          f"Average = {average:.2f}, "
          f"Highest = {highest}, Lowest = {lowest}")

# 3. Calculate column-wise statistics
print("\nSUBJECT-WISE STATISTICS")

subject_averages = []

for j in range(len(subjects)):
    column = [marks[i][j] for i in range(len(students))]

    total = sum(column)
    average = total / len(students)
    highest = max(column)
    lowest = min(column)

    subject_averages.append(average)

    print(f"{subjects[j]}: Total = {total}, "
          f"Average = {average:.2f}, "
          f"Highest = {highest}, Lowest = {lowest}")

# 4. Identify the top-performing student(s)
highest_average = max(student_averages)

print("\nTOP PERFORMER(S):")

for i in range(len(students)):
    if student_averages[i] == highest_average:
        print(f"{students[i]} with average {highest_average:.2f}")

# 5. Detect subjects with low average performance
threshold = 70

print(f"\nSUBJECTS WITH AVERAGE BELOW {threshold}:")

found = False

for j in range(len(subjects)):
    if subject_averages[j] < threshold:
        print(f"{subjects[j]}: Average = {subject_averages[j]:.2f}")
        found = True

if not found:
    print("No subjects have an average below the threshold.")

# 6. Find the overall class average
all_marks = [mark for row in marks for mark in row]
overall_average = sum(all_marks) / len(all_marks)

print(f"\nOverall Class Average: {overall_average:.2f}")