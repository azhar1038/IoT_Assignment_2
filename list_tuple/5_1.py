s = input("Enter a String: ")
if len(s) < 3: print(s)
elif not s.endswith('ing'): print(s+'ing')
else: print(s+'ly')