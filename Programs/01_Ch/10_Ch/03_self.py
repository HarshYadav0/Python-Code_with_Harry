class Employee:
    language = 'python' #class attributes
    salary = 12000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee()  # Stored in Variable
harry.language = "Javascript"
print(harry.salary, harry.language) 

harry.getInfo()

