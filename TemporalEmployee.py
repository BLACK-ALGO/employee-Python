from employee import Employee

class Temporal_Employee(Employee):
    temporal_hourly_salary = 1000
    
    def __init__(self, employee_name: str, employee_status: str,category: str, daily_working_hourMonth: float,
     dialy_hour_salary:float , salary=0):
        super().__init__(employee_name, employee_status,category, salary)
        self.daily_working_hourMonth = daily_working_hourMonth
        self.dialy_hour_salary = dialy_hour_salary

    
    def comulSalary(self):
        return self.dialy_hour_salary * self.daily_working_hourMonth

    def previousSalary(self):
        self.previous_category_salary = (self.comulSalary * self.commision)

