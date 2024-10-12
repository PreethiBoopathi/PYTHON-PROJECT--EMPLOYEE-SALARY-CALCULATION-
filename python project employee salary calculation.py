
class SalaryCalculator:
    def __init__(self, name, bp, da_percent=0.4, hra_percent=0.3, ta_percent=0.1, tax_percent=0.15):
        self.name = name
        self.bp = bp
        self.da_percent = da_percent
        self.hra_percent = hra_percent
        self.ta_percent = ta_percent
        self.tax_percent = tax_percent

    def calculate_allowances(self):
        da = self.bp * self.da_percent
        hra = self.bp * self.hra_percent
        ta = self.bp * self.ta_percent
        return da, hra, ta

    def calculate_gross_salary(self, da, hra, ta):
        return self.bp + da + hra + ta

    def calculate_tax(self, gross_salary):
        return gross_salary * self.tax_percent

    def calculate_total_salary(self, gross_salary, tax):
        return gross_salary - tax

    def calculate_salary(self):
        da, hra, ta = self.calculate_allowances()
        gross_salary = self.calculate_gross_salary(da, hra, ta)
        tax = self.calculate_tax(gross_salary)
        total_salary = self.calculate_total_salary(gross_salary, tax)
        return {
                        "Name": self.name,
            "Basic Pay": self.bp,
            "Dearness Allowance (DA)": da,
            "House Rent Allowance (HRA)": hra,
            "Travel Allowance (TA)": ta,
            "Gross Salary": gross_salary,
            "Tax": tax,
            "Total Salary": total_salary
        }


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    # Here you can implement your authentication logic
    # For simplicity, let's assume any username and password combination is valid
    return True


def logout():
    print("Logged out successfully.")
def main():
    if login():
        employees = {
            "Preethi": 50000,
            "Vinitha": 55000,
            "Sneha": 60000,
            "Hassani": 52000,
            "Mirnalini": 58000
        }
        employee_name = input("Enter employee's name: ")
        if employee_name in employees:
            basic_pay = employees[employee_name]
            calculator = SalaryCalculator(employee_name, basic_pay)
            salary_details = calculator.calculate_salary()
            for key, value in salary_details.items():
                print(f"{key}: {value}")
        else:
            print("Employee not found.")
        logout()
    else:
        print("Invalid username or password.")


if __name__ == "__main__":
    main()
//OUTPUT
Enter username: admin
Enter password: admin
Enter employee's name: Preethi
Name: Preethi
Basic Pay: 50000
Dearness Allowance (DA): 20000.0
House Rent Allowance (HRA): 15000.0
Travel Allowance (TA): 5000.0
Gross Salary: 90000.0
Tax: 13500.0
Total Salary: 76500.0
Logged out successfully.

Enter username: admin
Enter password: admin
Enter employee's name: Vinitha
Name: Vinitha
Basic Pay: 55000
Dearness Allowance (DA): 22000.0
House Rent Allowance (HRA): 16500.0
Travel Allowance (TA): 5500.0
Gross Salary: 99000.0
Tax: 14850.0
Total Salary: 84150.0
Logged out successfully.


Enter username: admin
Enter password: admin
Enter employee's name: Hassani
Name: Hassani
Basic Pay: 52000
Dearness Allowance (DA): 20800.0
House Rent Allowance (HRA): 15600.0
Travel Allowance (TA): 5200.0
Gross Salary: 93600.0
Tax: 14040.0
Total Salary: 79560.0
Logged out successfully.

Enter username: admin
Enter password: admin
Enter employee's name: Sneha
Name: Sneha
Basic Pay: 60000
Dearness Allowance (DA): 24000.0
House Rent Allowance (HRA): 18000.0
Travel Allowance (TA): 6000.0
Gross Salary: 108000.0
Tax: 16200.0
Total Salary: 91800.0
Logged out successfully.

Enter username: admin
Enter password: admin
Enter employee's name: Mirnalini
Name: Mirnalini
Basic Pay: 58000
Dearness Allowance (DA): 23200.0
House Rent Allowance (HRA): 17400.0
Travel Allowance (TA): 5800.0
Gross Salary: 104400.0
Tax: 15660.0
Total Salary: 88740.0
Logged out successfully.


Enter username: admin
Enter password: admin
Enter employee's name: aaaaaaaaaaaaaaaaa
Employee not found.
Logged out successfully.
