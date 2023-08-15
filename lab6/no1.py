def grader(mark):
    if mark >= 80 and mark <= 100: grade = "A"
    elif mark >= 70 and mark < 80: grade = "B"
    elif mark >= 60 and mark < 70: grade = "C"
    elif mark >= 50 and mark < 60: grade = "D"
    elif mark < 50: grade = "F"
    else: raise ValueError
    return grade

def main():
    score = eval(input("Enter the score (0-100): "))
    grade = grader(score)
    print(f"The grade is {grade}")

main()