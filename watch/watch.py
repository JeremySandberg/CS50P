import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if reg := re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)", s):
        return "https://youtu.be/" + reg.group(1)

if __name__ == "__main__":
    main()