import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].split(".")[-1] != "py":
        sys.exit("Not a Python file")

    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count_lines(lines))

def count_lines(lines):
    count = 0
    for line in lines:
        line = line.lstrip()
        if len(line) == 0 or line[0] == "#":
            continue
        count +=1
    return count

if __name__ == "__main__":
    main()
