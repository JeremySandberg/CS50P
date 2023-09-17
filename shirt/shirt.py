import sys
from PIL import Image, ImageOps
from os.path import splitext

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif splitext(sys.argv[2])[-1] not in [".jpg",".jpeg",".png"]:
        sys.exit("Invalid output")
    elif splitext(sys.argv[1])[-1] != splitext(sys.argv[2])[-1]:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(sys.argv[1]) as muppet:
            with Image.open("shirt.png") as shirt:
                size = shirt.size
                muppet = ImageOps.fit(muppet, size)
                muppet.paste(shirt, shirt)
                muppet.save(fp=sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
