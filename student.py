# student.py

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def get_student_id(self):
        return self.student_id

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_grade(self):
        return self.grade


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.get_student_id() == student_id:
                self.students.remove(student)
                break

    def get_student_by_id(self, student_id):
        for student in self.students:
            if student.get_student_id() == student_id:
                return student
        return None

    def get_all_students(self):
        return self.students


# 创建学生信息管理系统实例
sms = StudentManagementSystem()

# 添加学生
student1 = Student(1, "John Doe", 18, "Grade 12")
student2 = Student(2, "Jane Smith", 17, "Grade 11")

sms.add_student(student1)
sms.add_student(student2)

# 获取所有学生
all_students = sms.get_all_students()
for student in all_students:
    print("Student ID:", student.get_student_id())
    print("Name:", student.get_name())
    print("Age:", student.get_age())
    print("Grade:", student.get_grade())
    print()

# 删除学生
sms.remove_student(1)

# 再次获取所有学生
all_students = sms.get_all_students()
for student in all_students:
    print("Student ID:", student.get_student_id())
    print("Name:", student.get_name())
    print("Age:", student.get_age())
    print("Grade:", student.get_grade())
    print()
