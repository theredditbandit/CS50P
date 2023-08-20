months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def main():
    while True:
        date = input("Date: ")
        if "/" in date:
            m, d, y = date.split("/")
            if int(m) < 12 and int(d) < 31:
                ISO_8061(m, d, y)
                break
        else:
            m, d, y = date.split(" ")
            if m in months:
                m = months.index(m)
                d = d.rstrip(',')
                if int(d) < 31:
                    ISO_8061(m+1, d, y)
                    break
            else:
                pass


def ISO_8061(month, date, year):
    month = str(month).zfill(2)
    date = str(date).zfill(2)
    print(f"{year}-{month}-{date:02}")


main()
