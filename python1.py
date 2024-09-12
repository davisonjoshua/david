
# Input the two numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Compare the numbers
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} and {b} are equal")


# Input the marks of the student
marks = []
subjects = int(input("Enter the number of subjects: "))

for i in range(subjects):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    marks.append(mark)

# Calculate total and average
total = sum(marks)
average = total / subjects

# Determine the grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Display the results
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)
