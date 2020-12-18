from math import factorial
num = input("Enter a number: ")
x = sum([int(i) for i in num if i in ('0','4','6')])
n = sum([int(i) for i in num if i in ('5','7','9')])
print(sum([(-1)**i*x**j/factorial(j) for i,j in enumerate(range(1,n+1, 2))]))