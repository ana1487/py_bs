def sum_square_difference(n):
    # Calculate the sum of the squares of the first n natural numbers
    sum_of_squares = sum(i**2 for i in range(1, n+1))

    # Calculate the square of the sum of the first n natural numbers
    square_of_sum = sum(range(1, n+1)) ** 2

    # Find the difference
    difference = square_of_sum - sum_of_squares

    return difference

# Set n = 100
n = 100
result = sum_square_difference(n)

print(f"The difference between the sum of the squares and the square of the sum of the first {n} natural numbers is: {result}")
