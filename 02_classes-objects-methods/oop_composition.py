# the term composition implies that the two objects are strongly linked, one object belongs exclusively to the other object.
# if the link between two objects is weaker and neither object has exclusive ownership of the other, it can also be called aggresation
class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.classes = []

    def enrol(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)

class department:
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {}

    def add_course(self, description, course_code, credits):
        self.courses[course_code] = Course(description, course_code, credits, self)
        return self.courses[course_code]

class Course:
    def __init__(self, description, course_code, credits, department):
        self.description = description
        self.course_code = course_code
        self.credits = credits
        self.department = department
        self.department.add_course(self)

        self.runnings = []

    def add_running(self, year):
        self.running.append(course_running(self, year))
        return self.runnings[-1]
class CourseRunning:
    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []

    def add_student(self, student):
        self.students.append(student)

maths_dept = department("Math and Applied Math", "MAM")
mam1000w = maths_dept.add_course("Mathematics 1000","MAM100W",1)
mam1000w_2013 = mam1000w.add_running(2013)
