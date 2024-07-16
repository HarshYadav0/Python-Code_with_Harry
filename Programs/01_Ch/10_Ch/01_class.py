class Employee:
    language = 'python' #class attributes
    salary = 12000


harry = Employee()  # Stored in Variable
print(harry.salary, harry.language) 

harsh = Employee()  # Stored in Variable
harsh.name = 'Harsh' # Object/ Instance attribute
print(harsh.name, harry.salary, harry.language)

# Name is Object/Instance  attribute and Salary , Language are the class attributes