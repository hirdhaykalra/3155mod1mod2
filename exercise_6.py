#Worked with Haley Siharath
grid=[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]
x=int(input("Enter 1-5: "))-1
y=int(input("Enter 1-5: "))-1
grid[y][x] = 1

for elem in grid:
    print(elem)