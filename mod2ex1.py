x = input("enter a string: ")
y = ""
for i in range(len(x)):
    y = y + x[len(x)-i-1]

print(f"Reversed!: {y}")