def fibonacci(n):
    fib_series = [0,1]

    for i in range(2,n):
        fib_series.append(fib_series[i-2]+ fib_series[i-1])

    return fib_series
    
total_fibo = int(input('Enter the number of Fibonacci Series to generate: '))
fib_list = fibonacci(total_fibo)
print(fib_list)

# Upto 30th fibonacci number
# ... existing code ...

# Find pairs of consecutive Fibonacci numbers whose sum exceeds 1 million
# Find pairs of consecutive Fibonacci numbers whose sum is less than 1 million
new_list = []
max_sum = 0
max_pair = None

for i in range(len(fib_list)-1):
    current_sum = fib_list[i] + fib_list[i+1]
    
    if current_sum >= 1000000:
        break
        
    new_list.append(current_sum)
    if current_sum > max_sum:
        max_sum = current_sum
        max_pair = (fib_list[i], fib_list[i+1])

print("All sums:", new_list)
print(f"Largest sum under 1000000: {max_sum}")
print(f"Pair of the fibonacci numbers: {max_pair}")
   

    

