def sum_of_primes(limit):
    # Create a boolean array "prime[0..n]" and initialize all entries as true
    primes = [True] * limit
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit, i):
                primes[j] = False
    
    # Sum all prime numbers
    return sum(i for i, is_prime in enumerate(primes) if is_prime)

# Find the sum of all primes below 2 million
result = sum_of_primes(2000000)
print(f"The sum of all primes below two million is {result}")
