# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer :
    company = "Microsoft"

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Harsh", 1200000, 456003)
print(p.name, p.salary, p.pin)

p = Programmer("Rohan", 105000, 433003)
print(p.name, p.salary, p.pin)

