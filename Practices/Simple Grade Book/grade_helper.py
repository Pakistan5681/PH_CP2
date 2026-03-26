from Pakistans_Functions import pakistans_functions as pf

class All_Students:
    def __init__(self, students):
        self.students = students

    def add_student(self):
        name = input("What is the name of the new student? ")
        studentID = pf.idiot_proof_num_range("What is the students ID? ", 10000, 99999, "integer", "The ID must be 5-digit code")
        self.students.append(Student(name, studentID, []))

    def print_students(self):
        print("| Name | ID | Avg | Grade |")
        for i in self.students: i.print_self()

    def new_grade(self):
        for i in self.students: i.basic_print()


class Student:
    def __init__(self, name, stuID, classes):
        self.classes = classes
        self.name = name
        self.stuID = stuID

    def calc_average(self):
        totalGrade = 0
        for i in self.classes:
            totalGrade += i.grade

        return totalGrade / len(self.classes)
    
    def get_letter_grade(self):
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

    def add_grade(self, grade):
        self.classes.append(grade)

    def print_self(self):
        print(f"|{self.name}|{self.stuID}|{self.calc_average()}|{self.get_letter_grade(self.calc_average())}|")

    def basic_print(self):
        print(f"{self.name} (ID: {self.stuID})")


class Class_Grade:
    def __init__(self, grade, className):
        self.grade = grade
        self.className = className      

def main():
    while True:
        menu()

def menu():
    pass


