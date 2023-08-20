face = input()

sady = "🙁"
smily = "🙂"
# This for loop block iterates through the entire input and whenever it comes across any patterns that we mention , it basically replaces it with the required space/emoji

for i in face:
    if i == ":":
        print("", end="", sep="")
    elif i == ")":  # closed bracket means smiling
        print(smily, end="", sep="")
    elif i == "(":  # open bracket means frowning
        print(sady, end="", sep="")
    else:
        # catch all condition for when i is not a colon or bracket
        print(i, end="", sep="")
