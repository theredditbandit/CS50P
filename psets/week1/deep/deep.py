def main():
    print("What is the Answer to the Great Question of Life, the Universe, and Everything? ", end="")
    check(input().strip())


def check(number): # This block does all the checking to see if the input is equal to 42 or not
    # print(number)
    if(number == "42"):
        print("Yes")

    elif(number.lower() == "forty two"):
        print("Yes")
    elif(number == "forty-two"):
        print("Yes")
    else:
        print("No")


main()
