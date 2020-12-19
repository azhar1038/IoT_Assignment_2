n = list(filter(lambda x: x in ['2','3','5','7'], input("Enter number: ")))
print(sum(int(n[i])*int(n[i+1]) for i in range(0, len(n)-1)))