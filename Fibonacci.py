def fibonacci(n):
    fib_series = [0,1]

    for i in range(2,n):
        fib_series.append(fib_series[i-2]+ fib_series[i-1])

    return fib_series
    
total_fibo = int(input('Enter the number of Fibonacci Series to generate: '))
result = fibonacci(total_fibo)
print(result)
