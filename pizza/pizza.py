from tabulate import tabulate
import sys
import csv

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].split(".")[-1] != "csv":
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            page = []
            for row in reader:
                page.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(page, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
