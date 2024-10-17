name = input("Enter your full name here:")
section = input("Enter your section here:")

prelims = float(input("Enter prelims grades:"))

if prelims < 40 or prelims > 100:
    print("Invalid grades! Grades must be between 40 and 100!")
else:
    midterms = float(input("Enter midterms grades:"))
if midterms < 40 or midterms > 100:
    print("Invalid grades! Grades must be between 40 and 100!")
else:
    finals = float(input("Enter finals grades:"))
if finals < 40 or finals > 100:
    print("Invalid grades! Grades must be between 40 and 100!")
else:
    prelims_2 = prelims * 0.3333
    midterms_2 = midterms * 0.3333
    finals_2 = finals * 0.3333
    final_grades = prelims_2 + midterms_2 + finals_2
    final_grades = round(final_grades)
    
    print("Hello Mr/Ms.", name, "you have a average final grade of", final_grades,)
    
if 99 <= final_grades <= 100:
    print(" a GPA of 1.00, Congratulations!")
elif 96 <= final_grades <= 98:
    print(" a GPA of 1.25, Congratulations!")
elif 93 <= final_grades <= 95:
    print(" a GPA of 1.50, Congratulations!")
elif 90 <= final_grades <= 92:
    print(" a GPA of 1.75, Congratulations!")
elif 87 <= final_grades <= 89:
    print(" a GPA of 2.00, Good Job!")
elif 84 <= final_grades <= 86:
    print(" a GPA of 2.25, Good Job!")
elif 81 <= final_grades <= 83:
    print(" a GPA of 2.50, Good Job!")
elif 78 <= final_grades <= 80:
    print(" a GPA of 2.75, Good Job!")
elif 75 <= final_grades <= 77:
    print(" a GPA of 3.00, You passed!")
else:
    print("Your grade is below 75, you failed. Better luck next time")

