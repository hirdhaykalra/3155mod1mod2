#Worked with Haley Siharath
x = []
for elem in range(int(input("Enter number of floats: "))):
    x.append(float(input(f"Enter number {elem+1}: ")))

total = 0
for elem in x:
    total = total + elem

print(f'average: {total/len(x)}')