import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].split(".")[-1] != "csv":
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.reader(file)
            page = "first,last,house\n"
            for row in reader:
                if row[0] == "name": continue
                last, first = row[0].replace(" ","").split(",")
                page += (f"{first},{last},{row[1]}\n")

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        file.write(page)

if __name__ == "__main__":
    main()
