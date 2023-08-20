def isvowel(char):  # checks if char is a vowel
    return char in 'aeiouAEIOU'


message = input("Input: ")

for i in message:
    if isvowel(i):
        # if isvowel() returns true then i get's replaced by a blank space
        message = message.replace(i, '')
print("Output:", message)
