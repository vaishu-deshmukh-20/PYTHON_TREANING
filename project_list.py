students = ["Vaishnavi", "Vishranti", "Dipika", "Kailas"]
marks = [91, 87, 84, 89]
attendance = [95, 90, 88, 93]

notices = [
    "Python Internship started from 1st June 2026.",
    "Mini Project submission date is 20th June 2026.",
    "Unit Test will begin from next Monday.",
    "Attendance must be above 75%."
]


def student_login():
    name = input("Enter Student Name: ")
    for i in range(len(students)):

        if students[i].lower() == name.lower():

            print("\nLogin Successful")

            print("\n--- Student Details ---")
            print("Name :", students[i])
            print("Marks :", marks[i])
            print("Attendance :", attendance[i], "%")

            if marks[i] >= 90:
                print("Grade : A+")
            elif marks[i] >= 80:
                print("Grade : A")
            elif marks[i] >= 70:
                print("Grade : B")
            else:
                print("Grade : C")

            print("\n--- Notice Board ---")
            for notice in notices:
                print("#", notice)

            return

    print("Student Not Found")

student_login()
