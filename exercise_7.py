#Worked with Haley Siharath
stuff = []
inp = input("Enter QUIT to stop or enter another number: ")
while inp != 'quit' and inp != 'Quit' and inp !='QUIT':
    stuff.append(int(inp))
    inp = input("Enter QUIT to stop or enter another number: ")

evens = []

for elem in stuff:
    if elem%2 == 0:
        evens.append(elem)

print('Evens:')
print(evens)