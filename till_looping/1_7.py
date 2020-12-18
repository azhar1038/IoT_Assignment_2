n = input("Enter a number: ")
print(sum(int(n[i])*int(n[i+1]) for i in range(0, len(n)-1)))