students = [
    {"name": "shibir", "roll": 1}, 
    {"name": "ismal vai", "roll": 2}, 
    {"name": "omayer vai", "roll": 3}, 
    {"name": "rayhan", "roll": 4}, 

]

studentName = str(input("Enter Student Name: "))
for student in students:
    if studentName == student["name"]:
        print(f"Name:{studentName.capitalize()} \nRoll: {student['roll']}")