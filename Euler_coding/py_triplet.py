def find_pythagorean_triplet(sum_value):
    for a in range(1, sum_value // 3):
        for b in range(a, sum_value // 2):
            c = sum_value - a - b
            if a**2 + b**2 == c**2:
                return a, b, c, a * b * c

# Given sum of a, b, and c is 1000
a, b, c, product = find_pythagorean_triplet(1000)
print(f"The Pythagorean triplet is: a={a}, b={b}, c={c}")
print(f"The product abc is: {product}")
