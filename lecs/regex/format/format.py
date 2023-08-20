import re

name = input("What's your name? ").strip()

if matches := re.search("^(.+), ?(.+)$",name):
    # last , first = matches.groups() alt approach
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

print(f"hello {name}")