class Employee:
    language = 'python' #class attributes
    salary = 12000

    def __init__(self, name, salary, language):  # Dunder Method Auto Call 
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object ")


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee('Harry', 12300, 'Javascript')  # Stored in Variable


print(harry.name,harry.salary, harry.language) 

harry.getInfo()

