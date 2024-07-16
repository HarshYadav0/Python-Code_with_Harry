# Can we have a set with 18 (int) and '18' (str) as a value in it?

s = (18, "18")
print(s)

s2 = set()
s2.add(18)
s2.add("18")
print(s2)