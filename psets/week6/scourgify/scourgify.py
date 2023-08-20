import sys
from os.path import exists
import csv


def main():
    students = []  # list of dicts
    check_len(sys.argv)
    infile = sys.argv[1]
    outfile = sys.argv[2]
    check_file(infile, "csv")
    check_file(outfile, "csv", infile=False)
    with open(infile) as inf:
        reader = csv.DictReader(inf)
        for i in reader:
            students.append(i)
    cleaned = sanitize(students)
    with open(outfile, "w") as outf:
        writer = csv.DictWriter(outf, fieldnames=["first", "last", "house"])
        writer.writerow({'first':'first', 'last':'last', 'house':'house'})
        for i in cleaned:
            writer.writerow(
                {'first': i['first'].strip(), 'last': i['last'].strip(), 'house': i['house'].strip()})
        # for i in cleaned:
        #     print(i['first'],i['last'],i['house'])


def sanitize(students):
    clean = []
    for student in students:
        last, first = student["name"].split(",")
        clean.append({'first': first, 'last': last, 'house': student['house']})
    return clean


def check_len(args):
    if len(args) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(args) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        pass


def check_file(file, extension, infile=True):
    if infile:
        if exists(file):
            pass
        else:
            print("File does not exist")
            sys.exit(1)
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


main()
