def main():
    message = input("Input: ")
    print(shorten(message))


def isvowel(char):  # checks if char is a vowel
    return char in 'aeiouAEIOU'

def shorten(word):
    for i in word:
        if isvowel(i):
            word = word.replace(i, '')
    return word


if __name__ == "__main__":
    main()