#Worked with Haley Siharath
x = input('enter a string: ')

list1 = []
list2 = []
for elem in range(len(x)):
    if(len(list1) == 2 or elem == len(x)-1):
        list1.append(x[elem])
        list2.append(list1)
        list1 = []
    else:
        list1.append(x[elem])

print(list2)