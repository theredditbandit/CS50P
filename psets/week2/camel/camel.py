# Take input
usrinput = input("camelCase: ")

# For loop to iterate over the string to check for camel case

for i in range(0, len(usrinput)):
    # print(i,usrinput[i])
    if usrinput[i].isupper():
        newstr = usrinput[:i]+"_"+usrinput[i].lower()+usrinput[i+1:]
        usrinput = newstr

print("snake_case:", newstr)
