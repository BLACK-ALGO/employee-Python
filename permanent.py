import csv
from employee import Employee
    
class Permanent_Employee(Employee):
     
    # fixed_working_day = 20
    # perment_hourly_salary = 2500
    all = []
  
    def __init__(self, employee_name: str, employee_status: str, category: str, salary=0,
    working_day_InMonth = 0,previous_category_salary=0, number_childrent =0, marital_status = False , 
    month_bonus = 0.0):
        super().__init__(employee_name, employee_status,category, salary,previous_category_salary)
        self.__working_day_InMonth = working_day_InMonth
        self.__number_childrent = number_childrent
        self.marital_status = marital_status
        self.__month_bonus = month_bonus
        self.category = category
        self.previous_category_salary = previous_category_salary

        Permanent_Employee.all.append(self)

    # getter and setter for working day in manth
    @property
    def working_day_InMonth(self):
        return self.__working_day_InMonth
    
    @working_day_InMonth.setter
    def working_day_InMonth(self, work_day):
        self.__working_day_InMonth = work_day
    
    # getter and setter for fixed month salary
   
    def fixed_month_salary(self):
        return self.__salary
    
    

    # getter and setter for number of childrent
    @property
    def number_childrent(self):
        return self.__number_childrent
    
    @number_childrent.setter
    def fixed_month_salary(self, number_of_childrent):
        self.__number_childrent = number_of_childrent
    
    # getter and setter for number of month bonus
    @property
    def month_bonus(self):
        return self.__month_bonus
    
    @month_bonus.setter
    def month_bonus(self, bonus):
        self.__month_bonus = bonus
    


    # def daily_salary(self):
    #     return self.fixed_month_salary / Permanent_Employee.fixed_working_day

    # def monthly_salary(self):
    #     return self.daily_salary() * self.working_day_InMonth

    
    def comulSalary(self):
        return (self.fixed_working_day(self.fixed_month_salary + self.month_bonus))/20
    
    def previousSalary(self):
        self.previous_category_salary = (self.comulSalary * self.commision)
    
    def Hire_Employee(self):
    

        with open('permanentEp.csv', 'a+', newline='') as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
            self.employee_name ,
            self.employee_status,self.category,
            self.salary,
            self.__working_day_InMonth,
            self.fixed_month_salarys,
            self.previous_category_salary,
            self.__number_childrent,self.marital_status,
            self.__month_bonus
            ])
