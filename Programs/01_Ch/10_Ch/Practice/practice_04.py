# Add a static method in problem 2, to greet the user with hello.

# Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class   Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n*self.n}")

    def cube(self):
        print(f"The cube of {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot of {self.n**1/2}")

    @staticmethod 
    def hello():
        print("Hello There !")

a = Calculator(3)

a.hello()
a.square()
a.cube()
a.squareroot()
