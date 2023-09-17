def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[:2].isalpha():
            number = False
            for letter in s[2:]:
                if letter.isnumeric():
                    if not number and letter == "0":
                        return False
                    number = True
                    continue
                elif letter.isalpha():
                    if number:
                        return False
                    continue
                else:
                    return False
            return True
    return False


if __name__ == "__main__":
    main()
