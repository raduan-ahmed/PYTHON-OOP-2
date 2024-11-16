class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

# PermanentEmployee Derived Class
class PermanentEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

# ContractEmployee Derived Class
class ContractEmployee(Employee):
    def __init__(self, name, emp_id, hourly_rate, hours_worked):
        super().__init__(name, emp_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

# Test Data
permanent_emp = PermanentEmployee("Alice", 1, 3000)
contract_emp = ContractEmployee("Bob", 2, 50, 160)

# Demonstration

print(permanent_emp.name, permanent_emp.emp_id, permanent_emp.calculate_salary())
print(contract_emp.name, contract_emp.emp_id, contract_emp.calculate_salary())

#print(f"{permanent_emp.name} (ID: {permanent_emp.emp_id}) Salary: ${permanent_emp.calculate_salary()}")
#print(f"{contract_emp.name} (ID: {contract_emp.emp_id}) Salary: ${contract_emp.calculate_salary()}")
