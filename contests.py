class Customer:
    def __init__(self, name):
        self.name = name
        self.loan_amount = 0
        self.salary = 0

    def apply_loan(self, amount):
        self.loan_amount += amount
    
    def apply_salary(self,money):
        self.salary += money 

class Employee:
    def __init__(self, name):
        self.name = name
        self.position = ""
        self.salary = 0

# customers section
customer = Customer("Ali")
customer.apply_salary(4000)
customer.apply_loan(1000)
print(f"Customer salary: {customer.salary}")
print(f"Customer loan amount: {customer.loan_amount}")
# employees section
employee = Employee("mohamed")
employee.position = "Manager"
employee.salary = 5000
print(f"Employee position: {employee.position}")
print(f"Employee salary: {employee.salary}")