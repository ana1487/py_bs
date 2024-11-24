import math
from fractions import Fraction

x = Fraction(2,4) * Fraction(3,8)


print(x.numerator)
print(x.denominator)

print("1 is numerator, 2 is denominator :", Fraction(1,2) )

print("2 is numerator, 1 is denominator :",Fraction(2,1))


print(Fraction( denominator= 11, numerator=12))
print(Fraction(numerator = 11, denominator=12))



upper_val = Fraction(11,23)
lower_val = Fraction(13,21)

print(upper_val.denominator)
print(upper_val.numerator)

print(lower_val.denominator)
print(lower_val.numerator)



x = Fraction(math.pi)


print(x)

print(float(x))

y = Fraction(math.sqrt(2))
print(float(y))


a = Fraction(1,8)
b = Fraction(3,10)


# print(format(a,'.5f'))
# print(format(b,'.5f'))

print(a)

print(b)

print(a.limit_denominator(10000))

print(b.limit_denominator(100))
