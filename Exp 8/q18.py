students = {
    "student1": {"name": "John", "grades": [90, 85, 88, 92, 78], "attendance": [1, 1, 1, 0, 1]},
    "student2": {"name": "Jane", "grades": [78, 88, 90, 84, 76], "attendance": [1, 1, 0, 1, 1]},
    "student3": {"name": "Jim", "grades": [65, 70, 68, 72, 60], "attendance": [0, 1, 1, 1, 1]},
}

roll_numbers = {1: "John", 2: "Jane", 3: "Jim"}

# Calculate average of all marks
total_marks = sum(sum(student["grades"]) for student in students.values())
total_subjects = sum(len(student["grades"]) for student in students.values())
average_marks = total_marks / total_subjects
print(f"Average marks: {average_marks:.2f}")
