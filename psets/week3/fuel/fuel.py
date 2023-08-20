def main():
    fuel = get_fraction()
    if fuel > 99:
        print("F")
    elif fuel < 1:
        print("E")
    else:
        fuel = str(fuel).split('.')
        print(fuel[0]+'%')


def get_fraction():
    while True:
        Fraction = input("Fraction :")
        for i in Fraction:
            try:
                a, b = Fraction.split("/")
            except(ValueError):
                pass
            else:
                try:
                    per = int(a)/int(b)
                except(ValueError, ZeroDivisionError):
                    pass
                else:
                    if int(a) > int(b):
                        pass
                    else:
                        return per*100


main()
