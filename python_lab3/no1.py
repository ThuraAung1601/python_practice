score = eval(input("Enter a score: "))
if isinstance(score,int) or isinstance(score,float):
    if score >= 80 and score <= 100:
        grade = "A"
    elif score >= 70 and score < 80:
        grade = "B"
    elif score >= 60 and score < 70:
        grade = "C"
    elif score >= 50 and score < 60:
        grade = "D"
    elif score < 50 and score >= 0:
        grade = "F"
    else:
        grade = "Score should be in the range from 0 to 100."
else:
    print("Invalid. Score should be number.")
print("Your grade:" + grade)