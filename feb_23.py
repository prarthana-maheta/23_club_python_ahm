# OOP

# 1. class and objects
# 2. inheritance
# 3. abstraction
# 4. polymorphism
# 5. encapsulation

# functuon--in buit function
# len(),print(),def examp-le()
# instance
# class ExamplePrac:

#     msg="hello from class"

#     def display(self):
#         print(self.msg)
#         return "hello from method display"
    
# ex = ExamplePrac()
# print(ex.msg)
# print(ex.display())

class Student:
    student_dict={
        "deep":False,
        "vedant": False,
        "kunj":False
    }

    def take_attendance(self,name):
        if name in self.student_dict.keys():
            self.student_dict[name]=True
    
    def show_attendance(self):
        return self.student_dict
    
student = Student()
student.take_attendance(input("enter student name"))
print(student.show_attendance())