#Worked with Haley Siharath
x = []
y = []
for elem in range(10):
    num = int(input('Enter a Number: '))
    if num in x:
        y.append(num)
    else:
        x.append(num)
    
for elem in y:
    if elem in x:
        x.remove(elem)

print(x)
