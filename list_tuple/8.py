l = sorted([int(input("Enter value_%2d: "%(i+1))) for i in range(20)])
print("Largest:", *l[-1:-4:-1], "\nSmallest:", *l[:3])