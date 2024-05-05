# input
student_score = 80

# Process: Your Solution Code Here
def convert_to_grade(score):
    if score >= 80:
        return "A"
    elif score >= 65:
        return "B+"
    elif score >= 50:
        return "B"
    elif score >= 35:
        return "C"
    else:
        return "D"

# Output "Nilai A"
print("Nilai", convert_to_grade(student_score));