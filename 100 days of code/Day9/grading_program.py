student_scores={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Neville": 77,
    "Draco":68
    
}

student_grades={}

for key in student_scores.keys():
    if student_scores[key]>90:
        student_grades[key]="Outstanding"
    elif student_scores[key]>80:
        student_grades[key]="Exceeds Expectations"
    elif student_scores[key]>70:
        student_grades[key]="Acceptable"
    else:
        student_grades[key]="Fail"        

print(f"Following are the grades:  {student_grades}")