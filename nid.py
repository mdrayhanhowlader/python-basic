publicList = [
    {"id_number": 12345678, "name": "Rayhan", "fathers name": "Adam", "mothers name": "Hawa", "age": 23, "permanent address": "Faridabad Dhaka 1204"},
    {"id_number": 23456789, "name": "Sara", "fathers name": "John", "mothers name": "Jane", "age": 30, "permanent address": "New York City"},
    {"id_number": 34567890, "name": "Alex", "fathers name": "Michael", "mothers name": "Emily", "age": 28, "permanent address": "Los Angeles"},
    {"id_number": 45678901, "name": "Eva", "fathers name": "Daniel", "mothers name": "Sophia", "age": 25, "permanent address": "Paris"},
    {"id_number": 56789012, "name": "Ryan", "fathers name": "Robert", "mothers name": "Mia", "age": 22, "permanent address": "London"},
    {"id_number": 67890123, "name": "Lily", "fathers name": "Christopher", "mothers name": "Olivia", "age": 26, "permanent address": "Berlin"},
    {"id_number": 78901234, "name": "Oscar", "fathers name": "William", "mothers name": "Emma", "age": 27, "permanent address": "Tokyo"},
    {"id_number": 89012345, "name": "Sophie", "fathers name": "Joseph", "mothers name": "Ava", "age": 24, "permanent address": "Sydney"},
    {"id_number": 90123456, "name": "Lucas", "fathers name": "Anthony", "mothers name": "Isabella", "age": 29, "permanent address": "Toronto"},
    {"id_number": 12345098, "name": "Ethan", "fathers name": "Andrew", "mothers name": "Sophie", "age": 31, "permanent address": "Singapore"},
    {"id_number": 23450987, "name": "Grace", "fathers name": "David", "mothers name": "Chloe", "age": 33, "permanent address": "Seoul"},
    {"id_number": 34509876, "name": "Mason", "fathers name": "Richard", "mothers name": "Ella", "age": 35, "permanent address": "Mumbai"},
    {"id_number": 45098765, "name": "Ava", "fathers name": "Matthew", "mothers name": "Madison", "age": 32, "permanent address": "Moscow"},
    {"id_number": 50987654, "name": "Logan", "fathers name": "Edward", "mothers name": "Lily", "age": 28, "permanent address": "Madrid"},
    {"id_number": 9876543, "name": "Chloe", "fathers name": "George", "mothers name": "Aria", "age": 30, "permanent address": "Melbourne"},
    {"id_number": 98765432, "name": "Noah", "fathers name": "Thomas", "mothers name": "Zoe", "age": 29, "permanent address": "New Delhi"},
    {"id_number": 87654321, "name": "Emma", "fathers name": "Peter", "mothers name": "Grace", "age": 27, "permanent address": "Cape Town"},
    {"id_number": 76543210, "name": "Oliver", "fathers name": "Brian", "mothers name": "Natalie", "age": 26, "permanent address": "Rio de Janeiro"},
    {"id_number": 65432109, "name": "Aiden", "fathers name": "Samuel", "mothers name": "Hannah", "age": 25, "permanent address": "Hong Kong"},
    {"id_number": 54321098, "name": "Isabella", "fathers name": "Frank", "mothers name": "Victoria", "age": 31, "permanent address": "Bangkok"}
]

person_id = int(input("Enter your NID number: "))
new_person = ""
old_person = f"Name: {new_person['name']} \nfathers name: {new_person['father']}"
for person in publicList:
    if person["id_number"] == person_id:
        new_person = person

print(new_person["name"])
