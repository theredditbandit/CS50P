import sys
from os.path import exists
import csv
from tabulate import tabulate


def main():
    students = []  # list of dicts
    arg1 = check_len(sys.argv)
    check_file(arg1, "csv")
    with open(arg1) as file:
        reader = csv.reader(file)
        for i in reader:
            students.append(i)
    print(tabulate(students,headers="firstrow",tablefmt="grid"))


def check_len(args):
    if len(args) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(args) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(args) == 2:
        return args[1]


def check_file(file, extension):
    if exists(file):
        try:
            name, ext = file.split(".")
        except ValueError:
            print(f"Not a {extension} file")
            sys.exit(1)
        else:
            if ext == extension:
                # print("Great Success!")
                pass
            else:
                print(f"Not a {extension} file")
                sys.exit(1)
    else:
        print("File does not exist")
        sys.exit(1)


main()
