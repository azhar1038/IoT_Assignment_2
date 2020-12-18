s = input("Enter a String: ")
print(''.join([s[0]]+[c if c!=s[0] else '$' for c in s[1:]]))