fib = [0, 1]
[fib.append(fib[i-2]+fib[i-1]) for i in range(2, int(input("Enter N: ")))]
print(*fib, sep=", ")