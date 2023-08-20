# need to install the pyfiglet module first
from pyfiglet import Figlet
import sys
figlet = Figlet()
allfonts = figlet.getFonts()


def figletify(text, fonts=""):
    if fonts != "":
        figlet.setFont(font=fonts)
    print("Output:\n", figlet.renderText(text), sep="")


if len(sys.argv) == 1:
    text = input("Input: ")
    figletify(text)
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in allfonts:
            text = input("Input: ")
            figletify(text, sys.argv[2])
        else:
            sys.exit(1)
    else:
        sys.exit(1)
else:
    sys.exit(1)
