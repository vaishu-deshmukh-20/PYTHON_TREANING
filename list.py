#List - one variable with multiple values 
students = ["John", "Jane", "Doe", "Smith","vaishu"]
print(students)
print(students[0]) #accessing first element
print(students[1]) #accessing second element    
print(students[2]) #accessing third element
print(students[3]) #accessing fourth element
print(students[4]) #accessing last element

# Loop -to print all the element of the list
for student in students:
    print ("Hello {student})!Welcome to the class.")

    marks_list = [85,90,78,92,88]

    for mark in marks_list:
        if mark >= 90:
            print(f"Excellent! You scored {mark} .") 
        elif mark >= 80:
            print(f"Good job! You scored {mark}.")
        else:
            print (f"You scored {mark}. Keep trying to improve your grade.")



    for i in range (5):
        print (f"Line number {i}")


    
    # Defie function
    def greet(name):
        print(f"Hello {name}! Welcome to the programing world.")


    for student in students:
        greet(student)

    