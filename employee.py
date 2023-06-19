class Employee:
    em_Satus=[
        "permanent",
        "temporal"
    ]
   
    commision = 10
    def __init__(self, employee_name: str, employee_status: str,category: str,previous_category_salary=0, salary = 0):
        # assert employee_status != "permanent ",f"the stutus  schould be permanent or equal to 0"
        assert salary >= 0, f'"the salary is {salary} and it schould be grater or equal to 0"'
        self.__employee_name = employee_name
        self.__employee_status = employee_status
        self.__salary =  salary
        self.category = category
        self.previous_category_salary = previous_category_salary

        
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount: float):
        self.__salary = amount
    
    @property
    def employee_status(self):
        return self.__employee_status

    @employee_status.setter
    def employee_status(self, status: str):
        if status.lower() == Employee.em_Satus[0] or  status.lower() == Employee.em_Satus[1]:
            self.__employee_status =  status

    @property 
    def employee_name(self):
        return self.__employee_name

    @employee_name.setter
    def employee_name(self, name):
        self.__employee_name = name

    def newCategory_salary(self):
        pass

    def comulSalary(self):
        return self.salary
    
    def previousSalary(self):
        self.previous_category_salary = (self.comulSalary * self.commision)


# current salary =  oldSalary + comulSalary




