def compute_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid input"
try:
    score = float(input("Enter the student's score: "))
    if 0 <= score <= 100:
        grade = compute_grade(score)
        print(f"The student's grade is: {grade}")
    else:
        print("Invalid score. Score should be between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a numeric score.")