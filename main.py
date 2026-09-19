# Student Course & Performance Management System :
students = []
def add_student():
  name = input("Enter your name : ")
  age = int(input("Enter your age : "))
  
  subjects = []
  marks = []
  
  n = int(input("How many subjects ? : "))
  for i in range(n):
    subject = input(f"Enter subject name : {i+1} : ")
    mark = int(input(f"Enter marks of {subject} :  "))
    
    subjects.append(subject)
    marks.append(mark)
    
  skills = []
  number_skills = int(input("How many skills ? : "))
  for i in range(number_skills):
    skill = input("Enter your skills : ")
    skills.append(skill)
    
  student = {
        "Name": name,
        "Age": age,
        "Subjects": subjects,
        "Marks": marks,
        "Skills": skills
    }
  students.append(student)
  print("Student added successfully")
  
  

def view_students():
  for student in students :
    print("Name:",student["Name"])
    print("Age :",student["Age"])
    print("Subjects :",student["Subjects"])
    print("Marks :",student["Marks"])
    print("Skills :",student["Skills"])

def search_student():
  
  name = input("Enter you name : ")
  for student in students:
    if name == student["Name"]:
      print("User found")
      return
  print("User not found")
    

def passed_students():
  for student in students:
    average = sum(student["Marks"])/len(student["Marks"])
    if average>= 40:
      print(student["Name"] , "Passed")
    else:
      print("Failed")

def top_performers():
    performers = [
      student["Name"] 
      for student in students 
      if sum(student["Marks"])/len(student["Marks"]) >=80
      ]
    print(performers)

def unique_skills():
  unique_skills = set()
  for student in students:
    unique_skills.update(student["Skills"])
  print(unique_skills)
    
def subject_analysis():
    subject_marks = {}

    for student in students:
        for subject, mark in zip(student["Subjects"], student["Marks"]):
            if subject not in subject_marks:
                subject_marks[subject] = []

            subject_marks[subject].append(mark)

    for subject, marks in subject_marks.items():
        average = sum(marks) / len(marks)
        print(subject, ":", average)
    
    

def delete_student():
  name = input("Enter your name : ")
  for student in students:
    if name == student["Name"]:
      students.remove(student)
      print("Student deleted")
      return
  print("Student not found")
while True:

  print("\n===== STUDENT MANAGEMENT SYSTEM =====")
  print("1. Add Student")
  print("2. View Students")
  print("3. Search Student")
  print("4. Passed Students")
  print("5. Top Performers")
  print("6. Unique Skills")
  print("7. Subject Analysis")
  print("8. Delete Student")
  print("9. Exit")

  choice = input("Enter your choice: ")

  if choice == "1":
    add_student()

  elif choice == "2":
    view_students()

  elif choice == "3":
    search_student()

  elif choice == "4":
    passed_students()

  elif choice == "5":
    top_performers()

  elif choice == "6":
    unique_skills()

  elif choice == "7":
    subject_analysis()

  elif choice == "8":
    delete_student()

  elif choice == "9":
    print("Thank you!")
    break

  else:
    print("Invalid choice!")
