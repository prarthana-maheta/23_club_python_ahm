# class Employee:

#     def __init__(self,name):
#         self.name=name
#         self.ename={
#             1:'deep',
#             2:'yesha',
#             3:"diya"
#         }

#         self.esalary={
#             1:2000,
#             2:7000,
#             3:8000,
#         }
#         self.output={}

#     def calculate(self):
#         print(self.name)
#         for k,v in self.esalary.items():
#             if v > 5000:
#                 self.output.update({self.ename[k]:v})
#         return self.output
    
#     def __call__(self):
#         return "hello obj"
        
# obj = Employee('royal')
# print(obj())
# print(obj.calculate())




# Write a Python class Employee 
# with attributes like 
#     # emp_id, 
#     # emp_name,
#     # emp_salary, and
#     # emp_department and 
#     methods like 
#     calculate_emp_salary, 
#     emp_assign_department, 
#     and print_employee_details.
# Sample Employee Data:
# "ADAMS", "E7876", 50000, "ACCOUNTING"
# "JONES", "E7499", 45000, "RESEARCH"
# "MARTIN", "E7900", 50000, "SALES"
# "SMITH", "E7698", 55000, "OPERATIONS"
# Use 'assign_department' method to change the department of an employee.
# Use 'print_employee_details' method to print the details of an employee.
# Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
# overtime = hours_worked - 50
# Overtime amount = (overtime * (salary / 50))

class Emplyee:
    dict1, dict2, dict3

    def  assign(self,emp_id,dept):
        if emp_id in dict3.keys():
            dict3.update({emp_id:dept})

    def show(self,emp_id):
        name = dict1.get(emp_id)
        salary = dict2.get(emp_id)

    def overtime(self,emp_id,hours):
        ot = hours-50
        amount=(ot * (dict2.get(emp_id)/50))
        return amount

