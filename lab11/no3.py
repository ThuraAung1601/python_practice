class Name:
    def __init__(self, t, f, l):
        self.title = t
        self.firstName = f
        self.lastName = l
    def setName(self, t, f, l):
        self.title = t
        self.firstName = f
        self.lastName = l
    def getName(self):
        return "{}. {} {}".format(self.title, self.firstName, self.lastName)

class Date:
    def __init__(self, day, month, year):
        if day > 31:
            month += day // 31
            day %= 31
        if month > 12:
            year += month // 12
            month %= 12
        self.day = day
        self.month = month
        self.year = year
    def setDate(self, day, month, year):
        if day > 31:
            month += day // 31
            day %= 31
        if month > 12:
            year += month // 12
            month %= 12
        self.day = day
        self.month = month
        self.year = year
    def getDate(self):
        return "{:02d}/{:02d}/{:02d}".format(self.day, self.month, self.year)
    def getBC(self):
        return "{:02d}/{:02d}/{:02d} BC".format(self.day, self.month, self.year+543)
    
# date = Date()
# date.setDate(1,2,2001)
# print(date.getDate())
# print(date.getBC())

# date.setDate(12,14,2001)
# print(date.getDate())
# print(date.getBC())

class Address:
    def __init__(self, house_no, city, distrinct, country):
        self.house_no = house_no
        self.city = city
        self.distrinct = distrinct
        self.country = country
    def setAddress(self, house_no, city, distrinct, country):
        self.house_no = house_no
        self.city = city
        self.distrinct = distrinct
        self.country = country
    def getAddress(self):
        return "No.{}, {}, {}, {}.".format(self.house_no, self.city, self.distrinct, self.country)
       
class Department:
    def __init__(self, description, employlist):
        self.description = description
        self.employlist = employlist
    def setDepartment(self, description, employlist):
        self.description = description
        self.employlist = employlist
    def addEmployee(self, employee):
        self.employlist.append[employee]
    def removeEmployee(self, employee):
        self.employlist.remove(employee)
    def setManager(self, manager):
        if isinstance(manager, PermEmployee):
            self.manager = manager
        else:
            print(f"{manager.name} is not in the permanent employee list.")
    def printInfo(self):
        result = ""
        i = 1
        for e in self.employlist:
            result += f"Employee {i}: {e.name}\n"
            i += 1
        return result

class Person:
    def __init__(self, name, birthdate, address):
        self.name = name
        self.birthdate = birthdate
        self.address = address
    def printInfo(self):
        return f"Name: {self.name}\nBirthday: {self.birthdate}\nAddress: {self.address}\n"

class Employee(Person):
    def __init__(self, name, birthdate, address, startDate, department):
        super().__init__(name, birthdate, address)
        self.startDate = startDate
        self.department = department
    def printInfo(self):
        return super().printInfo() + f"Start Date: {self.startDate}\nDepartment: {self.department}"

class TempEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, department, wage):
        super().__init__(name, birthdate, address, startDate, department)
        self.wage = wage
    def printInfo(self):
        return super().printInfo() + f"\nWage: {self.wage}"
        
class PermEmployee(Employee):
    def __init__(self, name, birthdate, address, startDate, department, salary):
        super().__init__(name, birthdate, address, startDate, department)
        self.salary = salary
    def printInfo(self):
        return super().printInfo() + f"\nSalary: {self.salary}"
    
name = Name("Mr", "John", "Walter")
name.setName("Mr", "John", "Walter")
p1Name = name.getName()
# print(p1Name)

bdate = Date(1,6,2001)
bdate.setDate(1,6,2001)
p1Bd = bdate.getDate() 
# print(p1Bd)

address = Address(408, "Latkrabang", "Bangkok", "Thailand")
address.setAddress(408, "Latkrabang", "Bangkok", "Thailand")
p1Address = address.getAddress()
# print(p1Address)

person1 = Person(p1Name, p1Bd, p1Address)
startDate = Date(1, 2, 2023)
startDate.setDate(1, 2, 2023)
day1 = startDate.getDate()

e1 = Employee(p1Name, p1Bd, p1Address, day1, "Software Engineering")
# print(employee1.printInfo())

employee1 = TempEmployee(p1Name, p1Bd, p1Address, day1, "Software Engineering", 35000)
print(employee1.printInfo())
print()
employee2 = PermEmployee("Mr. Albert Einstein", "03/12/1995", p1Address, day1, "Software Engineering", 95000)
print(employee2.printInfo())

employee3 = PermEmployee("Ms. Albert Einstein", "03/12/1995", p1Address, day1, "Software Engineering", 95000)
print(employee2.printInfo())

department = Department("Software Engr", [employee1, employee2, employee3])
department.printInfo()
department.setManager(employee2)
print(department.printInfo())
