# Going to find the largest prime factor of a given number
# 600851475143




# The below method would make the computation too long, so checking a different method below
# number = int(input("Enter a number to see its prime factors: "))
# factors_list = []
# for i in range(1, number):
#     if number % i == 0:
#         factors_list.append(i)


# print(factors_list)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    


number = int(input("Enter a number to see its largest prime factor: "))
largest_prime_factor = 1

# We only need to check up to the square root of the number
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        # Check both the factor and its pair
        if is_prime(i):
            largest_prime_factor = max(largest_prime_factor, i)
        # Check the corresponding factor (number/i)
        if is_prime(number // i):
            largest_prime_factor = max(largest_prime_factor, number // i)

# Check if the number itself is prime
if is_prime(number):
    largest_prime_factor = number

print(f"The largest prime factor of {number} is: {largest_prime_factor}")