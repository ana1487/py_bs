# Main concept why floats are used.

# Do you think a = b?


a = 0.1 + 0.1 + 0.1 
b = 0.3

# Lets check

c = True if a == b else False
# What do you think c will be? False
print(c)

print(format(a, ".25f"))
print(format(b, ".25f"))

# Lets use round to round them up round(var, 1)
# Do you think a == b if we round them up?

c = True if round(a,1) == round(b,1) else False
# What do you think c will be? True
print(c)

print(format(round(a,1), ".1f"))
print(format(round(b,1), ".1f"))