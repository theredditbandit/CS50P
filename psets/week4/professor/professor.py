from random import randint


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        sum = a + b
        i = 0
        while i < 3:
            print(f"{a} + {b} = ", end="")
            try:
                guess = int(input())
            except ValueError:
                print("EEE")
                i += 1
                continue
            else:
                if guess == sum:
                    score += 1
                    break
                else:
                    print("EEE")
                    i += 1
                    continue
        if i == 3:
            print(sum)
        else:
            continue
    print(f"Score: {score}")



def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue
        else:
            if 1 <= n <= 3:
                return n
            else:
                continue


def generate_integer(level):
    if level == 1:
        begin_range = 0
    else:
        begin_range = 10**(level-1)
    end_range = (10**level)-1
    return randint(begin_range, end_range)


if __name__ == "__main__":
    main()
    # print(generate_integer(1))
