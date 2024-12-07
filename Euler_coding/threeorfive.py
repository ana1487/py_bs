# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below the provided parameter value number.

def multiplesOf3Or5(number):
    sum = 0
    # Loop from 1 to number-1
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# Test the function
print(multiplesOf3Or5(1000))