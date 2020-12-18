from math import factorial
x = int(input("Enter x: "))
n = int(input("Enter n: "))
print(1+sum([(-1)**(i+1)*x**i/factorial(i) for i in range(2,n+1)]))