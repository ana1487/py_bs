
def from_base10(n, b):
    if b < 2:
        raise ValueError("Base must be >= 2")
    if n < 0: 
        raise ValueError("Number n should be >0")
    if n==0:
        return [0]

    digits = []
    while n > 0:
        n,m = divmod(n,b)
        digits.insert(0,m)        
    return digits

print(from_base10(0, 16))




