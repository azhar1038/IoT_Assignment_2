def sieve_of_eratosthenes(start, end):
    prime = [True for i in range(end+1)]
    p=2
    while p*p <= end:
        if prime[p]: 
            for i in range(p*p, end+1, p): prime[i] = False
        p+=1
    for i in range(max(2, start), end+1):
        if prime[i]: print(i, end=", ")

sieve_of_eratosthenes(int(input("Enter starting number: ")), int(input("Enter ending number: ")))