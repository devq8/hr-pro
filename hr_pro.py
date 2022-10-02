from datetime import date

class Employee:
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
    
    def get_working_years(self):
        return date.today().year - self.employment_year

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Salary: {self.salary} KD | Working Year: {self.get_working_years()}"

class Manager(Employee):
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage

    def get_bonus(self):
        return self.bonus_percentage * self.salary

    def __str__(self):
        return f"Name: {self.name} | Age: {self.age} | Salary: {self.salary} KD | Working Year: {self.get_working_years()} | Bouns: {(self.bonus_percentage/100) * self.salary}"

def main():

    print("\nWelcome to HR Pro 2019\n")

    employees = []
    managers = []

    employees.append(Employee("Khaled", 36, 1050, 2011))
    employees.append(Employee("Ali", 29, 950, 2018))
    employees.append(Employee("Mohammad", 40, 2500, 2006))
    managers.append(Manager("Ayman", 50, 4000, 2000, 10))
    managers.append(Manager("Naser", 55, 4700, 1995, 15))

    user_input = 0

    while user_input != 5 :
        print("Options:")
        print("1. Show Employees")
        print("2. Show Managers")
        print("3. Add An Employee")
        print("4. Add A Manager")
        print("5. Exit")
        user_input = int(input("\nWhat would you like to do? "))
        print("-----------------")

        if user_input == 1 :
            print("List of Employees")
            for employee in employees:
                print(employee)
            print("\n")

        if user_input == 2 :
            print("List of Managers")
            for manager in managers:
                print(manager)
            print("\n")

        if user_input == 3 :
            print("Add New Employee")
            employees.append(
                Employee(input("Name: "),int(input("Age: ")), int(input("Salary: ")), int(input("Employement year: ")))
            )
            print("\nEmployee added succesfully.\n")
            
        if user_input == 4 :
            print("Add New Manager")
            managers.append(
                Manager(input("Name: "),int(input("Age: ")), int(input("Salary: ")), int(input("Employement year: ")),float(input("Bouns Percentage: ")))
            )
            print("\nManager added succesfully.\n")
    quit()


if __name__ == '__main__':
	main()
