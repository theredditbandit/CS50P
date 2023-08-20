import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(html):
    if link := re.search("https?://(?:www\.)?youtube\.com/embed/([a-z0-9-_]+)",html,re.IGNORECASE):
        for i in link.groups(1):
            return "https://youtu.be/" + i
        # return link.groups(1)


if __name__ == "__main__":
    main()
