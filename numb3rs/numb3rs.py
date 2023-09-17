import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if not (reg := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip)):
        return False
    for i in range(1,4):
        if int(reg.group(i)) > 255:
            return False
    return True

if __name__ == "__main__":
    main()