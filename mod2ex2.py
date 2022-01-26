x = input("Enter a String: ")
y = ""
for i in x:
    if i.islower() == True:
        y = y+i

for i in x:
    if i.isupper() == True:
        y = y+i

print(f"Output: {y}")

#Sources: https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
#Source taught how to use .isupper() and .islower(), which simply determine if every char...
#...in a string is uppercase or lowercase respectively.
