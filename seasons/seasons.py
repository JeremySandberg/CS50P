from datetime import date
import inflect
import sys

def main():
    print(date_to_minutes(input("Date of birth?: ")))

def date_to_minutes(s):
    try:
        birth = date.fromisoformat(s)
    except:
        sys.exit("Invalid date")
    diff = date.today() - birth
    minutes = int(diff.total_seconds() / 60)
    inflector = inflect.engine()
    return inflector.number_to_words(minutes, andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()