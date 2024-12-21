import math

def count_divisors(n):
    """Count the number of divisors of a number."""
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 2  # i and n // i
            if i == n // i:  # If divisors are the same, count only once
                count -= 1
    return count

def find_triangle_number_with_divisors(min_divisors):
    """Find the first triangle number with more than min_divisors divisors."""
    triangle_number = 0
    n = 1

    while True:
        triangle_number += n
        n += 1
        if count_divisors(triangle_number) > min_divisors:
            return triangle_number

# Find the first triangle number with more than 500 divisors
result = find_triangle_number_with_divisors(500)
print("The first triangle number with over 500 divisors is:", result)
