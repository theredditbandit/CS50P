
def main():
    fraction = input("Fraction:")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    for _ in fraction:
        try:
            a, b = fraction.split("/")
        except(ValueError):
            # raise ValueError("enter in a/b format")
            pass
        else:
            try:
                per = int(a)/int(b)
            except(ValueError):
                raise ValueError("val err")
            except(ZeroDivisionError):
                raise ZeroDivisionError("0 err")
            else:
                if int(a) > int(b):
                    pass
                else:
                    return per*100

def gauge(percentage):

    if isinstance(percentage,int):
        if percentage >= 99:
            return "F"
        elif percentage <= 1:
            return "E"
        else:
            percentage = str(percentage).split('.')
            return percentage[0]+'%'
    else:
        raise ValueError


if __name__ == "__main__":
    main()