from permanent import Permanent_Employee
from employee import Employee

Employee_type = input("Enter the status of the employee ")

if Employee_type.lower() == "permanent":
    
    Employee_name = input("Enter the employee name: ")
    Eployee_status = input("Enter the employee status: ")
    category = input("Enter category ")
    salary = float(input("Enter salary "))
    work_days = int(input("Enter the working day "))
    fixe_salary = float(input("month salaey "))
    number_childrent = int(input("Enter number of childrent "))
    marital_status = bool(input("Marital status [True or False] "))
    month_bonus = int(input("Month bonus "))

    PermanentEp = Permanent_Employee(employee_name= Employee_name,
     employee_status= Employee_type, category= category, 
    salary= salary, working_day_InMonth= work_days,
    number_childrent= number_childrent, marital_status= marital_status, month_bonus= month_bonus)

    PermanentEp.Hire_Employee()

    print(f'"you want to add a "{Employee_type} " employee')
elif Employee_type.lower() == "temporal":
    print(f'"you want to add a "{Employee_type} " employee')
else:
    print("Category does not exist")



# Employee_type = input("Enter the status of the employee ")
# if Employee_type.lower() == "temporal":
#     print(f'"you want to add a "{Employee_type} " employee')
# elif Employee_type == "permanent":
#     print(f'"you want to add a "{Employee_type} " employee')
# else:
#     print("Category does not exist")

# # 1-add_employee
# # 2-Display_employee
# # 3-Dismiss_employee
# # 4-mute_employee
# # 0-Close_System
# # csv file