import re
import sys


def main():
    print(count(input("Text: ")))


def count(text):
    match = re.findall(r"\bum\b",text.lower())
    return len(match)


if __name__ == "__main__":
    main()
