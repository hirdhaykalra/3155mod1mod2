#Worked with Haley Siharath
grade = int(input("Enter the grade, 0-100:"))
print(f'Your grade is {grade}')
if grade >= 90:
    print("you got a A")
elif grade >= 80:
    print("you got a B")
elif grade >= 70:
    print("you got C")
elif grade >= 60:
    print("you got D")
else:
    print("you just failed")
