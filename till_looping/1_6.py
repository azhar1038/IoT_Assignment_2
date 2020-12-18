num = input("Enter a number: ")
k = int(input("Enter K: "))
print("\nFront:",num[k-1], "\nBack:",num[-k]) if k<len(num) else print("\nInvalid K")