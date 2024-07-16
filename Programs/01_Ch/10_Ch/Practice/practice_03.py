# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 4

o = Demo()
print(o.a) # Print Class Attribute

o.a = 0  # Instance attribute is set

print(o.a) # Print Instance attribute because it is present
print(Demo.a)


# No Class Instance Is Not Change
