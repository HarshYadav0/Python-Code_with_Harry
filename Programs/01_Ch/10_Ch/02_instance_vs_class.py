class Employee:
    language = 'python' #class attributes
    salary = 12000


harry = Employee()  
print(harry.salary, harry.language) 

harsh = Employee()  # Stored in Variable
harsh.language = 'Javascript' # Instance attribute (Preference First)
print( harsh.salary, harsh.language)