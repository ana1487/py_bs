# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two n-digit numbers.

def largest_palindrome_product(n):
    # Calculate range limits for n-digit numbers
    start = 10 ** (n-1)  # Lower bound (e.g., 10 for n=2)
    end = (10 ** n) - 1  # Upper bound (e.g., 99 for n=2)
    
    largest_palindrome = 0
    
    # Check all possible products of n-digit numbers
    for i in range(end, start-1, -1):
        for j in range(i, start-1, -1):
            product = i * j
            
            # If product is smaller than current largest palindrome, skip inner loop
            if product <= largest_palindrome:
                break
                
            # Convert to string to check if palindrome
            product_str = str(product)
            if product_str == product_str[::-1]:
                largest_palindrome = product
                
    return largest_palindrome

# Example usage:
# print(largest_palindrome_product(2))  # Should return 9009

print(largest_palindrome_product(6))  # For 3-digit numbers