import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    reg = re.findall("([0-9]{1,2}):?([0-9][0-9])? (A|P)M", s)
    if len(reg) != 2 or "to" not in s:
        raise ValueError

    convert = []
    for hour, minutes, pre in reg:
        if minutes == "":
            minutes = "00"
        if int(hour) > 12 or int(minutes) > 59:
            raise ValueError
        if hour == "12":
            hour = "00"
        if pre == "P":
            hour = str(int(hour)+12)
        convert.append(f"{hour:>02}:{minutes:>02}")

    return " to ".join(convert)

if __name__ == "__main__":
    main()