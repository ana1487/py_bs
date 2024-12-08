#The prime factors of 13195 are 5, 7, 13 and 29.



def largest_prime_factor(n):
    # Initialize the largest prime factor
    largest_prime = -1
    
    # Divide out all factors of 2 first
    while n % 2 == 0:
        largest_prime = 2
        n = n // 2
    
    # Now check odd numbers up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n = n // i
    
    # If n is still greater than 2, it's prime itself
    if n > 2:
        largest_prime = n
    
    return largest_prime

# Test with the example from the problem
number = 13195
result = largest_prime_factor(number)
print(f"The largest prime factor of {number} is: {result}")

