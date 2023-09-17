import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    reg = re.findall("(^|\W)um($|\W)", s, flags=re.IGNORECASE)
    return len(reg)

if __name__ == "__main__":
    main()
