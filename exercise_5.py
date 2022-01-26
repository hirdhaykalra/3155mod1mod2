#Worked with Haley Siharath
x=[]
y=[]
for elem in range(5):
    x.append(int(input("enter a number for list 1: ")))

for elem in range(5):
    y.append(int(input("enter a number for list 2: ")))

z=[]

print(x)
print(y)

for elem in x:
    for elem2 in y:
        if elem == elem2 and elem not in z:
            z.append(elem)

print(z)