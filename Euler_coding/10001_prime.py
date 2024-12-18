def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_nth_prime(n):
    """Find the nth prime number."""
    prime_count = 0
    number = 1
    while prime_count < n:
        number += 1
        if is_prime(number):
            prime_count += 1
    return number

# Find the 10,001st prime number
nth_prime = 10001
result = find_nth_prime(nth_prime)
print(f"The {nth_prime}st prime number is {result}")
