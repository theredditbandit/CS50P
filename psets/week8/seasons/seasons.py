from datetime import date
import sys
import inflect


def main():
    dob = get_date(input("Date of Birth: "))  # year month date
    dob = date(dob[0], dob[1], dob[2])
    today = date.today()
    timediff = (today-dob).days*24*60

    inflector = inflect.engine()
    inwords = list(inflector.number_to_words(timediff, one=""))
    inwords[0] = inwords[0].upper()
    inwords = ''.join(inwords)
    words = inwords.split()
    for i in words:
        if i == "and":
            words.remove("and")
    words.append("minutes")
    inwords = ' '.join(words)
    # print(words)
    print(inwords)


def get_date(dob):
    if not dob:
        sys.exit(1)
    try:
        dob = dob.split("-")
        for i in range(3):
            # converting numbers from string to int to pass to the date function
            dob[i] = int(dob[i])
        date(dob[0], dob[1], dob[2])
    except (ValueError, IndexError):
        sys.exit(1)
    return dob


if __name__ == "__main__":
    main()
