import sys
def main():
    if len(sys.argv)==2:
        if ".py" in sys.argv[1]:
            number_of_lines=0
            try:
                file=open(sys.argv[1],"r")
            except FileNotFoundError:
                sys.exit("File does not exist")
            l=file.readlines()
            lines = l.copy()
            for line in lines:
                line=line.lstrip()
                if line and not line.startswith("#"):
                    number_of_lines+=1
            print(number_of_lines)
        elif ".py" not in sys.argv[1]:
            sys.exit("Not a Python File")
    elif len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")

print("hello world")
main()