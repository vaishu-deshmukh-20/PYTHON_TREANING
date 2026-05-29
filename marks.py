sub1 = int(input("Enter subject 1 marks:"))
sub2 = int(input("Enter subject 2 marks:"))
sub3 = int(input("Enter subject 3 marks:"))
sub4 = int(input("Enter subject 4 marks:"))
sub5 = int(input("Enter subject 5 marks:"))
 
total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total/5

print("Your total marks are:",total)
print("Your percentage is:",percentage)

if percentage >= 75:
    print("Result = First Class with Distinction")
elif percentage >= 60:
    print("Result = First Class")
elif percentage >= 45:
    print("Result = Pass")
else:
    print("Result = Fail")

