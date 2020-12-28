n = input("Enter a number: ")
evens = [int(i) for i in n if int(i)%2==0 and int(i)%4 != 0]
odds = [int(i) for i in n if int(i)%2!=0 and int(i)%3!=0]
print(sum(evens)/len(evens) - sum(odds)/len(odds))