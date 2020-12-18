from collections import Counter
c = Counter([int(input("Enter value_%2d: "%(i+1))) for i in range(20)])
[print(k,"is repeated", c[k], "times") for k in c if c[k]>1]