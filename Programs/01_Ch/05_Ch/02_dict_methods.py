# KEys : Values

marks = {
    "Harsh" : 100,
    "Lokesh" : 76,
    "Harry": 55
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Harsh": 98, "Yogi" : 56})
print(marks)

print(marks.get("Harsh")) # prints none if not found
print(marks["Harry"]) # return an error if not present