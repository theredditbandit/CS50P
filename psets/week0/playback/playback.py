string = input()

# This for loop adds "..." everytime it encounters a space 
for i in string:
    if i == ' ':
        print("...", end='')
    else:
        print(i, end='')
