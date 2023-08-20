names = []
with open("name.txt") as file:
    for line in file:
        names.append(line)

print(names)
for name in sorted(names,reverse=True):
    print(name.rstrip())