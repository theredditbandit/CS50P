def main():
    print("Greeting: ", end="")
    check(input().strip())


def check(greeting):  # This block handles checking for hey or hello or anything else
    # print(greeting)
    # greeting = greeting.lower()
    if(greeting[2].lower() == "l" and greeting[4].lower() == "o"):
        print("$0")
    elif(greeting[0].lower() == "h"):
        print("$20")
    else:
        print("$100")

main()
