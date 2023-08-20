import sys
from os.path import exists


def main():
    lines = []
    arg1 = check_len(sys.argv)
    check_file(arg1)

    with open(arg1) as file:
        l = file.readlines()
        lines = l.copy()
    n = count(lines)
    print(n)


def count(lines):
    noblanks = [i for i in lines if i.strip() != ""]
    working = [i for i in noblanks if i.strip()[0] != "#"]
    return len(working)


def check_len(args):
    if len(args) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(args) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(args) == 2:
        return args[1]


def check_file(file):
    if exists(file):
        try:
            name, ext = file.split(".")
        except ValueError:
            print("Not a python file")
            sys.exit(1)
        else:
            if ext == "py":
                # print("Great Success!")
                pass
            else:
                print("Not a python file")
                sys.exit(1)
    else:
        print("File does not exist")
        sys.exit(1)


main()
