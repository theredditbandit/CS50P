def main():
    print("What time is it? ", end="")
    converted = convert(input())
    # print(converted)
    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")
    else:
        print("", end="")


def convert(time):
    hour, minute = time.split(":")
    # returning a rounded integer value of the time given in 24H format
    return round(int(hour)+int(minute)/60, 2)


if __name__ == "__main__":
    main()
