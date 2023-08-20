def main():
    print("Greeting: ", end="")
    print(value(input().strip().lower()))


def value(greeting):  # This block handles checking for hey or hello or anything else
    # print(greeting)
    greeting = greeting.lower()
    if(greeting[2]== "l" and greeting[4] == "o"):
        return 0
    elif(greeting[0]== "h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
