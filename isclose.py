from math import isclose

#learning to use isclose to check if the numbers are close to each other
# Making use of relative and absolute tolerance


a = 0.3
b = 0.1 + 0.1 + 0.1

print(a == b)
print(isclose(a, b))

# Use isclose method so that float numbers can be checked for equality

x = 10000.01
c = 10000.0102
y = 10000.02
z = 10001.01
print(isclose(x,y, rel_tol=0.01))
print(isclose(x,c, rel_tol=0.0001))

# we can use rel_tol and abs_tol to make the conditions for closeness of numbers

print(isclose(x,z))
