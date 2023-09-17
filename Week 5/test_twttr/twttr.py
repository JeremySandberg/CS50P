

def main():
    ...


def shorten(word):
    twttr = ""

    for letter in word:
        if letter.lower() in ["a","e","i","o","u"]:
            continue
        else:
          twttr += letter

    return twttr

if __name__ == "__main__":
    main()