from Pakistans_Functions import pakistans_functions as pf
import os
import json

class All_Students:
    def __init__(self, students):
        self.students = students

    def add_student(self):
        name = input("What is the name of the new student? ")

        ids = []
        for i in self.students: ids.append(i.stuID)

        while True:
            studentID = pf.idiot_proof_num_range("What is the students ID? ", 10000, 99999, "integer", "The ID must be 5-digit code")
            if studentID in ids: print("You already have a student with that ID")
            else: break

        self.students.append(Student(name, studentID, []))

    def print_students(self):
        print("| Name | ID | Avg | Grade |")
        for i in self.students: i.print_self()

    def print_specific_student(self):
        studentNameRef = {}
        for i in self.students:
            i.basic_print()
            studentNameRef[i.name] = i
        
        student = studentNameRef[pf.idiot_proof_specific("What student do you want examine (Enter Name)? ", list(studentNameRef.keys()))]
        student.print_self()

    def change_grade(self):
        studentIDRef = {}
        for i in self.students: 
            i.basic_print()
            studentIDRef[str(i.stuID)] = i

        newID = pf.idiot_proof_specific("What student do you want to change the grade of (enter ID) ", list(studentIDRef.keys()))
        studentIDRef[newID].change_grade()
    
    def new_grade(self):
        studentIDRef = {}
        for i in self.students: 
            i.basic_print()
            studentIDRef[str(i.stuID)] = i

        newID = pf.idiot_proof_specific("What student do you want to change the grade of (enter ID) ", list(studentIDRef.keys()))
        studentIDRef[newID].new_grade()

    def yoink_summary(self):
        totalGrade = 0
        for i in self.students:
            totalGrade += i.calc_average()

        grade = totalGrade / len(self.students)
        print(f"Average class grade: {grade} ({self.get_letter_grade(grade)})")


    def get_letter_grade(self, num):
        if self.grade >= 94: return "A"
        elif self.grade >= 90: return "A-"
        elif self.grade >= 87: return "B+"
        elif self.grade >= 83: return "B"
        elif self.grade >= 80: return "B-"
        elif self.grade >= 77: return "C+"
        elif self.grade >= 73: return "C"
        elif self.grade >= 70: return "C-"
        elif self.grade >= 67: return "D+"
        elif self.grade >= 63: return "D"
        elif self.grade >= 60: return "D-"
        else: return "F"


class Student:
    def __init__(self, name, stuID, classes):
        self.classes = classes
        self.name = name
        self.stuID = stuID

    def calc_average(self):
        totalGrade = 0
        for i in self.classes:
            totalGrade += i.grade

        if totalGrade != 0: return totalGrade / len(self.classes)
        else: return "Not enrolled in any classes"
    
    def get_letter_grade(self, grade):
        if self.grade >= 94: return "A"
        elif self.grade >= 90: return "A-"
        elif self.grade >= 87: return "B+"
        elif self.grade >= 83: return "B"
        elif self.grade >= 80: return "B-"
        elif self.grade >= 77: return "C+"
        elif self.grade >= 73: return "C"
        elif self.grade >= 70: return "C-"
        elif self.grade >= 67: return "D+"
        elif self.grade >= 63: return "D"
        elif self.grade >= 60: return "D-"
        else: return "F"

    def change_grade(self):
        classNameRef = {}
        for i in self.classes: 
            classNameRef[i.name] = i
            print(f"{i.name} (grade: {i.grade}%)")

        print(" ")
        if bool(self.classes):
            classToChange = pf.idiot_proof_specific("What classes grade do you want to change? ", list(classNameRef.keys()))
            newGrade = pf.idiot_proof_num_range(f"What grade would you like to set for {classToChange}? ", 0, 100)

            self.classes.remove(classNameRef[classToChange])
            self.classes.append(Class_Grade(newGrade, classToChange))

    def new_grade(self):
        newClass = input("What class do you want to add? ")
        newGrade = pf.idiot_proof_num_range("What grade do you want in this class? ", 0, 100)

        self.classes.append(Class_Grade(newGrade, newClass))


    def print_self(self):
        print(f"|{self.name}|{self.stuID}|{self.calc_average()}|{self.get_letter_grade()}|")

    def basic_print(self):
        print(f"{self.name} (ID: {self.stuID})")


class Class_Grade:
    def __init__(self, grade, name):
        self.grade = grade
        self.name = name      

def menu():
    daClass = load()

    while True:
        print("1. Add new student")
        print("2. Add grade to student")
        print("3. Change student grade")
        print("4. View student record")
        print("5. View all students")
        print("6. Class summary")
        print("7. Exit")
        print(" ")
        option = pf.idiot_proof_num_range("Type the number of the desired option: ", 1, 6)

        match option:
            case 1: daClass.add_student()
            case 2: daClass.new_grade()
            case 3: daClass.change_grade()
            case 4: daClass.print_specific_student()
            case 5: daClass.print_students()
            case 6: daClass.yoink_summary()
            case 7: break

        save(daClass.students)

def save(students):
    if os.path.isfile("Practices/Simple Grade Book/saver.json"):
        with open("Practices/Simple Grade Book/saver.json", "w") as file:
            studentsRaw = []
            for i in students:
                classes = []
                for i in classes:
                    classes.append(i.__dict__)

                studentDict = {
                    "name": i.name,
                    "id": i.stuID,
                    "classes" : classes
                }

                studentsRaw.append(studentDict)
            json.dump(studentsRaw, file, indent=4)

def load():
    if os.path.isfile("Practices/Simple Grade Book/saver.json"):
        allStudents = All_Students([])
        try:
            with open("Practices/Simple Grade Book/saver.json", "r") as jFile:
                students = []
                file = json.load(jFile)

                for i in file:
                    classes = []
                    for c in i["classes"]:
                        name = c["name"]
                        grade = c["grade"]
                        classes.append(Class_Grade(grade, name))

                    students.append(Student(i["name"], i["id"], classes))
                allStudents.students = students
                return allStudents
            
        except json.JSONDecodeError:
            return allStudents
            
    

menu()

