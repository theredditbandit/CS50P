import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(hours):
    try:
        start, end = hours.split("to")
    except ValueError:
        raise ValueError

    start = re.search("^ ?([2-9]|1[0-2]?):?([0-9]+)?( AM| PM)", start.strip(), re.IGNORECASE)
    end = re.search("^ ?([2-9]|1[0-2]?):?([0-9]+)?( AM| PM)",end.strip(), re.IGNORECASE)

    try:
        start.group(1) or start.group(3)
        end.group(1)  or end.group(3)
    except AttributeError:
       raise ValueError

    if start.group(2) and end.group(2):
        if int(start.group(2)) >= 60 or int(end.group(2)) >= 60:
            raise ValueError

    start24 = twelveto24(start)
    end24 = twelveto24(end)

    return f"{start24} to {end24}"


def twelveto24(time):
    hour, minute, ampm = time.group(1).strip(), time.group(2), time.group(3).strip()
    if minute:
        pass
    else:
        minute = "00"

    if ampm == "AM":
        if hour == "12":
            return f"00:{minute}"
        else:
            return f"{hour.zfill(2)}:{minute}"
    else:
        if hour == "12":
            return f"{hour}:{minute}"
        else:
            hour = int(hour)
            hour += 12
            hour = str(hour)
            return f"{hour}:{minute}"


if __name__ == "__main__":
    main()
