import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    # if ip := validate(input("IPv4 Address: ")):
    #     print(ip)
    # else:
    #     print(ip)
    #     sys.exit(1)


def validate(ip):
    try:
        a,b,c,d = ip.split(".")
    except ValueError:
        # sys.exit(1)
        return False
    if int(a) in range(256) and int(b) in range(256) and int(c) in range(256) and int(d) in range(256):
        return True

    else:
        return False





if __name__ == "__main__":
    main()
