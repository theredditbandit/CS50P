names = []
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except(EOFError):
        print("\nAdieu, adieu, to ", end="")
        if len(names) == 2:
            print(f"{names[0]} and {names[1]}")
        else:
            for i in range(len(names)):
                if i == len(names)-2:  # to add an and at second last position
                    print(f"{names[i]}, and ", end="")
                elif i == len(names)-1:  # to avoid the "," at the last position
                    print(names[i], "", end="", sep="")
                else:
                    print(names[i], ", ", end="", sep="")
            print()
        break
