from math import factorial
x = int(input("Enter x: "))
n = int(input("Enter n: "))
print(sum([(-1)**i*x**j/factorial(j) for i,j in enumerate(range(1,n+1, 2))]))