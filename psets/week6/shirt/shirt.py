import sys
from os.path import exists
from PIL import Image, ImageOps


def main():
    check_len(sys.argv)
    infile = sys.argv[1]
    outfile = sys.argv[2]
    ext = verify(infile, outfile)
    background = Image.open(infile)  # muppet
    foreground = Image.open("shirt.png")  # shirt
    background = ImageOps.fit(background, foreground.size)
    # print(f"BG (muppet):{background.size}\nFG (shirt) : {foreground.size}")
    background.paste(foreground, foreground)
    background.save(outfile)


def check_len(args):
    if len(args) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif len(args) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    else:
        pass


def verify(infile, outfile):
    if exists(infile):
        try:
            n1, e1 = infile.split(".")
            n2, e2 = outfile.split(".")
        except ValueError:
            print("Invalid input")
            sys.exit(1)
        else:
            if e1.lower() == e2.lower() and e1.lower() in ["jpg", "png", "jpeg"]:
                # print("Great Success")
                return e2.lower()
            else:
                print("Input and output have different extensions")
                sys.exit(1)
    else:
        print("File does not exist")
        sys.exit(1)


main()
