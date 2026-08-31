print("Student Grade Calculator")
print("------------------------")

name = input("Enter your name: ")

subjects = ["Mathematics", "Physics", "Chemistry"]
marks = []

for subject in subjects:
    mark = float(input(f"Enter your {subject} mark: "))
    marks.append(mark)

average = sum(marks) / len(marks)

if average >= 75:
    grade = "A"
elif average >= 65:
    grade = "B"
elif average >= 55:
    grade = "C"
elif average >= 45:
    grade = "S"
else:
    grade = "F"

print()
print("Result")
print("------")
print("Name:", name)
print("Average:", round(average, 2))
print("Grade:", grade)
