def sum_square_difference(n):
    # Sum of the squares of the first n natural numbers
    sum_of_squares = sum(i**2 for i in range(1, n+1))
    
    # Square of the sum of the first n natural numbers
    square_of_sum = sum(range(1, n+1)) ** 2
    
    # Difference
    difference = square_of_sum - sum_of_squares
    
    return difference

# Set n = 100
n = 100
result = sum_square_difference(n)
print(f"The difference between the sum of squares and the square of the sum for the first {n} natural numbers is {result}.")
