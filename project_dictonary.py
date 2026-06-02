# ==================================
#      COLLEGE SMART PORTAL
# ==================================

students = [
    {
        "id": 101,
        "name": "Vaishnavi",
        "course": "BCA",
        "marks": 91,
        "attendance": 95,
        "city": "Latur"
    },

    {
        "id": 102,
        "name": "Vishranti",
        "course": "BCA",
        "marks": 87,
        "attendance": 90,
        "city": "Pune"
    },

    {
        "id": 103,
        "name": "Dipika",
        "course": "BCA",
        "marks": 84,
        "attendance": 88,
        "city": "Nanded"
    },

    {
        "id": 104,
        "name": "Kailas",
        "course": "BCA",
        "marks": 89,
        "attendance": 93,
        "city": "Osmanabad"
    },

    {
        "id": 105,
        "name": "Ashwin",
        "course": "BCA",
        "marks": 94,
        "attendance": 97,
        "city": "Solapur"
    },

    {
        "id": 106,
        "name": "Neha",
        "course": "BCA",
        "marks": 78,
        "attendance": 85,
        "city": "Aurangabad"
    }
]

# Bonus Dictionary

college_info = {
    "college_name": "ABC College",
    "location": "Latur",
    "principal": "Dr. Patil",
    "department": "Computer Science",
    "total_students": 500
}

# Function

def get_status(marks):
    if marks >= 90:
        return "Excellent"
    elif marks >= 75:
        return "Good"
    else:
        return "Needs Improvement"


# College Information

print("=================================")
print("      COLLEGE SMART PORTAL")
print("=================================")

print("\nCollege Information")
print("College Name :", college_info["college_name"])
print("Location     :", college_info["location"])
print("Principal    :", college_info["principal"])

# Print All Records

print("\nStudent Records")

for student in students:

    print("\n--------------------------")
    print("ID         :", student["id"])
    print("Name       :", student["name"])
    print("Course     :", student["course"])
    print("Marks      :", student["marks"])
    print("Attendance :", student["attendance"], "%")
    print("City       :", student["city"])
    print("Status     :", get_status(student["marks"]))

# Challenge Function

def search_records(name):

    for student in students:

        if student["name"].lower() == name.lower():

            print("\nStudent Found")
            print("--------------------------")
            print("ID         :", student["id"])
            print("Name       :", student["name"])
            print("Course     :", student["course"])
            print("Marks      :", student["marks"])
            print("Attendance :", student["attendance"], "%")
            print("City       :", student["city"])
            return

    print("\nStudent Not Found")


# Search Option

search_name = input("\nEnter Student Name to Search : ")
search_records(search_name)