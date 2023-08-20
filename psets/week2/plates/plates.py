def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(string):

    if 2 <= len(string) <= 6:  # making sure length of string is between 2 and 6
        # checking if first and second character in the string are alphabets
        if string[0].isalpha() and string[1].isalpha():
            # checking if any number occours in between the string
            for i in range(len(string)):
                if string[i].isnumeric():
                    if string[i+1].isalpha():
                        return False
                    # Checking if any number that occurs starts with 0
                    elif string[i] == "0" and string[i-1].isalpha():
                        return False
                    else:
                        return True
            for i in string:  # checking for punctuation occuring in plates
                if i in "-,.":
                    return False
            else:
                return True
        else:
            return False
    else:
        return False


main()
