def main():
    print("Expression: ", end="")
    x, y, z = input().split(" ")
    domath(x, y, z)


def domath(int1, operator, int2):
    int1, int2 = float(int1), float(int2)
    if operator == "+":
        print(int1+int2)
    elif operator == "-":
        print(int1-int2)
    elif operator == "*":
        print(int1*int2)
    elif operator == "/":
        print(int1/int2)


main()
