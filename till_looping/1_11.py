n = input("Enter a number: ")
evens = list(filter(lambda x: x in [0,4,8], map(int,n)))
odds = list(filter(lambda x: x in [1,5,9], map(int,n)))
print(sum([evens[i]*evens[i+1] for i in range(len(evens)-1)]) - sum([odds[i]*odds[i+1] for i in range(len(odds)-1)]))