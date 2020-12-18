l = [int(input("Enter value_%2d: "%(i+1))) for i in range(20)]
evens = list(filter(lambda x: x%2==0 and x%4!=0, l))
odds = list(filter(lambda x: x%2!=0 and x%5!=0, l))
print(sum(evens)/len(evens) - sum(odds)/len(odds))