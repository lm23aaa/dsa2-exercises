# 1. Syntax errors
# Reads your name and age
name = input("Enter your name: ")
age = input("Enter your age: ")
 
print("Your name is " + name + " and you are " + age + " years old.")

# 2. Unmatched data types
# Shows the first 10 multiples of a number
n = input("Enter a number: ")

print("The first 10 multiples of " + n + " are:")

for i in range(1, 11):
    print(str(i) + "x" + n + "= " + str(i * int(n)))

# 3. Null reference errors
# Splits a list into even and odd elements
data = [9,4,5,17,12,14,1,0,3,10,9]
odd = []
even = []

for i in range(0, len(data)):
    if data[i] % 2 == 0:
        # Found an even element
        even.append(data[i])
    else:
        # Found an odd element
        odd.append(data[i])

print("The even elements are: " + str(even))
print("The odd elements are: " + str(odd))

# 4. Classes
# Gets the student name by ID
class Student:
   def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

def find_student_by_id(students, search_id):
    for i in range(0, len(students)):
        if students[i].student_id == search_id:
            return students[i]
    
    return "-1"

students = [Student("Alice", 42), Student("Bob", 87)]
search_ids = [42, 5, 87]

for i in range(0, len(search_ids)):
    student = find_student_by_id(students, search_ids[i])
    if (student != "-1"):
        print("The student with id " + str(search_ids[i]) + " is " + student.name)
    else:
        print(f"Student with id {search_ids[i]} does not exist")


# 5. Multiple errors (one)
# Adds the first n numbers
n = input("Please enter a number: ")
i = 0
total = 0

while i < int(n):
    total = total + i
    i += 1

print("The total of the first " + n + " numbers is " + str(total))

# 5. Multiple errors (two)
# Adds the first n numbers
n = input("Please enter a number: ")
total = 0

for i in range(0, int(n)):
    total = total + i

print("The total of the first " + n + " numbers is " + str(total))