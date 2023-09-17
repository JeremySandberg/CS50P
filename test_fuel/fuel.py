def main():
    while True:
        inp = input("Fraction: ")
        try:
            fraction = convert(inp)
        except (ValueError, ZeroDivisionError):
            print("Incorrect input")
            continue
        print(gauge(fraction))
        break

def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdigit() or not y.isdigit() or float(x) > float(y):
            raise ValueError
    if float(y) == 0:
        raise ZeroDivisionError
    return round((float(x) / float(y))*100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
